# AI 活动雷达 — 飞书多维表格 API 参考

## 表格信息

- **app_token**: `MJpIbpWkSaLN0tsSQoTcn4QDnId`
- **table_id**: `tblYhMRh3fJ0FDfW`
- **表名**: AI 活动雷达
- **Wiki 链接**: `https://my.feishu.cn/wiki/Gouswxel0iP28FkwaNBcn6M9nHf`

## 字段清单（2026-06-21 更新）

| 字段名 | field_id | 类型 | ui_type |
|--------|----------|------|---------|
| 活动名称 | fldckS8l6L | 1 | Text (主字段) |
| 厂商 | fldi0Lx1cN | 3 | SingleSelect |
| 活动类型 | fldeW2TQVa | 3 | SingleSelect |
| 难度评级 | fldq1Obyd0 | 3 | SingleSelect |
| 难度说明 | fld7N8vbRU | 1 | Text |
| 奖励详情 | fldZNNNYWQ | 1 | Text |
| 活动形式 | fldJwBf5ZM | 1 | Text |
| 参与方式 | fldXCDNMhn | 1 | Text |
| 获奖条件 | fldPl7RN5s | 1 | Text |
| 时间节点备注 | fldxhvtEgx | 1 | Text |
| 推荐指数 | fldcnSQ6lC | 2 | Number (**不是单选！传整数 1-5**) |
| 建议 | fldPlBP5zC | 3 | SingleSelect |
| 状态 | fldjX8d8Yt | 3 | SingleSelect |
| 报名入口 | fldzeW2heY | 15 | Url |
| 活动详情链接 | fldBBEfUbK | 15 | Url |
| 官方确认 | fldr70feDB | 3 | SingleSelect |
| 我的备注 | fldk38mAgz | 1 | Text |
| 开始时间 | flde2OBDvy | 5 | DateTime |
| 截止时间 | flddFTRAyI | 5 | DateTime |
| 地区 | fldqoOZMo1 | 3 | SingleSelect |
| 奖励类型 | fldLRCyXCb | 4 | MultiSelect |
| 发现日期 | fld6xjKa7u | 5 | DateTime |
| 来源渠道 | fldUpwRnyl | 3 | SingleSelect |
| 预计投入 | fldNqmBwuT | 3 | SingleSelect |

## 视图清单

| 视图名 | view_id | 类型 | 配置方式 |
|--------|---------|------|---------|
| 全部活动 | vewDxfhDJC | grid | 默认，无筛选 |
| 即将截止 (7天内) | vewcJ0sSxl | grid | **API + 每日自动滚动**：截止时间 > Yesterday AND < ExactDate(today+8天零点)。由 cron `campaign-view-filter-roll` 每天 01:00 自动更新上界时间戳 |
| 高价值 (≥18) | vewABa0iZy | grid | 推荐指数 ≥ 18 (已通过 API 设置) |
| 按厂商 | vewscHmKWi | grid | 按厂商分组 (已通过 API 设置) |
| 看板 | vewSnxs3Un | kanban | 按状态分列 (已通过 API 设置) |
| 甘特图 | vewCbMJ7sD | gantt | 甘特视图 |

> 视图的 filter_info **可以通过 API 设置**（2026-06-23 实测验证）。关键格式要求见下方"视图筛选 API"小节。

## 单选字段选项值

### 厂商
EvoMap, 阿里云, 华为, Google, GitLab, Vercel, OpenAI, Anthropic, Microsoft, MiniMax, 智谱 AI, Moonshot, DeepSeek, 百度, Bitget, UiPath, AWS, 其他, Qoder Work, Qwen Cloud

### 活动类型
Hackathon, 开发者挑战赛, 开发者激励, AI竞赛, 内测体验, 福利发放, 内容创作, 其他

### 难度评级
⭐ 轻松领取, ⭐⭐ 简单参与, ⭐⭐⭐ 需花时间, ⭐⭐⭐⭐ 需技术能力, ⭐⭐⭐⭐⭐ 专业挑战

