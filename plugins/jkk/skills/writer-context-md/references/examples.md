# Examples

Use these as reusable shapes, not templates to copy blindly.

## Minimal Root AGENTS.md

```md
# AGENTS.md

## Stack
- Node 22 / pnpm 10 / TypeScript strict / PostgreSQL 16.

## Commands
- Install: `pnpm install`
- Dev: `pnpm dev`
- Build: `pnpm build`
- Test all: `pnpm test`
- Test one: `pnpm vitest run path/to/file.test.ts`
- Typecheck: `pnpm typecheck`
- Lint: `pnpm lint`

## Non-Obvious Patterns
- API helpers return `ApiResult`; do not wrap them in try/catch unless the
  function explicitly throws.
- `src/generated/*` is generated. Change schemas and run `pnpm generate`.

## Boundaries
### Always
- Read files and run focused tests.
- Update tests when behavior changes.

### Ask First
- Add dependencies.
- Change database schemas or migrations.
- Delete files.

### Never
- Commit secrets or `.env` files.
- Modify `dist/`, `vendor/`, or generated files by hand.

## Verification
- Run the smallest relevant check before finishing.
- If a check cannot run, report the command and reason.
```

## Reference Map Section

```md
## Reference Map
- Read `docs/testing.md` before changing test helpers or CI.
- Read `docs/architecture.md` before changing cross-service contracts.
- Read `docs/release.md` only for release tasks.
```

## Nested Package Context

```md
# apps/web/AGENTS.md

## Web App Rules
- Use `pnpm --filter web test` for focused web tests.
- Run Playwright only when UI behavior, routing, or accessibility changes.
- Do not edit generated route files directly; run `pnpm --filter web routes`.
```

## Multi-Tool Adapter

Use when `AGENTS.md` is canonical but another tool expects a specific file.

```md
# CLAUDE.md

This repository uses `AGENTS.md` as the canonical agent instruction file.
Read `AGENTS.md` first. Only use this file for Claude-specific notes below.

## Claude-Specific Notes
- [Add only product-specific behavior here.]
```

## Review Finding Format

```md
Findings
- High: `pnpm test` is listed, but `package.json` only defines `test:unit`.
  Replace with `pnpm test:unit` and add the single-test command from Vitest.
- Medium: "Be careful with migrations" is not actionable. Replace with the
  migration command and ask-first boundary.
- Low: The directory tree duplicates README content. Delete it or replace with
  a link to `README.md`.

Score: 74/100 (B)
Main risk: commands and boundaries are useful, but stale command names and
vague migration guidance will still cause mistakes.
```
