# Quality Scoring Rubric

## Scoring Dimensions

### 1. Content Completeness (30 points)

| Check Item | Points | Type | Criteria |
|------------|--------|------|----------|
| Project Title | 2 | Auto | H1 exists and is unique |
| Project Description | 5 | Auto+Manual | One-line description of what and why |
| Badges | 3 | Auto | shields.io or CI badges present |
| Installation Guide | 5 | Auto | Installation section exists with commands |
| Usage Examples | 5 | Auto+Manual | Usage section with code blocks |
| API Reference | 2 | Auto | API section exists (if applicable) |
| Configuration | 2 | Auto | Configuration/env vars documented |
| Contributing | 2 | Auto | Contributing section or link exists |
| License | 2 | Auto | License section or file exists |
| Changelog | 1 | Auto | Changelog section or link exists |
| FAQ | 1 | Auto | FAQ section exists (optional) |

**Auto-detection rules:**
```typescript
// Check if section exists (case-insensitive)
function hasSection(content: string, keywords: string[]): boolean {
  const headings = content.match(/^#{1,6}\s+.+$/gm) || [];
  return headings.some(h =>
    keywords.some(kw => h.toLowerCase().includes(kw.toLowerCase()))
  );
}

// Count code blocks
function countCodeBlocks(content: string): number {
  return (content.match(/```/g) || []).length / 2;
}

