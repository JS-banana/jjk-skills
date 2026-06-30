# Source Map

Use live backend availability, not hard-coded platform assumptions.

## First Command

```bash
agent-reach doctor --json
```

Use the active backend for Reddit, Xiaohongshu, Twitter/X, Bilibili, V2EX, RSS,
Exa, and web. If a backend is unavailable, switch source family instead of
pretending the platform is covered.

## Default Mix

For narrow runs, use at least three source families:

1. Mass-market lived pain: Xiaohongshu, Reddit, V2EX, Bilibili comments.
2. Explicit ask or dissatisfaction: Q&A, reviews, complaints, recommendation
   threads.
3. Money/workflow evidence: paid manual services, product reviews, procurement,
   tenders, industry forums.

For general or deep runs, add a fourth lane:

4. Third-party direction or scale: Product Hunt, app/store rankings, trend
   pages, package downloads, job posts, funding/product directories, and search
   volume proxies.

Include both Chinese and international sources unless the user narrows scope.
Do not compensate for weak quality by adding developer-only sources.

Choose acquisition modes from `acquisition-strategy.md` before writing queries.
Keyword search is auxiliary unless the run is explicitly a query-mining run.

## Operational Channel Matrix

Use this matrix to choose sources before running commands. "Primary evidence"
can produce accepted records after original reading. "Direction/scale" can only
prioritize topics or validate recurrence.

| Channel | Best role | Tool path | Default status |
| --- | --- | --- | --- |
| Reddit subreddit/search/read | Primary evidence, international depth | `opencli reddit subreddit/search/read -f yaml` | Default international source |
| V2EX API/RSS/node/replies | Primary evidence, Chinese tech/life/workflow | `curl` public API, `feedparser` RSS, Jina post read | Default Chinese stable source |
| Bilibili search/video/comments/subtitle | Primary evidence from Chinese video comments and creator workflows | `opencli bilibili search/video/comments/subtitle -f yaml` | Default Chinese mass-market source |
| Xiaohongshu note/comments/feed | Primary evidence for Chinese lifestyle scenes | `opencli xiaohongshu search/note/comments -f yaml` | High value but session-sensitive; fallback after repeated `[]` |
| App Store public app pages | Review evidence and category gaps | Jina Reader on `apps.apple.com` app pages; direct HTML parse if needed | Use page reviews; legacy RSS may return zero |
| Chrome Web Store extension pages | Review evidence for browser workflows | Jina Reader on full extension detail/reviews URL, Exa to find pages | Use when page is readable |
| Product Hunt topics/products/reviews/forums | Direction and lead source; some review evidence | Jina Reader on topic/product/review/forum pages | Direction by default; accept only concrete reviews/forums |
| YouTube search/subtitles/comments | Education demand and product-comparison comments | `yt-dlp` search/subtitle/comments | Secondary; comments are best evidence |
| Twitter/X search/feed/tweets | Speed, meta discussion, and switching language | `twitter search/tweet/feed` | Noisy; direction unless concrete actor/workflow |
| GitHub Issues/HN/Stack Overflow | Developer workflow pain | `gh search issues`, HN Algolia/Jina | Developer-only unless scoped |
| Procurement/tenders | Budgeted B-side workflow evidence | Exa search + Jina Reader on notices/PDFs | Strong B-side evidence |
| Paid service marketplaces | Money-backed manual workflows | Exa/Jina/manual browser for Fiverr, Upwork, Taobao, Xianyu, ZBJ | Strong if listing/order/review is readable |
| Job posts | Budgeted role/workflow signal | LinkedIn if configured; otherwise Exa/Jina job boards | Validation/direction unless task pain is explicit |
| Package/download metrics | Adoption and developer ecosystem scale | npm API, PyPIStats, GitHub stars/issues | Scale only |
| Trend/market data | Timing and category selection | Exploding Topics, Google Trends, reports, directories | Direction only |

## Source Families

