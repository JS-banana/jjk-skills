# AI 活动雷达 — 信源注册表

> 基于 2026-06-27 实测验证，所有信源均已通过可达性测试。
> 分层策略：Tier A（每日必扫）→ Tier B（每周深扫）→ Tier C（按需/用户转发时查）
> 最近更新：2026-06-30（新增 V2EX "AI赛事通"月度聚合帖模式、DDG 非 site: 查询返回过期活动网站陷阱、cron 模式 JSONL 更新完整工作流）

---

## Tier A：每日必扫（每次巡检都要覆盖）

### 🏗️ 直接聚合平台（核心信源，信号密度最高）

| ID | 平台 | URL | 搜索方式 | 提取方式 | 数据质量 | 备注 |
|----|------|-----|---------|---------|---------|------|
| `agentdeadlines` | AgentDeadlines | agentdeadlines.com | `web_extract("https://agentdeadlines.com")` | web_extract ✅ + **curl 直连 ✅**（含 JSON-LD 结构化数据） | ⭐⭐⭐⭐⭐ | **AI Agent 专属 deadline 聚合器**（31+ 活动），单页含奖金/截止/格式/赞助商。2026-06-21 实测：一次提取发现 KDD Cup $885K + RAISE €250K + ARC Prize $2M + AWS AI League $50K。**降级模式**：curl 直连获取 198KB HTML，解析 `<script type="application/ld+json">` 获得全部 31 条结构化事件数据（name/startDate/endDate/url/description），无需 web_extract。详见 SKILL.md "搜索降级策略"。**⚠️ 过期过滤**：31 项中约 1/3 已过期，先按 endDate < today 排除再提取详情。|
| `devpost` | Devpost | devpost.com/hackathons | `site:devpost.com AI hackathon 2026` | web_extract ✅ | ⭐⭐⭐⭐⭐ | 全球最大 hackathon 平台，含奖金/截止/参赛人数/标签 |
| `lablab` | lablab.ai | lablab.ai/ai-hackathons | `site:lablab.ai AI hackathon 2026` | web_extract ✅ / curl ❌ Cloudflare JS 挑战（2026-06-26 确认） | ⭐⭐⭐⭐⭐ | AI 专属平台，信号纯净，有 LIVE/Register/Coming Soon 状态。**降级模式**：DDG `site:lablab.ai` 查询结果含活动名+截止日期+描述，信息密度足够做初筛。确认为 Cloudflare JS 挑战页后不再尝试 curl 直连 |
| `dorahacks` | DoraHacks | dorahacks.io | `site:dorahacks.io AI hackathon 2026` | web_extract ✅（newsletter页） | ⭐⭐⭐⭐ | AI+Web3，`/blog/news/dora-hackathons` 是结构化表格 |
| `tianchi` | 天池（阿里云） | tianchi.aliyun.com/competition | `site:tianchi.aliyun.com 2026 大赛 OR competition` | web_extract ✅ | ⭐⭐⭐⭐⭐ | 国内最结构化的竞赛平台，含标签/奖金/队伍数。**⚠️ `/specials/` 路径为 JS 渲染壳**，curl 仅返回导航文字。用 DDG 搜索获取摘要，或 Firecrawl 提取 |
| `aistudio` | 百度 AI Studio | aistudio.baidu.com | `site:aistudio.baidu.com competition 2026` | web_extract ❌（JS SPA） | ⭐⭐⭐⭐ | 搜索可达，详情页需 Firecrawl JS 渲染 |
| `xfyun` | 讯飞开发者大赛 | challenge.xfyun.cn | `site:challenge.xfyun.cn 2026` | web_extract ❌（反爬） | ⭐⭐⭐⭐ | 搜索可达，提取被拦截，用 Firecrawl stealth |
| `dataagent` | KDD Cup Data Agents | dataagent.top | web_search ✅ / DDG ✅ | ❌ JS SPA (React) | ⭐⭐⭐⭐⭐ | KDD Cup 2026 第二赛道（HKUST 主办），不同于 algo.qq.com 的 Tencent UNI-REC。React SPA 无法 curl 提取，需 DDG 搜索获取摘要 |

