#!/usr/bin/env python3
"""Verify Bitable field schema matches what campaign_bitable_sync.py expects.

Usage: python3 ~/.hermes/scripts/vendor_campaign_seen.jsonl/../verify_bitable_fields.py
       (or just python3 verify_bitable_fields.py from the skill scripts dir)

Lists all fields in the Bitable table and checks for known required fields.
Use this after Bitable schema changes or when FieldNameNotFound errors occur.
"""
import json, os, sys

# Import the sync module for credentials
sys.path.insert(0, os.path.expanduser("~/.hermes/scripts"))
from importlib.machinery import SourceFileLoader
mod = SourceFileLoader("sync", os.path.expanduser("~/.hermes/scripts/campaign_bitable_sync.py")).load_module()

token = mod.get_token()
import urllib.request

# Fetch all fields
fields = []
page_token = ""
while True:
    q = f"?page_size=100" + (f"&page_token={page_token}" if page_token else "")
    req = urllib.request.Request(
        f'https://open.feishu.cn/open-apis/bitable/v1/apps/{mod.APP_TOKEN}/tables/{mod.TABLE_ID}/fields{q}',
        headers={'Authorization': f'Bearer {token}'})
    resp = json.loads(urllib.request.urlopen(req, timeout=30).read())
    items = resp.get('data', {}).get('items', [])
    fields.extend(items)
    if not resp.get('data', {}).get('has_more'):
        break
    page_token = resp['data'].get('page_token', '')

TYPE_MAP = {1: 'Text', 2: 'Number', 3: 'SingleSelect', 4: 'MultiSelect', 5: 'Date', 15: 'URL'}

print(f"=== Bitable Fields ({len(fields)}) ===")
for f in fields:
    t = TYPE_MAP.get(f['type'], f'type={f["type"]}')
    print(f"  {f['field_name']:20s} | {t}")

# Check required fields the script writes
REQUIRED = [
    '活动名称', '厂商', '活动类型', '难度评级', '推荐指数', '难度说明',
    '奖励详情', '活动形式', '参与方式', '获奖条件', '时间节点备注',
    '建议', '状态', '报名入口', '官方确认', '开始时间', '截止时间',
    '地区', '奖励类型', '发现日期', '来源渠道', '预计投入',
]
existing_names = {f['field_name'] for f in fields}
missing = [r for r in REQUIRED if r not in existing_names]
if missing:
    print(f"\n⚠️ MISSING FIELDS (will cause FieldNameNotFound): {missing}")
else:
    print(f"\n✅ All {len(REQUIRED)} required fields present")
