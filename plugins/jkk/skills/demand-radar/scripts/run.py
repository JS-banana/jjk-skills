#!/usr/bin/env python3
"""Validate demand-radar rows and emit lark-cli batch JSON."""

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse


FIELDS = [
    "标题",
    "一句话痛点",
    "社区反响",
    "需求方向",
    "产品形态",
    "需求强度",
    "需求普遍性",
    "优先级",
    "处理状态",
    "原文内容",
    "原始链接",
    "来源平台",
    "语言",
]

DIRECTIONS = {
    "效率工具", "生活好物", "学习成长", "健康管理", "财务理财", "旅行出行",
    "育儿教育", "社交娱乐", "工作方法", "创作工具", "开发者工具", "其他",
}

FORMS = {
    "手机App", "微信小程序", "网站/Web应用", "桌面应用", "浏览器插件", "硬件产品",
    "实体商品", "服务", "内容产品", "API/SDK", "其他",
}

STRENGTH = {"强": 3, "中": 2, "弱": 1}
UNIVERSALITY = {"高": 3, "中": 2, "低": 1}
LANGUAGES = {"中文", "英文", "双语"}
STATUSES = {"待评估", "有价值", "无价值", "待观察"}


def priority(strength, universality, p0_evidence=""):
    score = STRENGTH.get(strength, 1) * UNIVERSALITY.get(universality, 1)
    if score >= 9:
        return "P0-立即行动" if str(p0_evidence).strip() else "P1-重点考虑"
    if score >= 6:
        return "P1-重点考虑"
    if score >= 3:
        return "P2-观察中"
    return "P3-待观察"


def load_records(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        if isinstance(data.get("fields"), list) and isinstance(data.get("rows"), list):
            fields = data["fields"]
            return [dict(zip(fields, row)) for row in data["rows"]]
        for key in ("records", "rows", "signals"):
            if isinstance(data.get(key), list):
                return data[key]
    raise ValueError("input must be a list or contain records/rows/signals")


def valid_url(value):
    parsed = urlparse(value or "")
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(record):
    errors = []
    required = ["标题", "一句话痛点", "社区反响", "原文内容", "原始链接", "来源平台"]
    for field in required:
        if not str(record.get(field, "")).strip():
            errors.append(f"missing {field}")

    if not valid_url(record.get("原始链接", "")):
        errors.append("原始链接 must be http(s) URL")

    if len(str(record.get("一句话痛点", "")).strip()) > 80:
        errors.append("一句话痛点 too long")

    if len(str(record.get("原文内容", "")).strip()) < 40:
        errors.append("原文内容 too short to prove original evidence was read")

    if record.get("需求方向", "其他") not in DIRECTIONS:
        errors.append("invalid 需求方向")

    if record.get("产品形态", "其他") not in FORMS:
        errors.append("invalid 产品形态")

    if record.get("需求强度", "中") not in STRENGTH:
        errors.append("invalid 需求强度")

    if record.get("需求普遍性", "中") not in UNIVERSALITY:
        errors.append("invalid 需求普遍性")

    if record.get("语言", "中文") not in LANGUAGES:
        errors.append("invalid 语言")

    if record.get("处理状态", "待评估") not in STATUSES:
        errors.append("invalid 处理状态")

    return errors


def normalize(record):
    strength = record.get("需求强度", "中")
    universality = record.get("需求普遍性", "中")
    p0_evidence = record.get("P0证据") or ""
    normalized = {
        "标题": record.get("标题", "").strip(),
        "一句话痛点": record.get("一句话痛点", "").strip(),
        "社区反响": record.get("社区反响", "").strip(),
        "需求方向": record.get("需求方向", "其他"),
        "产品形态": record.get("产品形态", "其他"),
        "需求强度": strength,
        "需求普遍性": universality,
        "优先级": priority(strength, universality, p0_evidence),
        "处理状态": record.get("处理状态", "待评估"),
        "原文内容": record.get("原文内容", "").strip()[:5000],
        "原始链接": record.get("原始链接", "").strip(),
        "来源平台": record.get("来源平台", "").strip(),
        "语言": record.get("语言", "中文"),
    }
    return normalized


def build(records):
    accepted = []
    rejected = []
    for index, record in enumerate(records, 1):
        if not isinstance(record, dict):
            rejected.append({
                "index": index,
                "title": "",
                "url": "",
                "reasons": ["record must be an object"],
            })
            continue
        errors = validate(record)
        if errors:
            rejected.append({
                "index": index,
                "title": record.get("标题") or record.get("title") or "",
                "url": record.get("原始链接") or record.get("url") or "",
                "reasons": errors,
            })
            continue
        accepted.append(normalize(record))

    rows = [[record[field] for field in FIELDS] for record in accepted]
    return {"fields": FIELDS, "rows": rows}, {"accepted": len(accepted), "rejected": rejected}


def self_check():
    sample = [{
        "标题": "目标追踪工具坚持困难",
        "一句话痛点": "用户想管理多个生活目标，但现有工具太复杂导致更焦虑",
        "社区反响": "35赞，104评论",
        "需求方向": "效率工具",
        "产品形态": "手机App",
        "需求强度": "中",
        "需求普遍性": "高",
        "原文内容": "我想把工作、健康和个人目标都整理起来，但每次试 App 都坚持不下去。功能一多就像又多了一个要管理的东西，最后反而更焦虑。",
        "原始链接": "https://reddit.com/r/productivity/comments/example",
        "来源平台": "Reddit",
        "语言": "英文",
    }]
    payload, report = build(sample)
    assert report == {"accepted": 1, "rejected": []}
    assert payload["rows"][0][7] == "P1-重点考虑"
    assert build([dict(zip(payload["fields"], payload["rows"][0]))])[1]["accepted"] == 1
    sample[0]["需求强度"] = "强"
    sample[0]["需求普遍性"] = "高"
    assert build(sample)[0]["rows"][0][7] == "P1-重点考虑"
    sample[0]["P0证据"] = "用户明确愿意付费购买"
    assert build(sample)[0]["rows"][0][7] == "P0-立即行动"
    # P0证据 显式为 None 时不应误判 P0（str(None) 真值 bug 回归测试）
    none_p0 = dict(sample[0])
    none_p0["P0证据"] = None
    assert build([none_p0])[0]["rows"][0][7] == "P1-重点考虑"
    # 非法 处理状态 必须被拒
    bad_status = dict(sample[0])
    bad_status["处理状态"] = "不存在的状态"
    rejected = build([bad_status])[1]["rejected"]
    assert rejected and "invalid 处理状态" in rejected[0]["reasons"]


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output", default="/tmp/demand-radar-feishu.json")
    parser.add_argument("--report", default="/tmp/demand-radar-report.json")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)

    if args.self_check:
        self_check()
        print("self-check passed")
        return 0

    if not args.input:
        parser.error("--input is required unless --self-check is used")

    payload, report = build(load_records(args.input))
    Path(args.output).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    if report["rejected"]:
        print(f"accepted={report['accepted']} rejected={len(report['rejected'])}", file=sys.stderr)
        return 1

    print(f"accepted={report['accepted']} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
