# Writing Principles & Best Practices

## Core Principles

### 1. 5-Second Rule
Reader must understand "what is this" and "what can I do with it" within 5 seconds.

**How to achieve:**
- Logo/Banner at top
- One-line description immediately after title
- Code example in first screen
- Clear value proposition

**Good:**
```markdown
# WakaTime CLI
> Track your coding time automatically - no manual timers needed.

![Demo](./demo.gif)
```

**Bad:**
```markdown
# MyTool
A tool for processing data using Node.js with various features.
```

### 2. Value First, Details Later
Show what it does before how to install.

**Order:**
1. What it does (Features)
2. How it looks (Screenshots/Demo)
3. How to install (Installation)
4. How to use (Usage)
5. How to configure (Configuration)

### 3. Code is Documentation
Include at least one runnable code example.

**Good:**
```markdown
## Quick Start

```bash
npm install my-tool
my-tool --input file.txt --output result.json
```

Output:
```json
{
  "processed": 42,
  "time": "0.3s"
}
```
```

**Bad:**
```markdown
## Usage
See the documentation for usage instructions.
```

### 4. Assume Newbie
Write for someone who knows nothing about your project.

**Good:**
```markdown
### Prerequisites
- Node.js >= 18.0.0 ([download](https://nodejs.org/))
- npm >= 9.0.0 (comes with Node.js)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/user/project.git
   cd project
   ```

2. Install dependencies:
   ```bash
   npm install
   ```
```

**Bad:**
```markdown
### Installation
npm install
```

### 5. Progressive Depth
Simple → Advanced, let users choose their entry point.

**Structure:**
- Quick Start (5 minutes)
- Basic Usage (15 minutes)
- Advanced Configuration (30 minutes)
- API Reference (as needed)

### 6. Too Long is Better Than Too Short
If README feels too long, split into separate docs rather than cutting information.

**Strategy:**
- README: Entry point, essential info only
- docs/: Detailed documentation
- CONTRIBUTING.md: Contribution guidelines
- CHANGELOG.md: Version history

### 7. Use Markdown Formatting
Structure content with headings, lists, code blocks, tables.

**Elements to use:**
- `#` headings for sections
- `-` or `*` for bullet lists
- `1.` for numbered steps
- `` ``` `` for code blocks
- `| |` for tables
- `>` for blockquotes
- `**bold**` for emphasis

### 8. Visual Hierarchy
Use visual elements to guide the reader's eye.

**Order:**
1. Logo/Banner (visual anchor)
2. Title + badges (identification)
3. Description (understanding)
4. Features (value proposition)
5. Code example (proof)
6. Installation (action)

### 9. Consistent Terminology
Use the same terms throughout the document.

**Good:**
- Always "CLI" not sometimes "command line" sometimes "CLI"
- Always "configuration" not sometimes "config" sometimes "settings"

**Bad:**
- Mix "install", "setup", "get started" interchangeably

### 10. Active Voice
Use active voice instead of passive voice.

**Good:**
```markdown
Run the following command to install the package.
```

**Bad:**
```markdown
The package can be installed by running the following command.
```

### 11. Concrete Over Abstract
Use specific examples instead of abstract descriptions.

**Good:**
```markdown
## Features

- **Syntax Highlighting**: Supports 200+ languages including JavaScript, Python, Rust
- **Git Integration**: Shows file changes inline with +/- indicators
- **Auto Paging**: Automatically pipes output to less/more
```

**Bad:**
```markdown
## Features

- Supports many languages
- Works with Git
- Has paging support
```

### 12. Show, Don't Tell
Demonstrate with examples instead of describing.

**Good:**
```markdown
## Before & After

**Before (unformatted):**
```javascript
const foo={a:1,b:2,c:3}
```

**After (prettified):**
```javascript
const foo = { a: 1, b: 2, c: 3 };
```
```

**Bad:**
```markdown
Prettier formats your code automatically.
```

### 13. Link Liberally
Provide links to related resources.

**Where to add links:**
- Dependencies and tools mentioned
- Documentation sections
- Related projects
- External resources

### 14. Keep Paragraphs Short
Each paragraph should focus on one idea.

**Good:**
```markdown
## Installation

