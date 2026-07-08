# AI 活动雷达 — 飞书表字段增补建议

> 状态：**建议稿，未实施**。确认后再改表；改表后需同步更新
> `plugins/jkk/skills/ai-vendor-campaign-radar/references/bitable-api-patterns.md`
> 和 `scripts/campaign_bitable_sync.py` 的字段默认值。
>
> 背景：表 `tblYhMRh3fJ0FDfW` 现有 22 字段；网站（panion-works/ai-hackathons）
> 的 `mapper.ts` 只读取已知字段名，**新增字段对网站零影响**；但修改现有字段的
> select 选项需同步网站 `enums.ts` 的归一化映射。

## 建议新增字段（5 个，均对网站安全）

| 字段 | 类型 | 为什么需要 | 写入方改动 |
|------|------|-----------|-----------|
| `来源链接` | 文本（URL） | 现有 `来源渠道` 是 select，只知道"来自哪类渠道"，丢失了发现时的原始 URL。有了它：① 跨源去重时可比对域名；② 复核/纠错时能一键回到出处；③ 能统计哪个源产出最多独家活动（registry 的"信源质量追踪"闭环目前无数据支撑） | sync 脚本加一个直通字段；skill 步骤 5 传 `source_url` |
| `奖池金额` | 数字（USD 归一） | `奖励详情` 是纯文本无法排序/筛选。Devpost JSON API 直接给 `prize_amount`，CompeteHub 也带奖金数字，采集成本≈0。网站将来可按奖池排序、做"高奖金"筛选 | sync 脚本加字段；非现金奖励留空 |
| `提交截止时间` | 日期 | 现有 `截止时间` 语义混杂（报名截止 vs 提交截止），AgentDeadlines 的 `endDate` 模糊问题（agentdeadlines-guide.md）本质就是缺这个字段。约定：`截止时间`=报名/参与截止，`提交截止时间`=作品提交截止，未知则留空 | skill 步骤 3/5 区分两个日期 |
| `城市` | 文本 | `地区` 粒度只到大区（全球/中国/北美…），对国内线下活动不够用。活动行/aihot/CompeteHub 都带城市数据。文本而非 select：城市长尾太长，select 会失控 | sync 脚本加字段；线上活动留空 |
| `最后核验时间` | 日期 | 提醒场景（deadline reminder 模式）目前只能信任写入时的状态。有了它，提醒前先看核验新鲜度：超过 N 天未核验的先复核官方页面再通知，避免用过期状态打扰 | skill 步骤 3 的 reminder 分支在复核后回写此字段 |

## 现有字段清理建议

**`难度评级` 有历史重复选项**（bitable-api-patterns.md 已记录此债务）。清理步骤：

1. `lark-cli base +field-list` 导出当前全部选项，确认重复项清单。
2. 批量更新存量记录：把重复选项的记录改到 5 个规范星级选项上。
3. 删除多余选项。
4. 网站影响检查：`enums.ts` 对难度是按星号/数字解析的，规范化后解析只会更稳，无需改网站。

## 明确不建议加的字段

- `活动详情链接`：历史上已确认不存在此字段（传了会 FieldNameNotFound），`报名入口` + 新增 `来源链接` 已覆盖需求，不要再引入第三个 URL 字段。
- `去重键`：去重是采集侧逻辑（seen JSONL + 脚本内 vendor|campaign 键），物化到表里只会产生同步负担。

## 实施顺序（确认后）

1. 飞书表加 5 个字段（皆为可空，存量记录不受影响）。
2. 更新 `bitable-api-patterns.md` 字段契约表（22 → 27 字段）。
3. 更新 `campaign_bitable_sync.py` 的 `jsonl_record_to_bitable_fields` 与 `OVERRIDE_FIELDS`。
4. 跑 `scripts/verify_bitable_fields.py` 确认契约一致。
5. 网站侧（可选、另做）：`mapper.ts`/`model.ts` 消费 `奖池金额`（排序）与 `城市`（展示）。