### 建议
立即行动, 值得做, 观望, 跳过

### 状态
新发现, 已报名, 进行中, 已完成, 已跳过, 已过期

### 官方确认
✅ 官方确认, ⚠️ 疑似, ❌ 非官方

### 地区
全球, 中国, 北美, 亚太, 欧洲, 其他

### 奖励类型 (多选)
现金, API Credits, 会员权益, 实物, 证书, 其他

### 来源渠道
Devpost, lablab.ai, DoraHacks, MLH, HackerEarth, Hack2Skill, Devfolio, X/Twitter, GitHub, 官网, linux.do, V2EX, Reddit, HuggingFace, 天池, 百度AI Studio, 讯飞, DataFountain, 即刻, 掘金, CSDN, InfoQ, 开源中国, 其他

### 预计投入
1小时内, 半天, 1-3天, 1周+, 长期投入

## API 操作速查

```python
# 获取 tenant token
token = fb.get_tenant_access_token(account_id='default', config_path='~/.openclaw/openclaw.json')

# 列出记录
records = fb.list_records(app_token, table_id, token=token)

# 创建/更新记录
fb.api_request(f'{base}/records', method='POST', token=token, payload={'fields': {...}})
fb.api_request(f'{base}/records/{rid}', method='PUT', token=token, payload={'fields': {...}})

# 改字段名 (必须带 type)
fb.api_request(f'{base}/fields/{fid}', method='PUT', token=token, payload={'field_name': '新名', 'type': 1})

# 改表名 (用 PATCH 不用 PUT)
url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}'
req = urllib.request.Request(url, data=json.dumps({"name":"新表名"}).encode(), method='PATCH', headers=...)
```python
# 视图筛选条件（2026-06-23 实测验证）
# 关键：filter_info 必须嵌套在 property 下；value 必须是字符串化 JSON 数组
# 日期字段只支持 isGreater/isLess（不支持 isGreaterEqual/isLessEqual）
view_url = f'{base}/views/{view_id}'

# 示例：设置"7天内截止"的动态范围
import json
filter_body = {
    "property": {
        "filter_info": {
            "conjunction": "and",
            "conditions": [
                {"field_id": "flddFTRAyI", "field_type": 5,
                 "operator": "isGreater",
                 "value": json.dumps(["Yesterday"])},       # 相对日期：≥ 今天
                {"field_id": "flddFTRAyI", "field_type": 5,
                 "operator": "isLess",
                 "value": json.dumps(["ExactDate", upper_ms])}  # < 7天后
            ]
        }
    }
}
req = urllib.request.Request(view_url, data=json.dumps(filter_body).encode(),
    method='PATCH', headers=headers)