// Count badges
function countBadges(content: string): number {
  return (content.match(/!\[.*?\]\(https:\/\/img\.shields\.io|https:\/\/github\.com.*?\/actions\/workflows.*?badge/g) || []).length;
}
```

### 2. Structure Organization (20 points)

| Check Item | Points | Type | Criteria |
|------------|--------|------|----------|
| Heading Hierarchy | 4 | Auto | H1 unique; H2-H4 no level skipping |
| Table of Contents | 3 | Auto | TOC section or [toc] marker exists |
| Section Order | 3 | Manual | Recommended order: intro → install → usage → advanced → contributing → license |
| Content Grouping | 3 | Manual | Related content grouped in sections |
| Lists/Tables Usage | 3 | Auto | Uses lists and tables for structured info |
| Horizontal Rules | 2 | Auto | Uses `---` to separate sections |
| Details/Summary | 2 | Auto | Uses `<details>` for collapsible content |

**Auto-detection rules:**
```typescript
// Check heading hierarchy
function checkHeadingHierarchy(content: string): { valid: boolean; violations: number[] } {
  const headings = content.match(/^(#{1,6})\s+/gm) || [];
  const levels = headings.map(h => h.trim().length);
  let violations: number[] = [];
  for (let i = 1; i < levels.length; i++) {
    if (levels[i] - levels[i-1] > 1) {
      violations.push(i);
    }
  }
  return { valid: violations.length === 0, violations };
}

// Check for TOC
function hasTableOfContents(content: string): boolean {
  return /##\s*(Table of Contents|目录|TOC)/i.test(content) ||
         /\[toc\]/i.test(content) ||
         /\[\[TOC\]\]/i.test(content);
}
```

### 3. Visual Presentation (15 points)

| Check Item | Points | Type | Criteria |
|------------|--------|------|----------|
| Screenshots/Demo | 5 | Auto+Manual | Image references present; images clear and relevant |
| Code Block Languages | 3 | Auto | Code blocks specify language identifier |
| Tables Usage | 2 | Auto | Markdown tables used for structured info |
| Emoji Usage | 2 | Manual | Emoji used appropriately, not excessively |
| Layout Aesthetics | 3 | Manual | Visual hierarchy, spacing, alignment comfortable |

**Auto-detection rules:**
```typescript
// Check code block language identifiers
function checkCodeBlockLanguages(content: string): { total: number; withLang: number } {
  const blocks = content.match(/```(\w*)/g) || [];
  const withLang = blocks.filter(b => b.length > 3).length;
  return { total: blocks.length, withLang };
}

// Count images
function countImages(content: string): number {
  return (content.match(/!\[.*?\]\(.*?\)/g) || []).length;
}
```

### 4. Readability & Language Quality (20 points)

| Check Item | Points | Type | Criteria |
|------------|--------|------|----------|
| Language Conciseness | 5 | Auto+Manual | Avg sentence length ≤ 30 words (EN) / 40 chars (CN) |
| Terminology Consistency | 3 | Auto | Same terms used throughout |
| Active Voice | 3 | Auto | Active voice preferred over passive |
| Avoid Jargon | 2 | Manual | Technical terms explained or linked |
| Paragraph Length | 3 | Auto | Each paragraph ≤ 5 lines (rendered) |
| CJK Spacing | 2 | Auto | Spaces between Chinese and English text |
| Blank Line Usage | 2 | Auto | Sections separated by blank lines; no 3+ consecutive blank lines |

**Auto-detection rules:**
```typescript
// Check CJK spacing
function checkCJSpacing(content: string): { issues: number; total: number } {
  const noSpaceAfter = (content.match(/[一-鿿][a-zA-Z]/g) || []).length;
  const noSpaceBefore = (content.match(/[a-zA-Z][一-鿿]/g) || []).length;
  return { issues: noSpaceAfter + noSpaceBefore, total: noSpaceAfter + noSpaceBefore };
}

// Check consecutive blank lines
function countConsecutiveBlankLines(content: string): number {
  return (content.match(/\n{3,}/g) || []).length;
}
```

### 5. Maintenance & Reliability (15 points)

| Check Item | Points | Type | Criteria |
|------------|--------|------|----------|
| Link Validity | 5 | Auto | All relative and external links accessible |
| File Reference Validity | 3 | Auto | Referenced images/files exist (relative paths) |
| Version Info | 2 | Auto | Version number or last updated time present |
| Multilingual Support | 2 | Auto | Multilingual versions detected (README-xx.md) |
| Contact Info | 1 | Auto | Issue tracker, email, or other contact provided |
| Acknowledgments | 1 | Auto | Credits to dependencies or inspirations |
| Legal Compliance | 1 | Auto | LICENSE file exists and is reasonable |

**Auto-detection rules:**
```typescript
// Check relative path references
function checkRelativeRefs(content: string, basePath: string): { valid: string[]; broken: string[] } {
  const refs = content.match(/(?:!\[.*?\]\(|src="|srcset=")([^https?:][^)]+|[^https?:][^"]+)/g) || [];
  // Check if files exist
}

// Extract external links
function extractExternalLinks(content: string): string[] {
  return (content.match(/\]\((https?:\/\/[^)]+)\)/g) || [])
    .map(m => m.slice(2, -1));
}
```

## Grade Scale

| Grade | Score Range | Meaning | Indicator |
|-------|-------------|---------|-----------|
| S (卓越) | 90-100 | Excellent, can serve as template | 🏆 |
| A (优秀) | 80-89 | High quality, minor improvements | ⭐ |
| B (良好) | 70-79 | Good, some dimensions need work | ✅ |
| C (一般) | 60-69 | Acceptable, multiple improvements needed | ⚠️ |
| D (不足) | 50-59 | Deficient, significant rewrite needed | ❌ |
| F (不合格) | <50 | Inadequate, needs complete rewrite | 🚫 |

## Dimension Grades

Each dimension also has its own grade:

| Grade | Score Rate | Description |
|-------|------------|-------------|
| Excellent | ≥ 80% | Outstanding performance |
| Good | 60-79% | Meets standards |
| Fair | 40-59% | Needs improvement |
| Poor | < 40% | Needs significant work |

## Veto Rules

The following situations result in automatic D or F grade regardless of total score:

- Missing project title → F
- Missing project description → D
- Missing installation/usage instructions → D
- Broken links exceed 30% → D
- Security issues (exposed API keys) → F

## Score Report Format

```markdown
## 📊 README 质量评分

**总分: 85/100** ⭐⭐⭐⭐ (A - 优秀)

### 各维度得分

| 维度 | 得分 | 等级 | 状态 |
|------|------|------|------|
| 内容完整性 | 26/30 | 优秀 | ✅ |
| 结构组织 | 17/20 | 优秀 | ✅ |
| 视觉呈现 | 12/15 | 优秀 | ✅ |
| 可读性 | 16/20 | 优秀 | ✅ |
| 维护性 | 14/15 | 优秀 | ✅ |

### 通过项 (PASSED)

- ✅ H1 标题存在且唯一
- ✅ 检测到 4 个徽章
- ✅ 安装指南完整
- ✅ 使用示例丰富
- ✅ 代码块语言标识完整
- ✅ 中英文混排规范

### 改进建议 (SUGGESTIONS)

**中优先级:**
- 添加目录 (TOC) 导航
- 添加 Contributing 章节

**低优先级:**
- 添加 FAQ 章节
- 添加版本/更新时间信息

### 问题项 (ISSUES)

无

### 统计信息

- 自动检查项: 38
- 人工评估项: 12
- 一票否决项: 4 (全部通过)
- 字数: 1200
- 标题数: 8
- 代码块数: 6
- 图片数: 4
- 表格数: 2
- 链接数: 12
- 失效链接: 0
```

## Improvement Suggestions Format

Each suggestion should include:
- **Priority**: Critical > High > Medium > Low
- **Difficulty**: Low / Medium / High
- **Current State**: What exists now
- **Recommendation**: What to add/change
- **Example**: Before/after comparison

## Manual Evaluation Items

For items requiring human judgment:

| Item | Criteria | Scoring |
|------|----------|---------|
| Description Quality | One-line value proposition clear | 0-5 |
| Example Sufficiency | Covers main use cases | 0-5 |
| Screenshot Relevance | Images clearly show project | 0-5 |
| Layout Aesthetics | Visual hierarchy comfortable | 0-5 |
| Terminology Accuracy | Technical terms used correctly | 0-5 |
| Content Accuracy | Info matches actual code | 0-5 |
