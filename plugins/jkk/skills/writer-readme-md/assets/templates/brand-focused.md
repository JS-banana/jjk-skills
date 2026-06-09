# Brand-Focused Pattern

## When to Use

- **Default pattern for all projects**
- Open source projects
- Personal projects (public or private)
- Projects with or without logo

## Structure

```html
<div align="center">
  [Logo - optional]
  <h1>Project Name</h1>
  <p><b>One-line description</b></p>
  [Badges]
</div>

<br/>

## Content sections (left-aligned)
```

## Example: With Logo

```html
<div align="center">
  <img src="./logo.svg" width="120" alt="Project Logo" />
  <h1>My Awesome Tool</h1>
  <p><b>A powerful CLI tool for processing data efficiently.</b></p>
  
  [![Tests](https://github.com/user/repo/actions/workflows/test.yml/badge.svg)](https://github.com/user/repo/actions)
  [![npm version](https://img.shields.io/npm/v/my-tool.svg)](https://www.npmjs.com/package/my-tool)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

<br/>

## Features

- **Feature 1**: Description
- **Feature 2**: Description
- **Feature 3**: Description

## Installation

```bash
npm install my-tool
```

## Usage

```bash
my-tool --input file.txt --output result.json
```

## License

[MIT](./LICENSE)
```

## Example: Without Logo

```html
<div align="center">
  <h1>🚀 My Awesome Tool</h1>
  <p><b>A powerful CLI tool for processing data efficiently.</b></p>
  
  [![Tests](https://github.com/user/repo/actions/workflows/test.yml/badge.svg)](https://github.com/user/repo/actions)
  [![npm version](https://img.shields.io/npm/v/my-tool.svg)](https://www.npmjs.com/package/my-tool)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

<br/>

## Features

...
```

## Design Specifications

### Logo

- **Size**: 120px width (recommended)
- **Format**: SVG (preferred), PNG
- **Position**: Above title
- **Alt text**: Project name

### Title

- **Tag**: `<h1>`
- **Content**: Project name
- **Optional**: Emoji prefix (🚀, 🔧, ⚡, etc.)

### Description

- **Tag**: `<p><b>...</b></p>`
- **Content**: One-line value proposition
- **Length**: Under 20 words
- **Style**: Bold for emphasis

### Badges

- **Position**: After description
- **Quantity**: 3-5 badges
- **Style**: flat-square (recommended)
- **Order**: CI → Version → License → Downloads

### Spacing

- **After centered block**: `<br/>` tag
- **Before first section**: Empty line

## Implementation

### Step 1: Check for Logo

```typescript
function findLogo(projectRoot: string): string | null {
  const logoNames = [
    'logo.svg', 'logo.png', 'logo.jpg',
    'icon.svg', 'icon.png', 'icon.jpg',
    'assets/logo.svg', 'assets/logo.png',
    'public/logo.svg', 'public/logo.png',
  ];
  
  for (const name of logoNames) {
    if (fs.existsSync(path.join(projectRoot, name))) {
      return name;
    }
  }
  
  return null;
}
```

### Step 2: Generate Header

```typescript
function generateHeader(project: ProjectAnalysis): string {
  const logoPath = findLogo(project.root);
  
  let header = '<div align="center">\n';
  
  // Logo (if exists)
  if (logoPath) {
    header += `  <img src="./${logoPath}" width="120" alt="${project.name}" />\n`;
  }
  
  // Title
  header += `  <h1>${project.name}</h1>\n`;
  
  // Description
  header += `  <p><b>${project.description}</b></p>\n`;
  
  // Badges
  header += '\n';
  header += generateBadges(project);
  
  header += '\n</div>\n\n<br/>\n';
  
  return header;
}
```

### Step 3: Generate Badges

```typescript
function generateBadges(project: ProjectAnalysis): string {
  const badges: string[] = [];
  
  // CI badge
  if (project.hasCI) {
    badges.push(`[![Tests](https://github.com/${project.owner}/${project.repo}/actions/workflows/test.yml/badge.svg)](https://github.com/${project.owner}/${project.repo}/actions)`);
  }
  
  // Version badge (if published)
  if (project.isPublished) {
    badges.push(`[![npm version](https://img.shields.io/npm/v/${project.packageName}.svg)](https://www.npmjs.com/package/${project.packageName})`);
  }
  
  // License badge
  if (project.license) {
    badges.push(`[![License: ${project.license}](https://img.shields.io/badge/License-${project.license}-yellow.svg)](./LICENSE)`);
  }
  
  return badges.join('\n');
}
```

## Complete Example

```markdown
<div align="center">
  <img src="./logo.svg" width="120" alt="Dev Stats" />
  <h1>Dev Stats</h1>
  <p><b>Archive your weekly WakaTime coding stats and generate beautiful SVG cards for GitHub README.</b></p>
  
  [![Tests](https://github.com/JS-banana/dev-stats/actions/workflows/update-wakatime.yml/badge.svg)](https://github.com/JS-banana/dev-stats/actions)
  [![Node.js](https://img.shields.io/badge/Node.js-%3E%3D22-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
  [![WakaTime](https://img.shields.io/badge/Powered%20by-WakaTime-orange?logo=wakatime&logoColor=white)](https://wakatime.com/)
</div>

<br/>

---

## ✨ Preview

| Light Mode | Dark Mode |
|:---:|:---:|
| ![Weekly coding stats](./assets/wakatime-language.svg) | ![Weekly coding stats dark](./assets/wakatime-language-dark.svg) |

---

## 🚀 Quick Start

Get your stats cards in 3 steps:

### 1. Fork this repo

Click the **Fork** button at the top right of this page.

...
```

## Key Principles

1. **Centered Header**: Logo + Title + Description + Badges
2. **Left-Aligned Body**: All content sections use standard Markdown
3. **Visual Hierarchy**: Header captures attention, body provides details
4. **Consistent Spacing**: Use `<br/>` after centered block
5. **Badge Style**: Use `flat-square` for consistent look

## Checklist

- [ ] Centered div wrapper
- [ ] Logo (if exists) - 120px width
- [ ] H1 title
- [ ] Bold description
- [ ] 3-5 badges
- [ ] `<br/>` after centered block
- [ ] Content sections left-aligned
- [ ] Consistent formatting