### 🌐 社区/社交信号（最早发现渠道，v3 恢复）

| ID | 平台 | 搜索方式 | 数据质量 | 备注 |
|----|------|---------|---------|------|
| `linuxdo` | linux.do | `site:linux.do AI credits OR 福利 OR 活动 OR 赠金 OR 大赛 OR hackathon` | ⭐⭐⭐⭐⭐ | 中文开发者福利/羊毛/credits 第一信号源，v2.0 实测极佳。**降级模式**：搜索 API 被 CF 拦截，但 `curl linux.do/t/topic/ID.json` 可直接获取帖子内容（Discourse JSON API），配合 DDG `site:linux.do` 搜索发现 topic ID |
| `v2ex` | V2EX | `site:v2ex.com AI credits hackathon 2026` | ⭐⭐⭐⭐ | 开发者 credits 讨论/赠金，v2.0 实测高。**⚠️ DDG 查询必须用英文关键词**（2026-06-27 实测：`site:v2ex.com AI credits hackathon 2026` 返回 10 条；含中文关键词如"赠金/福利"则返回 0 条）。**🆕 "AI赛事通"(CompeteHub) 月度聚合帖**（2026-06-30 实测）：V2EX 用户 `wuswoo` 每月发布中国区 AI 竞赛汇总（如 `t/1206299` 覆盖 112 场），含竞赛名/奖金/地点/起止日期/类型标签。内容比 DDG 搜索更全面、更结构化。发现路径：DDG `site:v2ex.com AI赛事通 竞赛 汇总 2026`。掘金上同源用户也发布类似汇总 |
| `twitter_auth` | Twitter/X（认证） | `twitter search "AI hackathon prize 2026" --type latest` | ⭐⭐⭐⭐⭐ | 已配置 cookies，twitter-cli 直连，实时信号最强。**⚠️ 401（cookie过期）和 404（ClientTransaction init failure）两种故障模式**，详见 SKILL.md Pitfalls |
| `x_hackathon` | X/Twitter（搜索） | `site:x.com "AI hackathon" OR "agent hackathon" OR "developer challenge" 2026` | ⭐⭐⭐⭐ | web_search 补充，能发现非平台活动 |
| `x_submissions` | X/Twitter（报名） | `site:x.com submissions open OR registration open AI agent prize 2026` | ⭐⭐⭐⭐ | 发现即将截止和刚开放的活动 |
| `hf_community` | HuggingFace | `site:huggingface.co hackathon OR competition AI 2026` | ⭐⭐⭐⭐ | ML 社区专属活动（Mistral Hack-a-ton、LeRobot 等）。**⚠️ HF org 页面可能显示已结束活动**：如 Agents-MCP-Hackathon（2025-06）仍出现在 DDG 搜索结果中。curl 提取 HF org 页面时需检查日期（`📅 Date:` 字段），避免将旧活动误判为当前活动。建议在 DDG 查询中加 `2026` 过滤 |
| `reddit_hackathon` | Reddit | `site:reddit.com r/hackathon OR r/AgentsOfAI AI hackathon 2026` | ⭐⭐⭐⭐ | 社区草根活动，很多不在主流平台出现 |

### 📢 通用发现查询（广撒网，捕获漏网之鱼）

| ID | 查询 | 语言 | 数据质量 | 备注 |
|----|------|------|---------|------|
| `broad_en` | `"AI hackathon" OR "agent hackathon" OR "developer challenge" prize deadline 2026` | EN | ⭐⭐⭐⭐⭐ | 单次最高 ROI 查询，捕获 MIT/Google Cloud/小众活动 |
| `broad_en_simple` | `AI hackathon developer challenge 2026 prize register` | EN | ⭐⭐⭐⭐ | **新发现（2026-06-27）**：平铺关键词无 OR 无 site: 的简单查询，DDG 可靠性最高（10/10 命中）。推荐作为 broad_en 的首选查询模式 |
| `broad_zh` | `"AI 大赛" OR "智能体大赛" OR "编程马拉松" OR "开发者挑战赛" 报名 2026` | ZH | ⭐⭐⭐⭐ | 国内生态全覆盖（DJI/天池/讯飞/华为） |
| `wechat_proxy` | `微信公众号 AI 大赛 OR hackathon OR 开发者挑战赛 OR 黑客松 报名 2026` | ZH | ⭐⭐⭐ | 公众号内容通过搜狗/搜索引擎间接覆盖 |
| `google_alerts` | `AI hackathon OR competition cash prize submissions open 2026 -site:facebook.com -site:instagram.com` | EN | ⭐⭐⭐⭐⭐ | Google Alerts 等效广撒网查询 |