| Family | Use for | Sources | Notes |
| --- | --- | --- | --- |
| Daily-life social | Mass-market lived pain | Xiaohongshu, Reddit, Bilibili comments | Best for lifestyle, health, travel, home, shopping, study, family |
| Idea communities | Direct "someone make this" leads | r/SomebodyMakeThis, r/AppIdeas, r/Startup_Ideas, Unvalidated Ideas, IdeasAI | Leads only; require original demand evidence before accepting |
| Question/recommendation | Explicit unsolved needs | V2EX, Reddit, Quora if readable, Zhihu if logged in | Reject generic recommendation without scene |
| Reviews/ratings | Existing product gaps | App Store, Google Play, Chrome Web Store, G2, Capterra, Trustpilot, AlternativeTo | Prefer 2-4 star reviews; 1-star is often product rage |
| Consumer complaints | Strong service pain | 黑猫投诉, public complaint boards | Treat as service/process pain, not always product opportunity |
| Paid manual services | Repetitive paid workflows | Fiverr, Upwork, 淘宝, 闲鱼, 猪八戒 | Search `代做`, `代整理`, `代填`, `代录入`, `代转写` |
| Business/procurement | Budgeted workflow needs | 中国政府采购网, public resource exchanges, industry forums | Strong for B-side; extract role, workflow, budget, requirement |
| Product/revenue directories | Validated products and gaps | Starter Story, Indie Hackers Products, MicroConf, Product Hunt, BetaList, 1000 Tools | Ask what people pay for and where gaps remain |
| Trend/VC | Direction and timing | Exploding Topics, Google Trends, Glimpse, YC RFS, a16z, NFX, First Round Review, industry reports | Direction only; never enough for an accepted record |
| Developer sources | Technical workflow pain | HN, GitHub Issues, Stack Overflow | Fallback unless user asks for developer products |
| Hiring/jobs | Budgeted operational work | LinkedIn, job boards, company career pages | Good for role/workflow discovery; not direct user pain alone |
| Usage/scale metrics | Adoption and recurrence proxy | npm, PyPIStats, GitHub stars/issues, app ratings, Chrome users | Scale only; pair with reviews or posts |

## Source Roles

| Role | What it can prove | Examples |
| --- | --- | --- |
| Direction | A category may be worth exploring | Trend reports, VC essays, Product Hunt, product directories |
| Lead | A possible pain exists | Idea communities, generic recommendation threads, broad search results |
| Evidence | A real actor has a job, obstacle, and current behavior | Original posts, reviews, complaints, comments, service listings |
| Validation | The pain repeats or money is involved | Multiple sources, 2-4 star reviews, paid services, procurement, order counts |
| Scale | A category or tool has adoption | Downloads, stars, ratings, rankings, traffic estimates |

Accepted records need evidence. Direction and lead sources must be followed by
original user/workflow evidence. Scale sources cannot create accepted records by
themselves.

## Language Scope

Do both Chinese and English unless the user narrows scope. The two languages are
not interchangeable:

- English Reddit/forum queries often work as full intent phrases, such as
  "what do you use to" or "alternative to", combined with a subreddit or scene.
- Chinese social/forum queries often combine scene words with tone markers such
  as `求推荐`, `太麻烦`, `平替`, `避坑`, or `手动整理`.
- Translation is for final Chinese row writing, not for query construction.
- Maintain hit/miss notes so the phrase list improves after each batch.

Use `acquisition-strategy.md` for native phrase families and non-keyword
channels.

## Deep Mining Categories

Pick 3-4 per deep run:

| Category | Inspect scenes | Evidence to prefer |
| --- | --- | --- |
| Health/Fitness | Habit adherence, sleep, ADHD, postpartum, rehab, chronic tracking, caregiver handoff | Long posts, app reviews, coaching/services, device complaints |
| Work/Productivity | Reminders, meetings, approvals, document handoff, team coordination, "chat plus spreadsheet" workflows | Workflow posts, 2-4 star SaaS reviews, tool-switching threads |
| Money/Finance | Subscriptions, budgeting, portfolio tracking, reimbursement, invoices, tax prep | Switching intent, paid apps, spreadsheet workarounds, finance forums |
| Learning/Education | Practice feedback, exam planning, language learning, parent-child study, credential prep | Study communities, app reviews, paid tutoring/service evidence |
| Jobs/Career | Resume, applications, interview prep, recruiting outreach, freelancer operations | Job-seeker threads, recruiter workflows, paid services, templates |
| Home/Life | Chores, cooking, pet care, storage, family schedules, errands | XHS/Bilibili comments, Reddit verticals, service listings |
| Travel/Housing | Trip planning, visas, rentals, home viewing, moving, local transport | Long complaint posts, review sites, agency/service evidence |
| Creative/Media | Writing, design, video editing, asset management, publishing, creator admin | Creator forums, software reviews, paid manual services |
| Business Workflow | Quotations, customer records, inspection reports, contracts, data entry, migrations | Procurement, service marketplaces, ops forums, repeated manual cost |
| AI/Automation | Tool cost, model migration, privacy, reliability, team governance, AI workflow handoff | Pricing complaints, workflow failures, local/offline asks, team usage posts |

## Stop Rules

- Stop after 30 inspected candidates or 8 strong accepted records by default.
- Switch source after two rounds of snippets, ads, product pages, or unreadable
  pages.
- Switch source if a platform returns empty results for three varied native
  queries; record this as source unreliability, not absent demand.
- For high-engagement posts, scan top 5-10 comments before accepting or
  rejecting.
- If all results are developer-only and scope is general, change source family.
