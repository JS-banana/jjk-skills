# Standard Framework Pattern

## When to Use

- Frameworks and libraries
- Projects with design philosophy
- Projects with governance structure
- Need to show maturity and professionalism

## Structure

```markdown
[Logo]

# Project Name
**One-line description**

[Badges]

[Code Example]

## Installation
## Features
## Documentation
## Quick Start
## Philosophy
## Examples
## Contributing
## Team
## License
```

## Example: Express Style

```markdown
<p align="center">
  <img src="https://i.cloudup.com/zfY6lL7eFa-3000x3000.png" alt="Express" width="200">
</p>

<p align="center">
  <strong>Fast, unopinionated, minimalist web framework for Node.js</strong>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/express">
    <img src="https://img.shields.io/npm/v/express.svg" alt="npm version">
  </a>
  <a href="https://www.npmjs.com/package/express">
    <img src="https://img.shields.io/npm/dm/express.svg" alt="npm downloads">
  </a>
  <a href="https://github.com/expressjs/express/actions">
    <img src="https://github.com/expressjs/express/actions/workflows/ci.yml/badge.svg" alt="CI">
  </a>
  <a href="https://codecov.io/gh/expressjs/express">
    <img src="https://img.shields.io/codecov/c/github/expressjs/express.svg" alt="Coverage">
  </a>
</p>

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});
```

## Installation

```bash
npm install express
```

**Requirements:** Node.js 18+

## Features

- Robust routing
- Focus on high performance
- Super-high test coverage
- HTTP helpers (redirection, caching, etc.)
- View system supporting 14+ template engines
- Content negotiation
- Executable for generating applications quickly

## Documentation

- [Official Website](https://expressjs.com/)
- [GitHub Organization](https://github.com/expressjs)
- [Discussions](https://github.com/expressjs/express/discussions)

### Migrating from v4 to v5

See [Migration Guide](https://expressjs.com/en/guide/migrating-5.html).

## Quick Start

### Using express-generator

```bash
npx express-generator myapp
cd myapp
npm install
npm start
```

### Manual Setup

```bash
mkdir myapp
cd myapp
npm init -y
npm install express
```

Create `index.js`:

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
```

Run:

```bash
node index.js
```

## Philosophy

The Express philosophy is to provide small, robust tooling for HTTP servers, making it a great solution for single page applications, web sites, hybrids, or public HTTP APIs.

Express provides a thin layer of fundamental web application features, without obscuring Node.js features that you know and love.

## Examples

View the [examples](https://github.com/expressjs/express/tree/master/examples) directory for more:

```bash
git clone https://github.com/expressjs/express.git
cd express
npm install
node examples/hello-world/index.js
```

## Contributing

See [Contributing Guide](./CONTRIBUTING.md).

### Security Issues

Report security issues to [security@expressjs.com](mailto:security@expressjs.com).

### Running Tests

```bash
npm test
```

## Current Project Team Members

### Technical Committee (TC)

- [@dougwilson](https://github.com/dougwilson) - Douglas Wilson
- [@hacksparrow](https://github.com/hacksparrow) - Hage Yaapa
- [@jonathanong](https://github.com/jonathanong) - jongleberry
- [@LinusU](https://github.com/LinusU) - Linus Unnebäck
- [@niftylettuce](https://github.com/niftylettuce) - niftylettuce
- [@troygoode](https://github.com/troygoode) - Troy Goode

### Triagers

- [@aravindvnair99](https://github.com/aravindvnair99) - Aravind Nair
- [@carpasse](https://github.com/carpasse) - Carlos Pastor
- [@crandmck](https://github.com/crandmck) - Rand McKinney
- [@davidmashe](https://github.com/davidmashe) - David Ashe
- [@ghinks](https://github.com/ghinks) - Glenn
- [@javoire](https://github.com/javoire) - Yevgen Safronov
- [@lpinca](https://github.com/lpinca) - Luigi Pinca
- [@maxakuru](https://github.com/maxakuru) - Max Edell
- [@mjbaldwin](https://github.com/mjbaldwin) - Michael Baldwin
- [@wesleytodd](https://github.com/wesleytodd) - Wes Todd

### Emeritus

<details>
<summary>Previous team members</summary>

- [@defunctzombie](https://github.com/defunctzombie) - Roman Shtylman
- [@Fishrock123](https://github.com/Fishrock123) - Jeremiah Senkpiel
- [@hueniverse](https://github.com/hueniverse) - Eran Hammer
- [@tj](https://github.com/tj) - TJ Holowaychuk

</details>

## License

[MIT](./LICENSE)
```

## Key Principles

1. **Professional Presentation**: Logo, centered layout, comprehensive badges
2. **Code First**: Show working example immediately
3. **Design Philosophy**: Explain why, not just how
4. **Governance Transparency**: Show team structure
5. **Community Focus**: Contributing guidelines, discussions
6. **Documentation Links**: Point to official docs

## Checklist

- [ ] Logo (centered)
- [ ] Strong one-line description
- [ ] 5+ badges (CI, coverage, version, downloads)
- [ ] Working code example
- [ ] Installation instructions
- [ ] Features list
- [ ] Documentation links
- [ ] Quick start guide
- [ ] Philosophy section
- [ ] Examples section
- [ ] Contributing guide
- [ ] Team/maintainers section
- [ ] License