Install via npm:

```bash
npm install my-tool
```

Or via yarn:

```bash
yarn add my-tool
```
```

**Bad:**
```markdown
## Installation

You can install this tool using npm or yarn. First, make sure you have Node.js installed. Then run the install command. If you prefer yarn, you can use yarn add instead. Both methods will install the package and its dependencies.
```

### 15. Regular Updates
Keep README in sync with code changes.

**When to update:**
- New features added
- Installation process changed
- Dependencies updated
- Breaking changes introduced

## Common Mistakes

### Fatal Mistakes (Users Will Leave)

1. **No README or empty README**
   - Most fatal mistake
   - Users won't investigate further

2. **Vague description**
   - "A tool for processing data" tells nothing
   - Be specific about what it does and why it matters

3. **No installation instructions**
   - Users don't know how to start
   - They'll move to a project that explains this

4. **Assuming tech stack knowledge**
   - Not everyone knows your framework
   - Explain prerequisites clearly

5. **Missing license**
   - Without license, code is "all rights reserved"
   - Open source projects must include license

### Readability Mistakes

6. **Large blocks of unformatted text**
   - No headings, lists, or code blocks
   - Wall of text is intimidating

7. **Not using Markdown**
   - Plain text looks terrible on GitHub
   - Use Markdown for formatting

8. **No table of contents**
   - Long README without navigation
   - Users get lost

9. **Non-copyable code examples**
   - Examples that need modification to work
   - Users should be able to copy-paste directly

10. **Outdated information**
    - Installation commands that don't work
    - Immediately destroys trust

### Content Mistakes

11. **Only technical description, no value proposition**
    - "Built with React" vs "Saves 50% development time"
    - Focus on benefits, not features

12. **No visual demonstration**
    - No screenshots, GIFs, or demos
    - Users can't see what they're getting

13. **No help channel**
    - Users don't know where to ask questions
    - Provide Issues, Discussions, or email

14. **Vague contribution guidelines**
    - "Contributions welcome" is not a guide
    - Explain the process

15. **README out of sync with code**
    - Documented features don't exist
    - Existing features not documented

## Audience-Specific Strategies

### For Beginners

- Use plain language, explain jargon
- Provide complete environment setup steps
- Include "Hello World" level examples
- Link to tutorials, not API docs
- Explain common errors and solutions
- Provide specific help channels (Discord, Stack Overflow tags)

### For Experienced Developers

- State technical architecture upfront
- Provide design decision rationale
- Show performance benchmarks
- Link to complete API reference
- Explain extension/customization methods
- Show integration with other tools

### For Contributors

- Explain contribution flow step by step: fork → branch → commit → PR
- List development environment setup
- Explain code style and linting rules
- Explain how to run tests
- Mark "good first issue" items
- Explain commit message format

### For End Users

- Focus on "what it does for me", not technical implementation
- Provide lots of screenshots and GIFs
- Use scenario-based language
- Provide FAQ section
- Explain how to uninstall or opt out

## Bilingual README Best Practices

### File Organization

```
README.md          # English (GitHub default display)
README.zh-CN.md    # Simplified Chinese
README.zh-TW.md    # Traditional Chinese (if needed)
```

### Language Switcher

Add at top of README:

```markdown
[![中文](https://img.shields.io/badge/-%E4%B8%AD%E6%96%87-blue)](./README.zh-CN.md)
[![English](https://img.shields.io/badge/English-blue)](./README.md)
```

### Writing Order

1. Write in one language first
2. Translate to the other
3. Don't machine translate without review

### Content Consistency

- Both versions should have identical structure
- Same section order
- Same code examples
- Each version should be self-contained

### Chinese-Specific Considerations

- Technical terms keep English (API, SDK, CLI)
- Use Chinese punctuation in Chinese text
- Use English punctuation in code
- Add spaces between Chinese and English text
- Chinese readers expect more visual elements

### English-Specific Considerations

- Write for global audience
- Use standard technical terminology
- Avoid culture-specific references
- English README is GitHub's default display language
- English README is primary for search indexing
