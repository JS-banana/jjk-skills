---
name: readme-generator
description: >
  Generate high-quality README files for GitHub projects. Use this skill when
  the user mentions "README", "project documentation", "generate readme",
  "write readme", "readme template", or wants to create or improve their
  project's README file. This skill analyzes the project structure, identifies
  the project type, and generates a customized README with quality scoring.
  Trigger on: /readme-generator, "帮我写 README", "生成项目文档", "README 太烂了",
  "write project docs", "create readme".
---

# README Generator

## Overview

This skill generates high-quality, project-specific README files by:
1. Analyzing the project structure and tech stack
2. Selecting the appropriate template pattern
3. Generating content following best practices
4. Scoring the output quality
5. Presenting for user review before writing

## When to Use

**Trigger on:**
- User explicitly calls `/readme-generator`
- User says "帮我写 README" / "generate readme" / "write project docs"
- User wants to improve or rewrite existing README
- New project needs documentation

**Do NOT trigger when:**
- User wants to edit a small section of existing README
- User asks about API documentation only
- User is discussing README concepts without intent to generate

## Workflow

### Step 1: Project Analysis

Analyze the project to understand its characteristics. Read these files:
- `package.json` (if exists) - for dependencies, scripts, project metadata
- Existing `README.md` (if exists) - to understand current state
- Source code structure - to identify patterns

Determine:
1. **Project type**: CLI tool, library, web app, web service, mobile app, desktop app, monorepo, etc.
2. **Tech stack**: Language, framework, build tool, test framework
3. **Project scale**: Personal tool, team project, open source library

Use the analysis rules in `references/project-patterns.md`.

### Step 2: Select Template Pattern

**Content Pattern** (based on project type):

| Project Type | Pattern | Example |
|--------------|---------|---------|
| Mature library with docs site | Minimal Facade | React, Prettier |
| CLI tool | Complete Manual | bat |
| Framework | Standard Framework | Express |
| Personal/practical tool | Operation Manual | proxy_pool |

**Visual Style**: Always use **Brand-Focused** style (centered header with logo, title, description, and badges).

Read the selected content pattern and `assets/templates/brand-focused.md` for the visual style.

### Step 3: Generate README

Generate the README following these principles (from `references/writing-principles.md`):

**Visual Style (Brand-Focused):**
```html
<div align="center">
  <img src="./logo.svg" width="120" alt="Project Name" />  <!-- if logo exists -->
  <h1>Project Name</h1>
  <p><b>One-line description</b></p>
  [Badges]
</div>

<br/>
```

**Core Structure:**
1. Centered header (logo + title + description + badges)
2. Features / Key capabilities
3. Quick Start (3 steps or less)
4. Installation (detailed)
5. Usage examples (with code)
6. Configuration (if applicable)
7. Contributing
8. License

**Writing Rules:**
- 5-Second Rule: Reader must understand "what is this" in 5 seconds
- Value First: Show what it does before how to install
- Code is Documentation: Include at least one runnable example
- Assume Newbie: Write for someone who knows nothing about your project
- Progressive Depth: Simple → Advanced

**Language:**
- If project has Chinese content → generate Chinese README
- If project is English → generate English README
- Support bilingual with language switcher if requested

### Step 4: Quality Scoring

Score the generated README using the rubric in `references/scoring-rubric.md`.

**5 Dimensions (100 points total):**
- Content Completeness: 30 points
- Structure Organization: 20 points
- Visual Presentation: 15 points
- Readability & Language: 20 points
- Maintenance & Reliability: 15 points

**Grade Scale:**
- S (90-100): Excellent, can serve as template
- A (80-89): High quality, minor improvements possible
- B (70-79): Good, some dimensions need strengthening
- C (60-69): Acceptable, multiple improvements needed
- D (50-59): Deficient, significant rewrite needed
- F (<50): Inadequate, needs complete rewrite

Generate the score report in the format specified in `references/scoring-rubric.md`.

### Step 5: Preview & Confirm

Present to the user:
1. Generated README content (in a code block)
2. Quality score report
3. Improvement suggestions (if any)

**Wait for user confirmation** before writing to file.

If user requests changes:
- Regenerate the affected section
- Re-score if changes are significant
- Present updated version

## Output Format

### README File
Write to `README.md` in the project root.

### Score Report
Display in chat with the README preview.

### Bilingual Support
If bilingual requested:
- `README.md` - English version
- `README.zh-CN.md` - Chinese version
- Add language switcher badges at top

## Reference Files

Read these files as needed during execution:

- `references/project-patterns.md` - Project type identification rules
- `references/writing-principles.md` - Writing best practices
- `references/scoring-rubric.md` - Quality scoring criteria
- `references/README-anatomy.md` - README structure analysis
- `references/badge-catalog.md` - Common badges reference
- `assets/templates/brand-focused.md` - Default visual style (centered header)

## Examples

### Example 1: CLI Tool

User: "帮我给这个 CLI 工具写个 README"

1. Analyze: Check package.json for `bin` field, check src/ for CLI entry point
2. Pattern: Select "Complete Manual" content pattern
3. Style: Apply Brand-Focused visual style (centered header)
4. Generate: Include installation table, usage examples, configuration, troubleshooting
5. Score: Check for installation completeness, usage examples, cross-platform support

### Example 2: Library

User: "这个库需要一个 README"

1. Analyze: Check package.json for `main`/`exports`, check for API docs
2. Pattern: Select "Minimal Facade" if docs site exists, "Standard Framework" otherwise
3. Style: Apply Brand-Focused visual style (centered header)
4. Generate: Include API overview, quick start, examples, TypeScript support
5. Score: Check for API documentation, code examples, installation clarity

### Example 3: Personal Tool

User: "新项目，写个文档"

1. Analyze: Check project structure, identify practical use case
2. Pattern: Select "Operation Manual" content pattern
3. Style: Apply Brand-Focused visual style (centered header)
4. Generate: Focus on quick start, practical usage, minimal theory
5. Score: Check for clarity, actionability, Docker support

## Integration with Other Skills

This skill can work with:
- `dev-stats` - For generating stats cards in README
- `api-docs` - For linking to API documentation
- `changelog` - For version history references

## Notes

- Always respect existing README content if user wants to improve rather than replace
- For open source projects, include contributing guidelines
- For personal projects, keep it practical and concise
- When in doubt, ask the user about their preferences