---

## Tier B：每周深扫（周三 + 周日各选一半覆盖）

### 🏗️ 补充聚合平台（GPT 推荐全量覆盖）

| ID | 平台 | 搜索方式 | 提取方式 | 数据质量 | 备注 |
|----|------|---------|---------|---------|------|
| `mlh` | MLH | `site:mlh.io hackathon AI 2026` | web_extract ✅（/seasons/2026/events） | ⭐⭐⭐⭐ | 学生/校园为主，有 Global Hack Week: Agents |
| `hackerearth` | HackerEarth | `site:hackerearth.com AI hackathon 2026` | web_extract ❌ | ⭐⭐⭐ | 企业/招聘型活动多，搜索可达 |
| `hack2skill` | Hack2Skill | `site:hack2skill.com AI hackathon 2026` | web_extract ❌ / **curl ❌ 全站 JS SPA**（2026-06-27 确认所有子页面） | ⭐⭐⭐ | 印度/企业活动，ISRO/Google/Intel 合作。**⚠️ 全站 React SPA**：hack2skill.com 和 vision.hack2skill.com 所有页面 curl 返回 9KB 空壳。只能通过 DDG 搜索获取摘要（snippet 含活动名/截止日期/描述）|
| `devfolio` | Devfolio | `site:devfolio.co AI hackathon 2026` | web_extract ❌ | ⭐⭐⭐ | 印度学生为主，$250K+ 奖池活动 |
| `kaggle` | Kaggle | `site:kaggle.com competitions AI 2026` | web_search | ⭐⭐⭐⭐ | AI/ML 竞赛平台，偏算法/数据赛 |
| `aicrowd` | AIcrowd | `site:aicrowd.com AI challenge 2026` | web_search | ⭐⭐⭐ | AI 竞赛平台，ML 挑战赛 |
| `angelhack` | AngelHack | `site:angelhack.com hackathon AI 2026` | web_search | ⭐⭐⭐ | 全球 hackathon 运营商 |
| `unstop` | Unstop | `site:unstop.com AI hackathon 2026` | web_search | ⭐⭐⭐ | 印度/亚太挑战赛平台，Google/AWS 企业活动常在此发布 |
| `datafountain` | DataFountain | `site:datafountain.cn 2026 大赛` | web_extract ✅ | ⭐⭐⭐ | 国内数据竞赛平台 |
| `eventbrite` | Eventbrite | `site:eventbrite.com AI hackathon 2026` | web_search | ⭐⭐ | 线下活动多，线上有限 |
| `meetup` | Meetup | `site:meetup.com AI hackathon developer 2026` | web_search | ⭐⭐ | 本地社区活动，信号密度低 |
| `hackernoon_hackathons` | HackerNoon Hackathons | `hackernoon.com/technology-hackathons` curl ✅ | curl 直连 | ⭐⭐⭐ | **新发现（2026-06-27）**：活跃 hackathon 列表页（含 Decentralize AI Hackathon $51K+），可 curl 获取 HTML。信息含赞助商/奖金/参赛机制。适合 Tier B 深扫 |
| `ethglobal_events` | ETHGlobal Events | `ethglobal.com/events` curl ⚠️ | curl 直连 ⚠️ | ⭐⭐⭐ | **新发现（2026-06-27）**：结构化活动列表含日期/地点/类型（IRL/Online），curl 可获取所有未来 hackathon。Web3+AI 交叉领域，往届奖金池 $275K+。**⚠️ URL 复用问题（2026-06-27 实测）**：ethglobal.com/events/{slug} 返回旧年份活动数据（如 `/events/lisbon` 显示 2023 年活动）。需通过 DDG 搜索或 AgentDeadlines 确认最新年份。适合 Tier B 深扫 |

