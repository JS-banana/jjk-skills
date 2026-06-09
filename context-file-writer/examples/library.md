> **Note**: This is a reference example for learning purposes, not a template to copy.
> Generate your AGENTS.md based on the six essential sections principle.

# [Project Name] - Library/SDK

## Stack
[Language] / [Build tool] / [Test framework]

## Commands
- Test: `[command]`
- Build: `[command]`
- Lint: `[command]`
- Publish: `[command]`

## Conventions
- Semantic versioning strictly enforced
- All public APIs must have JSDoc/docstring with `@example`
- Breaking changes require deprecation period of 2 minor versions
- Internal modules prefixed with `_` (not exported)

## Non-Obvious Patterns
- Types exported from `src/types.ts`, not co-located with implementation
- [Pattern 2: counter-intuitive decision and why]

## Public API
```typescript
// Main entry point
export { mainFunction } from './core'
export type { MainType } from './types'

// Named exports for tree-shaking
export { helper1, helper2 } from './helpers'
```

## Boundaries
### Always
- Maintain backward compatibility
- Add JSDoc for all public APIs
- Update changelog

### Ask First
- Add new public API
- Change existing API signature
- Update major version

### Never
- Export internal implementation details
- Break semver contract
- Remove deprecated APIs without notice

## Testing
- 100% coverage for public APIs
- Test all edge cases
- Test in multiple environments (Node, Bun, Deno if applicable)
- Run `[test command]` before publishing
