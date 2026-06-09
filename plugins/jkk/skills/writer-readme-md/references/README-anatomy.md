# README Anatomy

## Universal Sections (All Projects Need)

| Section | Purpose | Priority |
|---------|---------|----------|
| **Title** | Project identification | Critical |
| **Description** | What + Why in one sentence | Critical |
| **Installation** | How to get started | Critical |
| **Usage** | How to use it | Critical |
| **License** | Legal terms | Critical |

## Common Sections (Most Projects Need)

| Section | Purpose | When to Include |
|---------|---------|-----------------|
| **Badges** | Project status at a glance | Open source projects |
| **Features** | Key capabilities | Projects with multiple features |
| **Quick Start** | 5-minute setup | All projects |
| **Configuration** | Customization options | Configurable projects |
| **Contributing** | How to help | Open source projects |
| **Examples** | Real-world usage | Libraries, tools |

## Optional Sections (Project-Specific)

| Section | Purpose | Best For |
|---------|---------|----------|
| **Table of Contents** | Navigation for long README | Long documents (>100 lines) |
| **Screenshots/Demo** | Visual proof | UI projects, tools |
| **API Reference** | Detailed API docs | Libraries, SDKs |
| **Architecture** | System design | Complex projects |
| **Troubleshooting** | Common issues | Tools with known issues |
| **FAQ** | Anticipated questions | Popular projects |
| **Roadmap** | Future plans | Active projects |
| **Changelog** | Version history | Published packages |
| **Acknowledgments** | Credits | Projects with dependencies |
| **Team** | Maintainers | Large projects |

## Section Ordering Patterns

### Pattern A: Minimal Facade (React, Prettier)

```
Logo/Banner
Title + Badges
One-line description
3 Bullet Points (value props)
Installation (brief)
Documentation (link)
Contributing
License
```

**Best for:** Mature projects with docs site, large user base

### Pattern B: Complete Manual (bat)

```
Title + Description
Features
Usage (detailed)
Installation (table)
Customization
Configuration
Troubleshooting
Development
Maintainers
License
```

**Best for:** CLI tools, tools needing detailed usage

### Pattern C: Standard Framework (Express)

```
Logo
Title + Description
Badges
Code Example
Installation
Features
Documentation & Community
Quick Start
Philosophy
Examples
Contributing
Team
License
```

**Best for:** Frameworks, libraries with design philosophy

### Pattern D: Operation Manual (proxy_pool)

```
Title + Logo
Badges
Description
Quick Start
Installation (multiple methods)
Usage (API table)
Extension Guide
Contributing
License
```

**Best for:** Personal tools, practical utilities

## Section Details

### Title

**Rules:**
- H1 heading, unique
- Keep concise (2-6 words)
- Can include emoji for personality
- Can link to project website

**Good:**
```markdown
# bat - a cat clone with wings
# [React](https://react.dev/)
# 🚀 My Awesome Tool
```

**Bad:**
```markdown
# My Project Version 2.0 (Final) (1)
# README
```

### Description

**Rules:**
- One sentence, under 20 words
- Answer "what" and "why"
- Use blockquote (`>`) for visibility
- Avoid jargon

**Good:**
```markdown
> A cat clone with syntax highlighting and Git integration.
> Archive your weekly WakaTime stats and generate SVG cards.
```

**Bad:**
```markdown
> A tool for processing data using Node.js with various features.
> This project is a comprehensive solution for modern development workflows.
```

### Badges

**Rules:**
- Place after title
- Maximum 6-8 badges
- Use consistent style
- Link to relevant pages

**Recommended badges:**
1. CI/CD status
2. Code coverage
3. Version (npm/PyPI)
4. License
5. Downloads

### Features

**Rules:**
- Use bullet points
- One feature per point
- Benefit-focused, not feature-focused
- Use bold for feature name

**Good:**
```markdown
## Features

- **Syntax Highlighting**: Supports 200+ languages
- **Git Integration**: Shows changes inline
- **Auto Paging**: Pipes to less/more automatically
```

**Bad:**
```markdown
## Features

- Syntax highlighting
- Git integration
- Paging
```

### Installation

**Rules:**
- Numbered steps
- Copy-paste commands
- Prerequisites listed first
- Multiple methods if applicable

**Good:**
```markdown
## Installation

### Prerequisites
- Node.js >= 18.0.0
- npm >= 9.0.0

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/user/repo.git
   cd repo
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Verify installation:
   ```bash
   npm test
   ```
```

### Usage

**Rules:**
- Start with simplest example
- Show expected output
- Use real scenarios
- Link to detailed docs

**Good:**
```markdown
## Quick Start

```bash
my-tool --input file.txt --output result.json
```

Output:
```json
{
  "processed": 42,
  "time": "0.3s"
}
```

For more examples, see [documentation](./docs/usage.md).
```

### Configuration

**Rules:**
- Use table for options
- Include defaults
- Show examples
- Group by category

**Good:**
```markdown
## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--input` | string | required | Input file path |
| `--output` | string | `result.json` | Output file path |
| `--verbose` | boolean | `false` | Enable verbose logging |
```

### Contributing

**Rules:**
- Link to CONTRIBUTING.md if detailed
- Include basic steps inline
- Mention code style
- Link to issues

**Good:**
```markdown
## Contributing

Contributions are welcome! Please read our [Contributing Guide](./CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request
```

### License

**Rules:**
- Link to LICENSE file
- State license type
- Place at end

**Good:**
```markdown
## License

[MIT](./LICENSE)
```

## Visual Elements

### Images

**Rules:**
- Use relative paths
- Add alt text
- Keep file sizes reasonable
- Consider dark/light mode

**Good:**
```markdown
![Project Screenshot](./docs/screenshot.png)
![Demo GIF](./docs/demo.gif)
```

### Tables

**Rules:**
- Align columns
- Use for structured data
- Keep readable

**Good:**
```markdown
| Feature | Free | Pro |
|---------|------|-----|
| Users | 10 | Unlimited |
| Storage | 1GB | 100GB |
```

### Code Blocks

**Rules:**
- Specify language
- Use fenced blocks (```)
- Keep examples runnable
- Show output separately

**Good:**
```markdown
```javascript
const result = await myFunction();
console.log(result);
```

Output:
```
{ success: true }
```
```

### Details/Summary

**Rules:**
- Use for optional content
- Keep summary short
- Don't nest too deep

**Good:**
```markdown
<details>
<summary>Advanced Configuration</summary>

Detailed configuration options here...

</details>
```

## Common Anti-Patterns

### 1. Wall of Text
**Problem:** No headings, lists, or code blocks
**Fix:** Break into sections, use formatting

### 2. Missing Context
**Problem:** Assumes reader knows everything
**Fix:** Add prerequisites, explain terms

### 3. Outdated Information
**Problem:** Commands that don't work
**Fix:** Regular updates, test instructions

### 4. Too Short
**Problem:** "Install: npm install"
**Fix:** Add steps, verification, troubleshooting

### 5. Too Long
**Problem:** README is 1000+ lines
**Fix:** Move details to docs/, keep README as entry point

### 6. No Examples
**Problem:** Only describes, never shows
**Fix:** Add code examples, screenshots

### 7. Broken Links
**Problem:** Links to non-existent files
**Fix:** Use relative paths, verify links

### 8. Inconsistent Style
**Problem:** Mix of formatting styles
**Fix:** Use consistent headings, lists, code blocks