### 🌐 中文社区（GPT 推荐全量覆盖）

| ID | 平台 | 搜索方式 | 数据质量 | 备注 |
|----|------|---------|---------|------|
| `juejin` | 掘金 | `site:juejin.cn AI大赛 OR hackathon OR 创造力大赛 OR "AI赛事通" 2026` | ⭐⭐⭐⭐ | "AI赛事通" 月度聚合帖很有价值（单帖列出 112 场大赛） |
| `csdn` | CSDN | `site:csdn.net AI大赛 OR 开发者大赛 OR hackathon 2026` | ⭐⭐⭐ | 大赛报道和聚合帖 |
| `infoq_cn` | InfoQ 中国 | `site:infoq.cn AI大赛 OR hackathon 2026` | ⭐⭐⭐⭐ | 深度报道，含技术细节 |
| `oschina` | 开源中国 | `site:oschina.net hackathon OR 大赛 2026` | ⭐⭐⭐ | 开源/量子/AIGC 活动 |
| `jiqizhixin` | 机器之心 | `site:jiqizhixin.com AI大赛 OR hackathon OR 竞赛 2026` | ⭐⭐⭐ | AI 行业媒体报道 |
| `qbitai` | 量子位 | `site:qbitai.com AI大赛 OR hackathon OR 竞赛 2026` | ⭐⭐⭐ | AI 行业媒体报道 |
| `sfchina` | SegmentFault | `site:segmentfault.com AI hackathon OR 大赛 2026` | ⭐⭐ | 中文开发者社区 |

### 🏭 厂商活动页（GPT 推荐全量 watchlist，轮换覆盖）

| ID | 厂商 | 搜索方式 | 备注 |
|----|------|---------|------|
| `google_dev` | Google Developers | `site:developers.google.com events OR hackathon Gemini 2026` | Build with AI / Gemini API Sprints |
| `slack_dev` | Slack Developers | `site:slack.dev challenge OR hackathon 2026` | Agent Builder Challenge（$42K） |
| `anthropic` | Anthropic | `site:anthropic.com hackathon OR competition OR beta program 2026` | Fellows / events page |
| `microsoft` | Microsoft | `site:microsoft.com developer challenge OR hackathon AI 2026` | Build / Azure AI |
| `aws` | AWS | `site:aws.amazon.com developer challenge OR hackathon 2026` | AWS Activate / Hackathon |
| `nvidia` | NVIDIA | `site:nvidia.com developer challenge OR hackathon AI 2026` | GTC / developer programs |
| `huawei` | 华为 | `site:developer.huawei.com 活动 OR 大赛 OR 激励 OR 鸿蒙 2026` | 天工计划/鸿蒙激励 |
| `aliyun` | 阿里云 | `site:developer.aliyun.com 活动 OR 大赛 2026` | 天池/AI 创新大赛 |
| `bytedance` | 字节/Trae | `Trae OR 豆包 AI大赛 OR 创造力大赛 OR hackathon 2026` | Trae 创造力大赛 |
| `baidu` | 百度飞桨 | `site:aistudio.baidu.com OR site:paddlepaddle.org.cn 大赛 2026` | 飞桨开发者大赛 |
| `tencent` | 腾讯云 | `site:cloud.tencent.com 开发者 OR 大赛 2026` | 腾讯云开发者活动 |
| `volcengine` | 火山引擎 | `site:volcengine.com 开发者 OR 活动 OR 大赛 2026` | 火山引擎开发者社区 |
| `openai` | OpenAI | `site:openai.com hackathon OR beta program OR developer 2026` | — |
| `vercel` | Vercel | `site:vercel.com hackathon OR challenge 2026` | v0 / Next.js 生态 |
| `cloudflare` | Cloudflare | `site:developers.cloudflare.com challenge 2026` | 实测无信号，低优先级 |
| `github` | GitHub Blog | `site:github.blog hackathon OR developer program 2026` | — |
| `modelscope` | 魔搭 | `site:modelscope.cn 活动 OR 大赛 2026` | ModelScope 社区 |
| `zhipu` | 智谱 | `site:zhipuai.cn OR 智谱 GLM 活动 OR 大赛 OR 内测 2026` | — |
| `deepseek` | DeepSeek | `DeepSeek 活动 OR 开发者 OR credits 2026` | — |
| `minimax` | MiniMax | `MiniMax 海螺 活动 OR credits OR 内测 2026` | — |
| `moonshot` | Moonshot/Kimi | `Kimi 月之暗面 活动 OR 内测 OR 福利 2026` | — |
| `hf_events` | HuggingFace Events | `site:huggingface.co/events` | 直接活动页面 |
| `aitinkerers` | AI Tinkerers | `site:aitinkerers.org event 2026` | 全球 AI 社区 meetup |
| `gdg` | GDG Community | `site:gdg.community.dev events 2026` | Google Developer Groups |

