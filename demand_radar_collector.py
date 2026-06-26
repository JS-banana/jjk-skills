#!/usr/bin/env python3
"""
Demand Radar - 需求信号采集与分析系统
读取原始采集数据，通过AI分析提取结构化需求，写入本地JSON
"""

import json
import os
from datetime import datetime

# 输出目录
OUTPUT_DIR = os.path.expanduser("~/my-code/skills/demand_radar_data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# AI分析prompt模板
ANALYSIS_PROMPT = """你是一个产品需求分析专家。请分析以下用户表达，提取其中的产品需求信号。

## 原始数据
{raw_data}

## 分析要求

对每条数据，提取以下信息：

1. **标题**：用≤50字概括核心需求
2. **需求描述**：详细描述用户痛点（100-200字）
3. **用户原话**：保留最能体现需求的原始表达（≤200字）
4. **需求类别**：从以下选择1-3个：效率工具/开发工具/AI应用/设计工具/营销工具/财务管理/健康医疗/教育培训/生活服务/数据分析/其他
5. **五维评分**（每项1-5分）：
   - 痛点强度：用户有多痛？1=轻微不便 3=明显痛点 5=严重阻碍
   - 出现频率：这个需求出现频率如何？1=单次 3=偶见 5=高频
   - 付费意愿：用户愿意付钱吗？1=肯定不付 3=可能 5=明确愿意
   - 竞争缺口：现有方案差不差？1=成熟方案多 3=有但不满 5=完全没有
   - 实现难度：你能不能做？1=极难 3=中等 5=简单前端工具
6. **综合评分**：= 痛点强度×0.25 + 付费意愿×0.25 + 出现频率×0.20 + 竞争缺口×0.20 + 实现难度×0.10

## 输出格式

返回JSON数组，每条记录格式：
```json
{{
  "标题": "...",
  "需求描述": "...",
  "用户原话": "...",
  "原始链接": "...",
  "来源平台": "Reddit/V2EX/小红书/PH/HN/Twitter",
  "市场": "英文/中文/全球",
  "需求类别": ["效率工具", "AI应用"],
  "痛点强度": 4,
  "出现频率": 3,
  "付费意愿": 4,
  "竞争缺口": 3,
  "实现难度": 4,
  "综合评分": 3.65,
  "处理状态": "待评估",
  "标签": []
}}
```

注意：
- 如果原始数据不是真实的需求/痛点信号（比如只是新闻、闲聊、广告），跳过它
- 评分要客观，不要虚高
- 综合评分保留2位小数
- 标签从以下选择：高频需求/付费意愿强/竞品缺口/新技术驱动/本地化机会
"""

def save_results(signals: list, filename: str = None):
    """保存分析结果到JSON文件"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"demand_signals_{timestamp}.json"
    
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    output = {
        "collected_at": datetime.now().isoformat(),
        "total_signals": len(signals),
        "signals": signals
    }
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 保存 {len(signals)} 条需求信号到 {filepath}")
    return filepath

def load_latest():
    """加载最新的采集结果"""
    files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.startswith("demand_signals_")])
    if not files:
        return None
    filepath = os.path.join(OUTPUT_DIR, files[-1])
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    print(f"Demand Radar 数据目录: {OUTPUT_DIR}")
    latest = load_latest()
    if latest:
        print(f"最新采集: {latest['collected_at']}, 共 {latest['total_signals']} 条")
    else:
        print("暂无采集数据")
