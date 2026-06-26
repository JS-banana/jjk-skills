#!/usr/bin/env python3
"""
Demand Radar v2 - Cron任务配置
每天自动采集和处理需求数据
"""

# Cron任务prompt
CRON_PROMPT = """执行 Demand Radar v2 需求证据采集任务：

## 采集任务

### 1. 英文平台
- Reddit: r/LifeProTips, r/productivity, r/personalfinance, r/SideProject, r/SaaS
- Quora: 搜索 productivity tool, efficiency app
- AlternativeTo: 热门替代品

### 2. 中文平台
- 知乎: 求推荐、效率工具、好用的APP
- 少数派: 效率工具、工作流
- 什么值得买: 求推荐、好用

### 3. 开发者平台
- GitHub Issues: Cline, aider, Continue, OpenHands, Dify, n8n
- Stack Overflow: productivity, automation tags
- Hacker News: Top Stories

## 处理流程

1. 采集原始数据（每平台5-10条）
2. AI判断需求真实性（过滤广告、闲聊、情绪表达）
3. AI判断需求强度（强/中/弱）
4. AI提取一句话痛点
5. AI分类需求方向
6. AI判断产品形态
7. 计算优先级（P0/P1/P2/P3）
8. 写入飞书表格

## 飞书表格配置

- Base Token: Yuo3bJSBXaBI7AsOKMEcFLCknye
- Table ID: tblKLTYTOUOyL3FR

## 字段映射

- 标题、一句话痛点、需求方向、产品形态
- 需求强度、需求普遍性、可解决性、匹配度
- 优先级、状态、评分理由
- 原文内容、原始链接、来源平台、语言

## 输出统计

本次采集：各平台采集数量、写入数量、高优先级需求（P0/P1）列表
"""

# Cron任务配置
CRON_CONFIG = {
    "name": "Demand Radar v2 需求采集",
    "schedule": "0 9 * * *",  # 每天9:00执行
    "prompt": CRON_PROMPT,
    "skills": ["lark-base"],
    "enabled": True
}

if __name__ == "__main__":
    print("Cron任务配置：")
    print(f"名称: {CRON_CONFIG['name']}")
    print(f"执行时间: {CRON_CONFIG['schedule']}")
    print(f"技能: {CRON_CONFIG['skills']}")
