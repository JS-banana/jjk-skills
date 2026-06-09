> **Note**: This is a reference example for learning purposes, not a template to copy.
> Generate your AGENTS.md based on the six essential sections principle.

# [Project Name] - Backend

## Stack
[Runtime] / [Framework] / [Database] / [ORM] / [Key libraries - with versions]

## Commands
- Install: `[command]`
- Dev: `[command]`
- Build: `[command]`
- Test: `[command]`
- Test single: `[command]`
- Lint: `[command]`
- Migrate: `[command]`
- Migrate rollback: `[command]`

## Conventions
- Use Decimal, not float, for all financial calculations
- All external API calls wrapped in try/catch with project Logger
- Database migrations in `[path]`; always provide downgrade path
- All responses follow `{ data, error }` envelope

## Non-Obvious Patterns
- Auth uses JWT with rotating refresh tokens (not session-based)
- [Pattern 2: counter-intuitive decision and why]

## Boundaries
### Always
- Run migrations check before applying
- Validate all external input

### Ask First
- Database schema changes
- Add new dependencies
- Modify authentication flow

### Never
- Commit secrets, .env files
- Force push to main
- Modify committed migrations
- Expose internal error details to client

## Testing
- All new endpoints must have integration tests
- Mock external services
- Use transactions for test isolation
- Run `[test command]` before marking complete
