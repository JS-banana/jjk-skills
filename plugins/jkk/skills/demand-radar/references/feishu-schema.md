# Feishu Schema

Feishu is only the output store. Use the current `lark-cli` auth/config/session
state. Do not store Base tokens, table IDs, cookies, or app credentials in this
skill.

## Fields

Write these fields only:

| Field | Type | Rule |
| --- | --- | --- |
| 标题 | text | Short demand title, not the original noisy post title |
| 一句话痛点 | text | One sentence that captures the user's pain; ≤ 80 字 |
| 社区反响 | text | Likes/comments/replies/ratings/orders/budget, e.g. `35赞，104评论` |
| 需求方向 | select | 效率工具 / 生活好物 / 学习成长 / 健康管理 / 财务理财 / 旅行出行 / 育儿教育 / 社交娱乐 / 工作方法 / 创作工具 / 开发者工具 / 其他 |
| 产品形态 | select | 手机App / 微信小程序 / 网站/Web应用 / 桌面应用 / 浏览器插件 / 硬件产品 / 实体商品 / 服务 / 内容产品 / API/SDK / 其他 |
| 需求强度 | select | 强 / 中 / 弱 |
| 需求普遍性 | select | 高 / 中 / 低 |
| 优先级 | select | Derived by `scripts/run.py` |
| 处理状态 | select | 待评估 / 有价值 / 无价值 / 待观察；新行默认 `待评估`（其余为人工分诊状态） |
| 原文内容 | text | Natural Chinese rendering of the original evidence; ≥ 40 字（证明读过原文），超 5000 字截断 |
| 原始链接 | URL | Specific URL |
| 来源平台 | select | Must match a current Base option; the Base select may be narrower than the sources you mine — add the platform or use `其他` if missing |
| 语言 | select | 中文 / 英文 / 双语 |

## Priority

```text
score = 需求强度(强=3, 中=2, 弱=1) * 需求普遍性(高=3, 中=2, 低=1)
>= 9 + P0证据 => P0-立即行动
>= 9 without P0证据 => P1-重点考虑
6-8   => P1-重点考虑
3-5   => P2-观察中
< 3   => P3-待观察
```

`P0证据` is input-only and is not written to Feishu.

## Prepare JSON

```bash
python3 scripts/run.py \
  --input /tmp/demand-radar-rows.json \
  --output /tmp/demand-radar-feishu.json \
  --report /tmp/demand-radar-report.json
```

Input may be a JSON array or an object with `records`, `rows`, or `signals`.

## Write

Check auth/config first:

```bash
lark-cli config show
```

Find `BASE_TOKEN` and `TABLE_ID` from the user's lark-cli/session state, previous
run command history, or explicit user-provided values. Do not add stable tokens
to this skill.

Reconcile select options against the live Base before writing (the option values
documented above are a snapshot and can drift from the Base):

```bash
lark-cli base +field-list --base-token "$BASE_TOKEN" --table-id "$TABLE_ID" --as user
```

Confirm every 来源平台 / 需求方向 / 产品形态 / 处理状态 / 需求强度 / 需求普遍性 / 语言
value in your rows exists in the field's current options. If a source platform is
missing (e.g. App Store, Bilibili), add it once with `+field-update` (send the full
options list — update is PUT, not patch) or map it to `其他`.

Batch write usually needs `@./relative-path` from the file directory:

```bash
cd /tmp && lark-cli base +record-batch-create \
  --base-token "$BASE_TOKEN" \
  --table-id "$TABLE_ID" \
  --json @./demand-radar-feishu.json \
  --as user
```

## lark-cli Gotchas

- `+field-update` takes `options` at the top level (not under `property`) and is a
  full PUT: include all existing options plus the new one, or the rest are deleted.
- `+record-batch-create` consumes `run.py`'s `{fields, rows}` output directly.
- `+record-get` prints markdown by default and takes one `--record-id` (no comma lists).
- Add `--dry-run` to preview any write request before executing.

## Verify

- Confirm created count equals accepted row count.
- Spot-check at least 3 records, or all records if fewer than 3.
- Check that `原始链接` opens the exact source and `原文内容` matches the original
  evidence.
