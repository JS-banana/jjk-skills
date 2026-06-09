> **Note**: This is a reference example for learning purposes, not a template to copy.
> Generate your AGENTS.md based on the six essential sections principle.

# [Project Name] - Monorepo

## Stack
[Package manager] / [Build tool] / [Shared libraries]

## Structure
```
├── packages/
│   ├── web/         # Frontend application
│   ├── api/         # Backend API
│   └── shared/      # Shared utilities
├── apps/            # Deployable applications
└── docs/            # Documentation
```

## Commands
- Install: `[command]`
- Build all: `[command]`
- Build package: `[command] --filter=[package]`
- Test all: `[command]`
- Test package: `[command] --filter=[package]`
- Lint: `[command]`

## Conventions
- Shared code goes in `packages/shared`
- Each package has its own AGENTS.md for package-specific rules
- Use workspace protocol for internal dependencies
- Follow conventional commits: `type(scope): description`

## Non-Obvious Patterns
- [Pattern 1: how packages depend on each other]
- [Pattern 2: build order requirements]

## Boundaries
### Always
- Run affected tests after changes
- Check dependency graph before adding new deps

### Ask First
- Add new package
- Modify shared library API
- Change build configuration

### Never
- Commit secrets or .env files
- Create circular dependencies
- Bypass package boundaries

## Testing
- Test affected packages: `[command] --filter=[package]...`
- Integration tests in `apps/` test cross-package interactions
- Run full suite before major releases
