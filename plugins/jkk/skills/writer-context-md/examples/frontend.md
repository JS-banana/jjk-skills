> **Note**: This is a reference example for learning purposes, not a template to copy.
> Generate your AGENTS.md based on the six essential sections principle.

# [Project Name] - Frontend

## Stack
Node.js [version] / React [version] / TypeScript [version] / [State management] / [Styling]

## Commands
- Install: `pnpm install`
- Dev: `pnpm dev`
- Build: `pnpm build`
- Test: `pnpm test`
- Test single: `pnpm test -- path/to/file.test.ts`
- Lint: `pnpm lint`
- Typecheck: `pnpm typecheck`

## Conventions
- Named exports only, no default exports
- Components in `src/components/`, one component per file
- Use `@/` path alias, not relative imports
- Server state → React Query, client state → Zustand
- Forms use react-hook-form + zod validation

## Non-Obvious Patterns
- [Pattern 1: counter-intuitive decision and why]
- [Pattern 2: counter-intuitive decision and why]

## Boundaries
### Always
- Run lint and typecheck after changes

### Ask First
- Install new packages
- Modify routing configuration

### Never
- Commit secrets or .env files
- Use `any` type
- Add inline styles (use CSS modules/Tailwind)

## Testing
- All new components must have tests
- Use React Testing Library, not enzyme
- Mock API calls with MSW
- Run `pnpm test` before marking complete
