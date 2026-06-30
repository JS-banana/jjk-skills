#!/usr/bin/env python3
"""
Sync vendor campaign data from JSONL to Feishu Bitable.
Reads vendor_campaign_seen.jsonl, checks what's already in Bitable,
and creates records for new campaigns.

Usage:
  python3 campaign_bitable_sync.py          # sync all new records
  python3 campaign_bitable_sync.py --dry    # show what would be synced
  python3 campaign_bitable_sync.py --write '{"vendor":"X","campaign":"Y",...}'
                                          # write a single record directly

Dependencies: None beyond stdlib. Uses urllib for Feishu API.
Config: Reads app credentials from env vars or ~/.openclaw/openclaw.json

Write contract and field defaults are defined in the ai-vendor-campaign-radar skill.
"""

from __future__ import annotations
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta

SEEN_FILE = os.path.expanduser("~/.hermes/scripts/vendor_campaign_seen.jsonl")
CONFIG_FILE = os.path.expanduser("~/.openclaw/openclaw.json")
APP_TOKEN = "MJpIbpWkSaLN0tsSQoTcn4QDnId"
TABLE_ID = "tblYhMRh3fJ0FDfW"
TIMEOUT = 30

# ─── Feishu API helpers ───────────────────────────────────────────────

def load_config():
    # Check env vars first (same priority as feishu_bitable.py)
    for app_id_key, app_secret_key in [
        ("ZAIZAI_FEISHU_APP_ID", "ZAIZAI_FEISHU_APP_SECRET"),
        ("FEISHU_APP_ID", "FEISHU_APP_SECRET"),
    ]:
        app_id = os.environ.get(app_id_key, "").strip()
        app_secret = os.environ.get(app_secret_key, "").strip()
        if app_id and app_secret:
            return app_id, app_secret

    # Fallback to config file
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    feishu_cfg = cfg.get("channels", {}).get("feishu", {})
    accounts = feishu_cfg.get("accounts", {})
    if isinstance(accounts, dict):
        acct = accounts.get("default", {})
    else:
        acct = {}
    app_id = str(acct.get("appId") or feishu_cfg.get("appId") or "").strip()
    app_secret = str(acct.get("appSecret") or feishu_cfg.get("appSecret") or "").strip()
    if not app_id or not app_secret:
        raise RuntimeError("Feishu app credentials not found in env or openclaw.json")
    return app_id, app_secret


def get_token():
    app_id, app_secret = load_config()
    resp = api_request(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        method="POST",
        payload={"app_id": app_id, "app_secret": app_secret},
    )
    return resp["tenant_access_token"]


def api_request(url, *, method="GET", token=None, payload=None):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    parsed = json.loads(raw)
    code = parsed.get("code", 0)
    if code not in (0, None):
        raise RuntimeError(f"Feishu API code={code}: {parsed.get('msg', '')}")
    return parsed


# ─── Bitable operations ───────────────────────────────────────────────

def serialize_url(url, text=None):
    return {"link": url, "text": text or url}


def list_existing_campaigns(token):
    """Get all existing campaign names from Bitable for dedup."""
    items = []
    page_token = ""
    while True:
        q = {"page_size": 500}
        if page_token:
            q["page_token"] = page_token
        qs = urllib.parse.urlencode(q)
        resp = api_request(
            f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records?{qs}",
            token=token,
        )
        data = resp.get("data", {})
        items.extend(data.get("items", []))
        if not data.get("has_more"):
            break
        page_token = str(data.get("page_token", ""))
        if not page_token:
            break
    # Return set of (vendor, campaign_name) for dedup
    existing = set()
    for item in items:
        fields = item.get("fields", {})
        name = fields.get("活动名称", "")
        vendor = ""
        if isinstance(fields.get("厂商"), dict):
            vendor = fields["厂商"].get("text", "") or fields["厂商"].get("value", "")
        elif isinstance(fields.get("厂商"), str):
            vendor = fields["厂商"]
        existing.add(f"{vendor}|{name}".lower().strip())
    return existing


def create_record(fields, token):
    """Create a single record in Bitable."""
    resp = api_request(
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records",
        method="POST",
        token=token,
        payload={"fields": fields},
    )
    return resp.get("data", {}).get("record", {})


# ─── Data mapping ─────────────────────────────────────────────────────

def score_to_advice(score):
    """Map numeric score (1-5) to advice text."""
    s = int(score)
    if s >= 5: return "立即行动"
    if s >= 4: return "值得做"
    if s >= 3: return "观望"
    return "跳过"