# 验证：GET /views/{view_id} → data.view.property.filter_info.conditions
```

## 同步脚本

- 路径: `~/.hermes/scripts/campaign_bitable_sync.py`
- 模式: `--write` (单条写入), `--dry` (预览), 无参数 (批量同步 JSONL)
- 去重文件: `~/.hermes/scripts/vendor_campaign_seen.jsonl`
- **写入契约和默认值定义在 SKILL.md「写入契约（唯一入口）」section**，脚本是契约的执行实现

## ⚠️ 日期字段格式要求（关键）

飞书多维表格的日期字段（类型 5 = DateTime）**只接受毫秒时间戳整数**，不接受日期字符串。

`campaign_bitable_sync.py --write` 的 override 路径**不做日期转换**，直接透传 JSON 中的值。因此：

- `截止时间`、`发现日期`、`开始时间` 必须传整数毫秒时间戳
- 传 `"2026-07-13"` 字符串会报 `DatetimeFieldConvFail`

## ⚠️ 日期字段视图筛选运算符限制（2026-06-23 实测踩坑）

日期字段（type=5）在视图筛选中**不支持 `isGreaterEqual` / `isLessEqual`**：

- ❌ `isGreaterEqual` → 400 `operator type is unsupported`
- ❌ `isLessEqual` → 400 `operator type is unsupported`
- ✅ `isGreater` → 严格大于
- ✅ `isLess` → 严格小于

**实现"大于等于"的变通**：用相对日期关键词 `Yesterday`/`Today`/`Tomorrow` 偏移。

| 想实现 | 正确写法 |
|--------|---------|
| 截止时间 ≥ 今天 | `"operator": "isGreater", "value": "[\"Yesterday\"]"` |
| 截止时间 ≤ N天后 | `"operator": "isLess", "value": "[\"ExactDate\", {N+1天0点UTC毫秒}]"` |
| 截止时间 > 今天 | `"operator": "isGreater", "value": "[\"Today\"]"` |
| 截止时间 < 今天 | `"operator": "isLess", "value": "[\"Today\"]"` |

**相对日期关键词**：`Today`、`Yesterday`、`Tomorrow`。不支持 `NextWeek`/`N days later`。

## ⚠️ 动态日期范围需要每日滚动更新（2026-06-23 实测确认）

飞书视图筛选不支持"未来 N 天"这种动态表达。要实现"7天内截止"的效果：

1. 计算 `today+8` 天 00:00:00 UTC+8 的毫秒时间戳（+8 而非 +7，因为用 `isLess` 严格小于）
2. PATCH 视图更新 `filter_info.conditions[1].value = ["ExactDate", upper_ms]`
3. **每天执行一次**，由 cron job 自动完成

已部署脚本：`~/.hermes/scripts/update_campaign_view_filter.py`
已部署 cron：`campaign-view-filter-roll`（每天 01:00，no_agent，成功静默/失败报警）

### 脚本关键逻辑
```python
now_beijing = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
today = now_beijing.replace(hour=0, minute=0, second=0, microsecond=0)
upper = today + datetime.timedelta(days=8)  # +8天的00:00 = +7天全天的上界
upper_utc = upper - datetime.timedelta(hours=8)
upper_ms = int(upper_utc.timestamp() * 1000)
```

### 创建类似的维护 cron
```bash
# no_agent script-only cron: 零 token 消耗，成功静默，失败报警
hermes cron create --name "xxx-maintenance" --schedule "0 1 * * *" \
  --script "xxx_script.py" --no-agent
```

## ⚠️ 多选字段格式要求（关键，2026-06-23 实测验证）

多选字段（类型 4 = MultiSelect，如 `奖励类型`）**必须传 JSON 数组**，不能传字符串。

- ❌ `"奖励类型": "现金,证书"` → 报 `MultiSelectFieldConvFail`
- ❌ `"奖励类型": "现金"` → 报 `MultiSelectFieldConvFail`
- ✅ `"奖励类型": ["现金", "证书"]` → 正确
- ✅ `"奖励类型": ["现金"]` → 正确（单个值也要用数组）

可选值：现金, API Credits, 会员权益, 实物, 证书, 其他

## ⚠️ 推荐指数字段类型（2026-06-23 实测验证）

`推荐指数` (field_id: fldcnSQ6lC) 的 Bitable 实际类型是 **Number (type=2)**，不是 SingleSelect。
虽然 UI 显示为 ⭐~⭐⭐⭐⭐⭐ 星级，但写入时**必须传整数 1-5**，传字符串会报类型错误。

**转换方法（Python one-liner）：**
```bash
# 示例：2026-07-13 17:00 PDT → 毫秒时间戳
python3 -c "from datetime import datetime, timezone, timedelta; dt = datetime(2026,7,13,17,0,0,tzinfo=timezone(timedelta(hours=-7))); print(int(dt.timestamp()*1000))"
# 输出: 1783987200000

# 示例：2026-06-21 CST → 毫秒时间戳
python3 -c "from datetime import datetime, timezone, timedelta; dt = datetime(2026,6,21,0,0,0,tzinfo=timezone(timedelta(hours=8))); print(int(dt.timestamp()*1000))"
# 输出: 1781971200000
```
