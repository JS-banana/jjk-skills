# Project Patterns & Type Identification

## Project Type Classification

| Type | Description | Key Signals | README Pattern |
|------|-------------|-------------|----------------|
| **CLI Tool** | Command-line tools | `bin`, `commander`, `yargs`, `click` | Complete Manual |
| **Library/SDK** | Packages for other projects | `main`, `exports`, `types`, npm publish | Minimal Facade / Standard Framework |
| **Web App** | Browser-based applications | `react`, `vue`, `angular`, `next`, `vite` | Minimal Facade |
| **Web Service** | Backend APIs | `express`, `fastify`, `flask`, `fastapi` | Standard Framework |
| **Mobile App** | iOS/Android applications | `expo`, `react-native`, `flutter` | Operation Manual |
| **Desktop App** | Electron/Tauri applications | `electron`, `tauri` | Operation Manual |
| **Monorepo** | Multi-package repositories | `workspaces`, `lerna`, `nx`, `turbo` | Standard Framework |
| **DevOps Tool** | CI/CD or automation | `github-actions`, `terraform`, `ansible` | Operation Manual |
| **Data/ML** | Data science projects | `jupyter`, `pandas`, `tensorflow` | Operation Manual |
| **Docs Site** | Documentation sites | `docusaurus`, `vitepress`, `mkdocs` | Minimal Facade |

## Detection Algorithm

### Layer 1: Language Detection

Count source files by extension (exclude node_modules/, .git/, dist/):

```
.ts, .tsx → TypeScript
.js, .jsx → JavaScript
.py → Python
.go → Go
.rs → Rust
.java → Java
.kt → Kotlin
.swift → Swift
.dart → Dart
```

### Layer 2: Type Detection (Weighted Voting)

#### package.json Analysis (JS/TS Projects)

| Signal | Weight | Rule |
|--------|--------|------|
| `bin` field exists | 0.9 | → CLI Tool |
| `main` or `exports` field | 0.8 | → Library |
| `scripts.start` or `scripts.dev` | 0.4 | → Web App / Web Service |
| `workspaces` field | 0.85 | → Monorepo |
| `dependencies` empty, `devDependencies` not | 0.3 | → CLI Tool (likely) |

#### Dependency Analysis

| Dependency | Type Signal | Weight |
|------------|-------------|--------|
| `react`, `vue`, `angular` | Web App | 0.6 |
| `express`, `fastify`, `koa` | Web Service | 0.6 |
| `commander`, `yargs`, `meow` | CLI Tool | 0.5 |
| `electron` | Desktop App | 0.8 |
| `react-native`, `expo` | Mobile App | 0.8 |

#### Directory Structure Analysis

| Directory | Type Signal | Weight |
|-----------|-------------|--------|
| `pages/`, `app/`, `components/` | Web App | 0.7 |
| `commands/`, `cli/` | CLI Tool | 0.8 |
| `api/`, `routes/`, `controllers/` | Web Service | 0.7 |
| `packages/`, `apps/` | Monorepo | 0.9 |
| `android/`, `ios/` | Mobile App | 0.85 |
| `notebooks/` | Data/ML | 0.7 |

#### Config File Analysis

| Config File | Type Signal | Weight |
|-------------|-------------|--------|
| `vite.config.ts` | Web App | 0.7 |
| `next.config.js` | Web App (Next.js) | 0.8 |
| `angular.json` | Web App (Angular) | 0.9 |
| `electron-builder.yml` | Desktop App | 0.9 |
| `lerna.json`, `nx.json`, `turbo.json` | Monorepo | 0.9 |
| `docusaurus.config.js` | Docs Site | 0.9 |

### Layer 3: Confidence Calculation

```
confidence = highest_score / sum(all_scores)

HIGH (≥ 0.6): Deterministic, use directly
MEDIUM (0.4-0.6): May need confirmation
LOW (< 0.4): Need additional signals
```

## Template Selection Rules

### Minimal Facade Pattern

**When to use:**
- Mature project with dedicated docs site
- Large user base
- README serves as entry point, not full documentation

**Characteristics:**
- Very concise (under 100 lines)
- Logo/Banner at top
- 3 bullet points for value proposition
- Links to docs site
- Minimal code examples

**Examples:** React, Prettier, Vue

### Complete Manual Pattern

**When to use:**
- CLI tools
- Tools that need detailed usage instructions
- No separate documentation site

**Characteristics:**
- Comprehensive usage examples
- Installation table for multiple platforms
- Configuration options detailed
- Troubleshooting section
- Integration with other tools

**Examples:** bat, ripgrep, fd

### Standard Framework Pattern

**When to use:**
- Frameworks and libraries
- Projects with design philosophy
- Projects with governance structure

**Characteristics:**
- Design philosophy section
- Code example at top
- Features list
- Documentation links
- Contributing guidelines
- Team/maintainers info

**Examples:** Express, Fastify, NestJS

### Operation Manual Pattern

**When to use:**
- Personal tools
- Practical utilities
- Projects needing quick start

**Characteristics:**
- Extremely practical
- Multiple deployment methods (pip, Docker, etc.)
- API documentation inline
- Extension/customization guide
- Minimal theory

**Examples:** proxy_pool, various CLI tools

## Tech Stack Detection

### JavaScript/TypeScript Ecosystem

| Dependency | Framework | Type |
|------------|-----------|------|
| `react`, `react-dom` | React | Web UI |
| `next` | Next.js | Full-stack React |
| `vue` | Vue | Web UI |
| `nuxt` | Nuxt.js | Full-stack Vue |
| `angular` | Angular | Web UI |
| `svelte` | Svelte | Web UI |
| `express` | Express.js | Web Service |
| `fastify` | Fastify | Web Service |
| `nestjs` | NestJS | Enterprise Web Service |
| `electron` | Electron | Desktop App |
| `react-native` | React Native | Mobile App |
| `expo` | Expo | Mobile App |
| `commander`, `yargs` | CLI Framework | CLI Tool |

### Python Ecosystem

| Dependency | Framework | Type |
|------------|-----------|------|
| `flask` | Flask | Web Service |
| `fastapi` | FastAPI | Web Service |
| `django` | Django | Full-stack Web |
| `click`, `typer` | CLI Framework | CLI Tool |
| `pandas`, `numpy` | Data Science | Data Processing |
| `tensorflow`, `pytorch` | ML Framework | Machine Learning |

### Go Ecosystem

| Dependency | Framework | Type |
|------------|-----------|------|
| `gin-gonic/gin` | Gin | Web Service |
| `spf13/cobra` | Cobra | CLI Tool |
| `urfave/cli` | CLI Framework | CLI Tool |

## Build Tool Detection

| Config/Dependency | Build Tool |
|-------------------|------------|
| `webpack.config.js` | Webpack |
| `vite.config.ts` | Vite |
| `esbuild` | esbuild |
| `rollup.config.js` | Rollup |
| `tsconfig.json` | TypeScript Compiler |
| `Cargo.toml` | Rust (cargo) |
| `go.mod` | Go |
| `pyproject.toml` | Python (pip/poetry) |

## Test Framework Detection

| Dependency | Test Framework | Language |
|------------|----------------|----------|
| `jest` | Jest | JS/TS |
| `vitest` | Vitest | JS/TS |
| `mocha` | Mocha | JS/TS |
| `playwright` | Playwright | JS/TS |
| `cypress` | Cypress | JS/TS |
| `pytest` | pytest | Python |
| `go test` | Go testing | Go |
| `cargo test` | Rust testing | Rust |