def date_to_ms(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    dt = dt.replace(tzinfo=timezone(timedelta(hours=8)))
    return int(dt.timestamp() * 1000)


def score_to_int(score):
    """Normalize score to integer 1-5. Handles legacy 5-25 scale and star strings."""
    if isinstance(score, str) and '⭐' in score:
        return max(1, min(5, score.count('⭐')))
    s = int(score)
    if s > 5:  # legacy 5-25 scale
        if s >= 20: return 5
        if s >= 18: return 4
        if s >= 15: return 3
        if s >= 11: return 2
        return 1
    return max(1, min(5, s))


def jsonl_record_to_bitable_fields(rec):
    """Convert a JSONL seen record to Bitable fields dict."""
    vendor = rec.get("vendor", "其他")
    campaign = rec.get("campaign", "")
    score = rec.get("score", 0)
    url = rec.get("url", "")
    seen_at = rec.get("seen_at", datetime.now().strftime("%Y-%m-%d"))
    now_ms = int(datetime.now(tz=timezone(timedelta(hours=8))).timestamp() * 1000)
    # Clean vendor name (remove parenthetical)
    clean_vendor = vendor.split(" (")[0] if " (" in vendor else vendor
    return {
        "活动名称": campaign,
        "厂商": clean_vendor,
        "活动类型": "其他",          # Single-select, agent should override
        "难度评级": "⭐⭐⭐ 需花时间",  # Single-select, agent should override
        "难度说明": "",
        "奖励详情": campaign.split(" - ")[-1] if " - " in campaign else "",
        "活动形式": "",
        "参与方式": "",
        "获奖条件": "",
        "时间节点备注": "",
        "推荐指数": score_to_int(score),  # Number type, integer 1-5
        "建议": score_to_advice(score),   # Single-select, derived from score
        "状态": "新发现",                  # Single-select
        "开始时间": date_to_ms(seen_at),
        "报名入口": serialize_url(url),
        "官方确认": "⚠️ 疑似",             # Single-select, agent should override
        "地区": "全球",                     # Single-select, agent should override
        "奖励类型": ["其他"],               # Multi-select, agent should override
        "来源渠道": "其他",                 # Single-select, agent should override
        "预计投入": "1-3天",                # Single-select, agent should override
        "发现日期": now_ms,
    }


# ─── Main ─────────────────────────────────────────────────────────────

def load_seen():
    """Load all records from JSONL."""
    records = []
    if not os.path.exists(SEEN_FILE):
        return records
    with open(SEEN_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def sync_all(dry_run=False):
    """Sync all new JSONL records to Bitable."""
    seen = load_seen()
    if not seen:
        print("JSONL 文件为空，无记录可同步")
        return 0

    token = get_token()
    existing = list_existing_campaigns(token)

    new_records = []
    for rec in seen:
        vendor = rec.get("vendor", "")
        clean_v = vendor.split(" (")[0] if " (" in vendor else vendor
        key = f"{clean_v}|{rec.get('campaign', '')}".lower().strip()
        if key not in existing:
            new_records.append(rec)

    if not new_records:
        print("所有记录已存在于多维表格中，无需同步")
        return 0

    print(f"发现 {len(new_records)} 条新记录待同步:")
    for rec in new_records:
        print(f"  - [{rec.get('vendor')}] {rec.get('campaign')}")

    if dry_run:
        print("\n[DRY RUN] 以上记录将被同步，但未实际写入")
        return len(new_records)

    created = 0
    for rec in new_records:
        fields = jsonl_record_to_bitable_fields(rec)
        try:
            create_record(fields, token)
            created += 1
            print(f"  ✅ 已写入: {rec.get('campaign', '')[:50]}")
        except Exception as e:
            print(f"  ❌ 写入失败: {e}")

    print(f"\n同步完成: {created}/{len(new_records)} 条新记录已写入多维表格")
    return created


# Fields that agent can override via --write JSON
OVERRIDE_FIELDS = (
    "活动类型", "难度评级", "难度说明", "奖励详情", "活动形式",
    "参与方式", "获奖条件", "时间节点备注", "官方确认", "状态",
    "地区", "奖励类型", "来源渠道", "预计投入", "截止时间",
    "活动详情链接", "建议",
)


def write_single(json_str):
    """Write a single record directly (used by agent after scanning)."""
    rec = json.loads(json_str)
    token = get_token()

    # Check dedup
    existing = list_existing_campaigns(token)
    vendor = rec.get("vendor", "")
    clean_v = vendor.split(" (")[0] if " (" in vendor else vendor
    key = f"{clean_v}|{rec.get('campaign', '')}".lower().strip()
    if key in existing:
        print(f"SKIP: 记录已存在 - {rec.get('campaign', '')}")
        return

    # Build fields with defaults, then apply overrides
    fields = jsonl_record_to_bitable_fields(rec)
    for k in OVERRIDE_FIELDS:
        if k in rec and rec[k]:
            fields[k] = rec[k]

    result = create_record(fields, token)
    rid = result.get("record_id", "")
    print(f"OK: {rid} - {rec.get('campaign', '')}")


def main():
    parser = argparse.ArgumentParser(description="Sync campaign data to Feishu Bitable")
    parser.add_argument("--dry", action="store_true", help="Dry run")
    parser.add_argument("--write", type=str, help="Write a single record (JSON)")
    args = parser.parse_args()

    if args.write:
        write_single(args.write)
    else:
        sync_all(dry_run=args.dry)


if __name__ == "__main__":
    main()
