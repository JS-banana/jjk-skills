#!/usr/bin/env python3
"""
Demand Radar v2 - 需求证据采集系统
采集"问题证据"而非"想法"，保存完整原文，全中文化
"""

import json
import os
import hashlib
from datetime import datetime

OUTPUT_DIR = os.path.expanduser("~/my-code/skills/demand_radar_data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 需求证据分析 prompt - 中文版
EVIDENCE_ANALYSIS_PROMPT = """你是一个产品需求分析专家。你的任务是分析用户表达，提取其中的**问题证据**，而不是泛泛的想法。

## 核心判断原则
不要收集"想法"，要收集"问题证据"。一个需求必须能回答：
1. **谁**遇到了什么**任务阻塞**？
2. 为什么**现有方案不够好**？
3. 他为了解决这个问题**付出了什么代价**？
4. 这个问题是不是**反复出现**？
5. 有没有**钱、时间、流量、声誉、交付压力**在背后支撑？

## 原始数据
{raw_data}

## 分析要求

对每条数据，提取以下信息：

### 基础信息
1. **标题**：用≤50字概括核心问题（不是功能需求，是问题描述）
2. **用户角色**：谁遇到的问题？（前端开发者/独立开发者/AI编程用户/内容创作者/运营人员等）
3. **任务场景**：什么任务被阻塞了？（手动整理2小时/多人协作同步/API限额导致工作中断等）
4. **当前方案**：用户现在怎么解决？（用什么工具/流程/变通办法）
5. **变通方法**：用户的workaround是什么？（写了什么脚本/Excel/自动化来绕开问题）
6. **原文内容**：完整保留原始内容，不要摘要

### 证据强度判断
- **强证据**：明确痛点 + 付费信号（愿意付钱/找外包/发招聘/参加黑客松）
- **中证据**：明确痛点但无付费信号
- **弱证据**：泛泛表达或单一来源

### 100分制评分
1. **痛感强度**（0-20分）：用户是否明确表达卡住、损失、烦躁、风险？比如"每次手动2小时""这个限制导致我没法用"
2. **频率**（0-20分）：同类问题是否在多个来源重复出现？单个平台20条不如5个不同平台各5条
3. **付费/投入信号**（0-15分）：是否有人付费买竞品、找外包、发招聘、参加黑客松、订阅服务？
4. **人群清晰度**（0-10分）：能否明确是前端开发者、独立开发者、AI编程用户、内容创作者？
5. **当前方案不满**（0-10分）：是否已有替代品，但用户仍抱怨贵/复杂/不稳定/学习成本高/国内不可用？
6. **趋势增长**（0-10分）：最近7天/30天是否明显增加？
7. **能力匹配**（0-10分）：你能否用前端/Agent/自动化/飞书集成快速做MVP？
8. **分发可行性**（0-5分）：目标用户聚集地是否可触达？V2EX/GitHub/Product Hunt/掘金/Chrome Web Store

## 输出格式

返回JSON数组，每条记录格式：
```json
{{
  "标题": "问题描述（≤50字）",
  "用户角色": "前端开发者/独立开发者/AI编程用户/...",
  "任务场景": "什么任务被阻塞",
  "当前方案": "用户现在怎么解决",
  "变通方法": "用户的workaround",
  "原文内容": "完整原始内容",
  "原始链接": "...",
  "来源平台": "GitHub/V2EX/Stack Overflow/Product Hunt/Hacker News/小红书/...",
  "来源类型": "A级-强需求源/B级-产品市场信号/C级-趋势机会源/D级-弱信号灵感",
  "市场": "英文/中文/全球",
  "需求类别": ["效率工具", "AI应用"],
  "证据强度": "强-明确痛点+付费信号/中-明确痛点但无付费/弱-泛泛表达或单一来源",
  "痛感强度分": 15,
  "频率分": 12,
  "付费投入分": 8,
  "人群清晰度分": 7,
  "方案不满分": 6,
  "趋势增长分": 5,
  "能力匹配分": 8,
  "分发可行性分": 4,
  "需求总分": 65,
  "处理状态": "待评估",
  "标签": ["高频需求", "付费意愿强"]
}}
```

## 关键原则
- 如果原始数据不是真实的问题/痛点信号（比如只是新闻、闲聊、广告、泛泛的"求推荐"），跳过它
- 评分要客观，不要虚高
- 需求总分 = 痛感强度 + 频率 + 付费投入 + 人群清晰度 + 方案不满 + 趋势增长 + 能力匹配 + 分发可行性
- 标签从以下选择：高频需求/付费意愿强/竞品缺口/新技术驱动/本地化机会/开发者工具/AI编程/自动化/飞书生态
"""

def calculate_total_score(scores: dict) -> int:
    """计算需求总分"""
    return sum([
        scores.get("痛感强度分", 0),
        scores.get("频率分", 0),
        scores.get("付费投入分", 0),
        scores.get("人群清晰度分", 0),
        scores.get("方案不满分", 0),
        scores.get("趋势增长分", 0),
        scores.get("能力匹配分", 0),
        scores.get("分发可行性分", 0)
    ])

def deduplicate_hash(item: dict) -> str:
    """生成去重hash"""
    key = f"{item.get('标题', '')}{item.get('来源平台', '')}{item.get('原始链接', '')}"
    return hashlib.md5(key.encode()).hexdigest()[:12]

def save_evidence(evidence_list: list, filename: str = None):
    """保存需求证据到JSON文件"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"demand_evidence_{timestamp}.json"
    
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # 添加去重hash
    for item in evidence_list:
        item["_hash"] = deduplicate_hash(item)
        item["_collected_at"] = datetime.now().isoformat()
    
    output = {
        "version": "2.0",
        "collected_at": datetime.now().isoformat(),
        "total_evidence": len(evidence_list),
        "evidence": evidence_list
    }
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 保存 {len(evidence_list)} 条需求证据到 {filepath}")
    return filepath

def load_latest():
    """加载最新的采集结果"""
    files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.startswith("demand_evidence_")])
    if not files:
        return None
    filepath = os.path.join(OUTPUT_DIR, files[-1])
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    print(f"Demand Radar v2 数据目录: {OUTPUT_DIR}")
    latest = load_latest()
    if latest:
        print(f"最新采集: {latest['collected_at']}, 共 {latest['total_evidence']} 条")
    else:
        print("暂无采集数据")
