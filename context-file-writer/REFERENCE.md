# Context File Writer - Detailed Reference

> **Design Philosophy**: This skill uses "principle-driven" approach, not "template-driven".
> The six essential sections are guidelines, not rigid templates.
> Examples in `examples/` directory are for learning purposes only — generate your AGENTS.md based on principles, not by copying templates.

## Research Data

### Key Statistics

| Source | Finding |
|--------|---------|
| ETH Zurich 2025 | Auto-generated AGENTS.md reduces success rate ~3%, increases cost 20%+ |
| ETH Zurich 2025 | Human-written AGENTS.md only improves ~4%, still increases cost 19% |
| GitHub Blog | Most failures due to vague instructions, not technical limitations |
| Augment Code | Decision tables improve best_practices by 25% |
| HumanLayer | Effective AGENTS.md can be under 60 lines |
| ICLR 2026 | Agent default non-interactive behavior reduces solve rate from 48.8% to 28% |

### Instruction Budget

- LLM reliably follows ~150-200 instructions
- Agent harness already uses ~50 instructions
- Your file has ~100-150 instruction budget

## Detailed Guidance

### Section 1: Project Overview (WHAT)

**Purpose**: Anchor agent's understanding of the project scope

**Good examples**:
```
# Next.js Development Guide
This is a pnpm monorepo containing the Next.js framework and related packages.
```

```
Node.js 22 / React 19 / TypeScript 5.4 strict / PostgreSQL 16
```

**Bad examples**:
```
A web application for managing users.
```
(Too vague, no tech stack info)

### Section 2: Commands (HOW)

**Purpose**: Highest value section — AI cannot guess these

**Put this FIRST** — ETH research shows tools mentioned in AGENTS.md are used 160x more

**Good format**:
```markdown
## Commands
- Install: `pnpm install`
- Dev: `pnpm dev`
- Build: `pnpm build`
- Test: `pnpm test`
- Test single: `pnpm test -- path/to/file.test.ts`
- Lint: `pnpm lint`
- Typecheck: `pnpm typecheck`
```

**Bad format**:
```markdown
## Commands
Run npm install to install dependencies. Then run npm test to test.
```
(Not executable, no flags)

### Section 3: Non-Obvious Patterns (WHY)

**Purpose**: Highest signal density — record counter-intuitive decisions

**Good examples**:
```markdown
## Non-Obvious Patterns
- `client.api` never throws exceptions, it returns `ApiResult`
  - Wrapping in try/catch is incorrect
- All API routes return `{ data, error }` envelope
- Database migrations must provide downgrade path
```

**Why this matters**: Without these rules, agent will add try/catch to every API call

### Section 4: Conventions (HOW)

**Purpose**: Project-specific rules only

**Good examples**:
```markdown
## Conventions
- Named exports only, no default exports
- Components in `src/components/`, one component per file
- Use `@/` path alias, not relative imports
- Use Decimal, not float, for financial calculations
```

**Bad examples**:
```markdown
## Conventions
- Write clean, readable code
- Follow SOLID principles
- Use proper error handling
```
(Too vague, no actionable guidance)

**Note**: If linter can enforce it, don't write it here

### Section 5: Boundaries (WHAT NOT)

**Purpose**: Three-tier permission model

**Template**:
```markdown
## Boundaries
### Always
- Read files, list directories
- Run lint, typecheck, single test files

### Ask First
- Install or remove packages
- Delete files
- Push to git or open PR
- Database schema changes

### Never
- Commit secrets, .env files
- Force push to main
- Modify vendor/, dist/, build/
```

**Research finding**: GitHub analysis of 2500+ repos found "Never commit secrets" is the most common effective constraint

### Section 6: Testing (HOW)

**Purpose**: Exact commands, not vague guidance

**Good examples**:
```markdown
## Testing
- All new features must have tests
- Tests must be deterministic and isolated
- Mock all external dependencies
- Run `npm test` before marking work complete
```

**Bad examples**:
```markdown
## Testing
Write good tests with high coverage.
```
(Not verifiable)

## Anti-Patterns Reference

### Anti-Pattern 1: Prose Instead of Commands

**Wrong**:
```
Ensure the code is properly tested with good coverage.
```

**Right**:
```
Run `pytest --cov=app --cov-fail-under=80` before every commit.
```

**Reason**: Agent cannot verify "properly tested", but can check exit code

### Anti-Pattern 2: Vague Instructions

**Wrong**:
```
- Be careful with database migrations
- Handle errors gracefully where possible
```

**Right**:
```
- Run `alembic check` before applying migrations. Abort if downgrade path missing.
- Wrap external API calls in try/catch; log errors using project Logger, not console.log.
```

