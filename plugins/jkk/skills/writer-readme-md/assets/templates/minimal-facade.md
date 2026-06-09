# Minimal Facade Pattern

## When to Use

- Mature project with dedicated documentation site
- Large user base (10k+ stars)
- README serves as entry point, not full documentation
- Project value is self-evident (like Prettier, React)

## Structure

```markdown
[Logo or Banner - optional]

# Project Name

[Badges - 4-6 max]

> One-line description: what + why

- **Feature 1**: Brief description
- **Feature 2**: Brief description
- **Feature 3**: Brief description

[Quick Start or Installation - minimal]

[Documentation link]

[Contributing - brief]

[License]
```

## Example: Prettier Style

```markdown
<p align="center">
  <img src="./banner.svg" alt="Project Banner" width="100%">
</p>

<h1 align="center">Project Name</h1>

<p align="center">
  Opinionated tool for doing something awesome
</p>

<p align="center">
  <a href="https://github.com/user/repo/actions">
    <img src="https://github.com/user/repo/actions/workflows/test.yml/badge.svg" alt="Tests">
  </a>
  <a href="https://www.npmjs.com/package/package">
    <img src="https://img.shields.io/npm/v/package.svg" alt="npm version">
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  </a>
</p>

---

## Features

- **Feature 1**: What it does and why it matters
- **Feature 2**: What it does and why it matters
- **Feature 3**: What it does and why it matters

## Quick Start

```bash
npm install package
```

```javascript
import { myFunction } from 'package';

const result = myFunction();
```

## Documentation

For full documentation, visit [docs.example.com](https://docs.example.com).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

[MIT](./LICENSE)
```

## Example: React Style

```markdown
# [React](https://react.dev/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![npm version](https://img.shields.io/npm/v/react.svg)](https://www.npmjs.com/package/react)
[![Build Status](https://github.com/facebook/react/actions/workflows/build.yml/badge.svg)](https://github.com/facebook/react/actions)

React is a JavaScript library for building user interfaces.

- **Declarative**: Design simple views for each state
- **Component-Based**: Build encapsulated components
- **Learn Once, Write Anywhere**: Use with any backend

## Installation

```bash
npm install react react-dom
```

## Quick Start

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  return <h1>Hello, World!</h1>;
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
```

## Documentation

- [Getting Started](https://react.dev/learn)
- [Tutorial](https://react.dev/learn/tutorial-tic-tac-toe)
- [API Reference](https://react.dev/reference)

## Contributing

Please read our [Contributing Guide](https://react.dev/contributing/).

## License

React is [MIT licensed](./LICENSE).
```

## Key Principles

1. **Brevity**: Under 100 lines total
2. **Visual Anchor**: Logo or banner at top
3. **Value Proposition**: 3 bullet points max
4. **Minimal Code**: One simple example
5. **Link Out**: Push details to docs site
6. **Clean Layout**: Lots of whitespace

## Checklist

- [ ] Logo or banner (optional)
- [ ] Title with link to docs (optional)
- [ ] 4-6 badges
- [ ] One-line description
- [ ] 3 feature bullets
- [ ] Quick start with code
- [ ] Documentation link
- [ ] Contributing link
- [ ] License
