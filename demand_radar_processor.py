#!/usr/bin/env python3
"""
Demand Radar v2 - 数据处理脚本
读取采集的原始数据，进行AI判断和评分，然后写入飞书表格
"""

import json
import os
import sys

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from demand_radar_prompts import (
    DEMAND_REALITY_PROMPT,
    DEMAND_STRENGTH_PROMPT,
    DEMAND_SOLVABILITY_PROMPT,
    PAIN_POINT_PROMPT,
    DEMAND_DIRECTION_PROMPT,
    PRODUCT_FORM_PROMPT,
    calculate_priority
)

OUTPUT_DIR = os.path.expanduser("~/my-code/skills/demand_radar_data")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_raw_data(filename: str) -> list:
    """加载原始数据"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    if not os.path.exists(filepath):
        return []
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 支持两种格式：直接数组 或 {data: [...]}
    if isinstance(data, list):
        return data
    elif isinstance(data, dict) and "data" in data:
        return data["data"]
    else:
        return []


def save_processed_data(data: list, filename: str):
    """保存处理后的数据"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 保存 {len(data)} 条数据到 {filepath}")
    return filepath


def prepare_feishu_records(data: list) -> dict:
    """
    准备飞书写入数据
    
    字段：标题、一句话痛点、需求方向、产品形态、需求强度、需求普遍性、可解决性、
         匹配度、优先级、状态、评分理由、原文内容、原始链接、来源平台、语言
    """
    fields = [
        "标题", "一句话痛点", "需求方向", "产品形态", 
        "需求强度", "需求普遍性", "可解决性", "匹配度",
        "优先级", "状态", "评分理由", "原文内容", 
        "原始链接", "来源平台", "语言"
    ]
    
    rows = []
    for item in data:
        row = [
            item.get("标题", ""),
            item.get("一句话痛点", ""),
            item.get("需求方向", "其他"),
            item.get("产品形态", "其他"),
            item.get("需求强度", "中"),
            item.get("需求普遍性", "中"),
            item.get("可解决性", "中"),
            item.get("匹配度", ""),  # 需要手动填写
            item.get("优先级", "P2-观察中"),
            item.get("状态", "待复核"),
            item.get("评分理由", ""),
            item.get("原文内容", "")[:5000],  # 限制长度
            item.get("原始链接", ""),
            item.get("来源平台", ""),
            item.get("语言", "中文")
        ]
        rows.append(row)
    
    return {"fields": fields, "rows": rows}


def merge_data(*data_lists) -> list:
    """合并多个数据列表"""
    merged = []
    for data in data_lists:
        merged.extend(data)
    return merged


if __name__ == "__main__":
    print("Demand Radar v2 数据处理脚本")
    print(f"数据目录: {OUTPUT_DIR}")
    
    # 列出可用的数据文件
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".json")]
    print(f"可用数据文件: {files}")