---

## Tier C：按需/发现后深入

| ID | 平台 | 搜索方式 | 备注 |
|----|------|---------|------|
| `gitee` | Gitee | `site:gitee.com 大赛 2026` | 竞赛代码仓库，非发现平台 |
| `jiqizhixin` | 机器之心 | `site:jiqizhixin.com AI大赛 2026` | 大型赛事报道 |
| `cloudflare` | Cloudflare | `site:developers.cloudflare.com hackathon` | ❌ 实测无信号，降级 |
| `producthunt` | Product Hunt | `site:producthunt.com AI free credits` | 偏产品上线，非活动聚合 |
| `hackmap` | hackmap.io | DDG 搜索命中具体事件 URL 时 curl 提取 | ⚠️ 主页为纯 JS 交互地图，HTML 不含事件数据。2026-06-26 实测确认不可作为独立扫描源，仅在已有具体事件 URL 时辅助提取 |
| `info_ms` | Microsoft Events | `site:info.microsoft.com hackathon 2026` | 2026-06-26 DDG broad_en 发现 Agents League Hackathon（$55K）。厂商注册页模式，可在 Tier B 厂商活动扫描中覆盖 |
| `ainave` | ainave.com | `site:ainave.com hackathon 2026` / DDG broad 搜索命中 | 日本/亚太 DeepTech 活动聚合器，2026-06-26 DDG 广撒网发现。信号质量 ⭐⭐⭐，偏日语/亚太市场，部分活动面向特定区域创始人。适合作为 broad_en 查询的附带命中源 |
| `decentralizeai` | DecentralizeAI.tech | DDG broad 搜索命中 | HackerNoon 旗下 Decentralize AI Hackathon 主站（2026-06-27 发现），Web3+AI 基础设施方向。可通过 hackernoon.com/technology-hackathons 发现 |

---

## 扫描时间预算分配

### 每日巡检（5 分钟，12-15 次工具调用）

| 步骤 | 调用次数 | 来源 |
|------|---------|------|
| 读取 seen 记录 | 1 | 本地 |
| Tier A 聚合平台搜索 | 3-4 | devpost + lablab + tianchi + (dorahacks OR xfyun 轮换) |
| Tier A 社区信号搜索 | 2 | x_hackathon + (hf_community OR reddit 轮换) |
| Tier A 通用发现查询 | 1 | broad_en OR broad_zh 轮换 |
| 提取详情页 | 2-3 | 候选活动的详情页 |
| 写入 seen 记录 | 1 | 本地 |
| **合计** | **12-15** | |

### 每周深扫（周日额外执行，8-10 分钟）

| 步骤 | 说明 |
|------|------|
| Tier B 聚合平台 | mlh + hackerearth + hack2skill + devfolio + datafountain |
| Tier B 中文社区 | juejin + csdn + infoq_cn |
| Tier B 厂商活动页 | 每次选 2-3 个厂商（轮换覆盖） |
| 已报名活动截止提醒 | 检查 seen 中状态为"已报名"的活动截止时间 |

---

## 信源质量追踪

发现新活动时，记录"首次出现源"。如果某个源持续产出独家信号，提升其优先级；如果某源连续 10 次巡检无新信号，降级或移除。

**反馈闭环**：每次"知道晚了"的活动 → 反推最早出现的源 → 加入注册表。