### Anti-Pattern 3: Abstract Principles

**Wrong**:
```
SOLID, KISS, YAGNI
```

**Right**:
```
Use named exports only, no default exports.
API routes return `{ data, error }` shape.
```

### Anti-Pattern 4: Contradicting Priorities

**Wrong**:
```
- Ship fast
- 100% test coverage
- Zero technical debt
```

**Right**:
```
Priority 1: Tests pass
Priority 2: Under 5 minutes
Priority 3: Ship fast
```

### Anti-Pattern 5: Code Style Rules

**Wrong**:
```
Use single quotes for strings, double quotes for JSX attributes.
```

**Right**: Use linter and formatter instead

**Reason**: LLM is in-context learner, follows existing patterns automatically

### Anti-Pattern 6: File Too Long

- ETH Zurich: Auto-generated AGENTS.md reduces success rate ~3%
- Recommendation: < 300 lines (HumanLayer: 60 lines)
- Codex enforces 32KiB limit

### Anti-Pattern 7: Auto-Generated Without Editing

**Wrong**: Use `/init` and keep as-is

**Reason**: Research shows LLM-generated files are redundant with existing docs

### Anti-Pattern 8: Multiple Parallel Copies

**Wrong**: Maintain separate CLAUDE.md, .cursorrules, copilot-instructions.md

**Right**: Single source of truth (AGENTS.md) + symlinks

### Anti-Pattern 9: Outdated Information

- Node.js version changed but file not updated
- Database migrated but file references old one
- Project structure changed but directory list missing

### Anti-Pattern 10: Only "Don't" Without "Do"

**Wrong**:
```
Don't instantiate HTTP clients directly.
```

**Right**:
```
Don't instantiate HTTP clients directly.
Use the shared `apiClient` from `lib/http` with retry middleware.
```

### Anti-Pattern 11: Detailed Directory Listings

ETH Zurich: Removing "Architecture" section had no effect on agent behavior, but reduced token cost

### Anti-Pattern 12: Task-Specific Instructions

**Wrong**: 200-line database migration guide in main file

**Right**: Put in separate file, reference in main file

## Progressive Disclosure

### Root AGENTS.md (100-150 lines)

```markdown
# Project Name

## Stack
[One line: tech + versions]

## Commands
[All key commands]

## Non-Obvious Patterns
[Counter-intuitive decisions]

## Conventions
[Project-specific rules]

## Boundaries
[Always / Ask First / Never]

## Testing
[Exact commands]
```

### Separate Files

```
docs/
├── TESTING.md      # Detailed test rules
├── CONVENTIONS.md  # Code conventions
└── DATABASE.md     # Database patterns

.claude/
└── rules/          # Path-scoped rules
```

### Subdirectory AGENTS.md

For monorepo, each package can have its own AGENTS.md with package-specific rules

## Multi-Tool Strategy

### AGENTS.md as Single Source

```bash
# Create AGENTS.md as canonical source
# Then create symlinks for other tools
ln -s AGENTS.md CLAUDE.md
```

### Tool-Specific Additions

Only add tool-specific files when needed:
- `.cursor/rules/*.mdc` — Cursor-specific activation modes
- `.github/copilot-instructions.md` — Copilot-specific features

## Update Strategies

### Trigger Conditions

- AI repeatedly makes same mistake
- Architecture decision finalized
- New tool or process introduced
- Project phase completed

### Incremental Updates

Stanford/SambaNova research: Incremental updates reduce 86% drift vs full rewrites

**Process**:
1. Identify specific rule to update
2. Update only that rule
3. Keep unchanged parts intact

### Agent-Assisted Updates

Prompt to use at end of session:
```
If there's a nugget of knowledge learned in this conversation, update AGENTS.md.
Only add durable, generalizable lessons. Don't add bug-specific notes.
```

### Review Cadence

- Fast-moving teams: Monthly
- Stable codebases: Quarterly

**Review questions**:
1. Still accurate?
2. Still being followed?
3. Missing anything causing AI mistakes?

## Project Type Templates

See `templates/` directory:
- `minimal.md` — Smallest viable file
- `frontend.md` — React/Vue/Angular
- `backend.md` — API/server
- `monorepo.md` — Multi-package repos
- `cli.md` — Command-line tools
- `library.md` — SDK/package projects

## References

- ETH Zurich paper: https://arxiv.org/abs/2602.11988
- GitHub Blog: https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
- Augment Code: https://www.augmentcode.com/guides/how-to-build-agents-md
- HumanLayer: https://www.humanlayer.dev/blog/writing-a-good-claude-md
- Phil Schmid: https://www.philschmid.de/writing-good-agents
