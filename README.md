<div align="center">
  <h1>🍌 banana-skills</h1>
  <p><b>小帅的 AI 资产库：skills 插件 + prompts 沉淀</b></p>
</div>

## 🗂️ 仓库结构

| 目录 | 内容 |
|------|------|
| `plugins/banana/` | 可安装的 Claude Code 插件（技能见下方列表） |
| `prompts/` | 收藏的提示词与 AI 使用沉淀（[索引](prompts/README.md)） |
| `docs/` | 技能的 specs / ADR / 研究资料 |

## 📦 安装

```bash
# 安装全部技能
npx skills add JS-banana/banana-skills

# 或按需安装单个技能
npx skills add JS-banana/banana-skills --skill demand-radar
```

<details>
<summary>Claude Code 插件方式安装</summary>

```bash
/plugin marketplace add JS-banana/banana-skills
/plugin install banana
```

</details>

---

## ✨ 技能列表

| 技能 | 功能 |
|------|------|
| ai-vendor-campaign-radar | 发现、筛选、提醒并记录 AI/编程活动机会 |
| demand-radar | 采集、筛选、验证真实用户需求信号，并准备飞书多维表格记录 |
| r2-asset-publisher | 压缩图片、发布到 Cloudflare R2，并维护 Markdown 图床 URL 与资产台账 |
| writer-readme-md | 分析项目结构，生成高质量 README |
| writer-context-md | 创建和优化 AGENTS.md/CLAUDE.md |
