# README 排版元素实证调研（2026-07）

为 `writer-readme-md` 的 `references/presentation.md` 提供实证依据。抓取 20 个
知名仓库的 README 原文（gh api，2026-07-09），用脚本统计排版元素使用频率。

## 样本

facebook/react、vuejs/core、vercel/next.js、shadcn-ui/ui、ant-design/ant-design、
fastapi/fastapi、BurntSushi/ripgrep、sharkdp/bat、oven-sh/bun、vitejs/vite、
supabase/supabase、excalidraw/excalidraw、lobehub/lobe-chat、
langchain-ai/langchain、ollama/ollama、n8n-io/n8n、AppFlowy-IO/AppFlowy、
chalk/chalk、expressjs/express、langgenius/dify

选样覆盖：极简风（ripgrep、chalk、react、shadcn）、中等修饰（fastapi、vite、
supabase）、重装修社区产品（lobe-chat、dify、AppFlowy）、中文双语（ant-design）。

## 元素使用频率（n=20）

| 元素 | 数量 | 备注 |
|---|---:|---|
| 居中头部（`align="center"`） | 15 | 主流 |
| Logo 图 | 12 | 全部为既有品牌资产（仓库内文件或官网 CDN），无一临时生成 |
| shields.io 徽章 | 15 | 多数 ≤8 个；dify 26 个、lobe-chat 32 个属另一流派 |
| 导航链接行（`·` 分隔） | 7 | |
| 深浅色 `<picture>` | 7 | |
| Sponsors 区 | 6 | |
| hero 截图/GIF | 6 | |
| 语言切换行 | 4 | ant-design / dify / lobe-chat / bat，均在标题区 |
| emoji 标题 | 2 | ant-design、lobe-chat，且均为全部章节统一使用 |
| contrib.rocks 贡献者墙 | 3 | |
| star history 图 | 2 | 仅 dify、lobe-chat；置于底部社区区 |
| GitHub Alerts | 2 | |
| `<details>` 折叠 | 3 | |
| repobeats | 0 | |

## 关键结论（已落入 skill）

1. **两种正当风格，不可混搭半套**：工程克制风（主流、默认，0-5 徽章）vs
   社区产品风（徽章墙 `<br/>` 分组 + star history + 贡献者墙 + 多语言 + 全章节
   emoji，整套采用）。shadcn/ui 全文 17 行、一张 hero 图，证明克制是高星项目
   的主流姿态。
2. **Logo 只用既有资产**：仓库文件 → 官网 CDN → org 头像；没有就用朴素 H1，
   生成 logo 需用户确认且产物入库（如 `docs/assets/logo.svg`），不外链。
3. **star history 是"增长叙事"组件**：只适合公开且确有社区诉求的仓库，放底部
   社区区，`<picture>` 深色适配，区块长时用 `<details>` 折叠（lobe-chat 写法）。
4. 徽章密集的 README 依赖引用式链接定义（`[![][shield]][link]` + 文末定义）
   保持源码可维护；长文加 `<a name="readme-top">` 回顶锚点。

## 复现

原始 README 存于会话 scratchpad（临时），统计脚本为一次性 Python 正则计数：
按 `centered_header / logo / badges / star-history / contrib.rocks /
prefers-color-scheme / alerts / details / lang-switcher / emoji-headings /
sponsors` 等模式逐文件匹配。如需刷新，用 `gh api repos/{owner}/{repo}/readme
-H "Accept: application/vnd.github.raw"` 重抓即可。
