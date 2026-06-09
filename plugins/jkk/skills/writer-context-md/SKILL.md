---
name: context-file-writer
description: Create and maintain high-quality AGENTS.md/CLAUDE.md files for AI agent context. Use when user wants to create, optimize, or update project context files for Claude Code, Codex, Cursor, Copilot, or other AI coding tools.
---

# Context File Writer

Create and maintain AGENTS.md/CLAUDE.md files based on research data (ETH Zurich, GitHub 2500+ repos).

## Core Principle

**Less is more.** Target < 300 lines. Use progressive disclosure — details in separate files.

## Workflows

### 1. New Project Creation

Ask user:
1. Tech stack and versions
2. Project type (frontend/backend/monorepo/CLI/library)
3. Key commands (install, dev, build, test, lint)
4. Non-obvious patterns or conventions

Generate file based on six essential sections. Explain each section's purpose.

### 2. Existing File Optimization

Analyze current file for common problems:
- Too long (> 300 lines)
- Contains code style rules (use linter instead)
- Contains directory listings (agent can discover)
- Vague instructions ("be careful with X")

Provide specific fixes with rationale.

### 3. Periodic Update

Guide user through review checklist:
- [ ] Still accurate? (commands, paths, versions)
- [ ] Still relevant? (remove obsolete rules)
- [ ] Missing anything? (AI recurring mistakes)

Use incremental updates, not full rewrites.

### 4. Multi-Tool Unification

If team uses multiple AI tools:
1. Use AGENTS.md as single source of truth
2. Create symlinks: `ln -s AGENTS.md CLAUDE.md`
3. Only add tool-specific files when needed

## File Structure

```
project/
├── AGENTS.md              # Main entry (100-150 lines)
├── CLAUDE.md              # Symlink to AGENTS.md
├── docs/
│   ├── TESTING.md         # Detailed test rules
│   └── CONVENTIONS.md     # Code conventions
└── .claude/
    └── rules/             # Path-scoped rules
```

## Six Essential Sections

1. **Stack** — Tech + versions (one line)
2. **Commands** — Install, dev, build, test, lint (put first!)
3. **Non-Obvious Patterns** — Counter-intuitive decisions
4. **Conventions** — Project-specific only
5. **Boundaries** — Always / Ask First / Never
6. **Testing** — Exact commands, not vague guidance

## Anti-Patterns to Detect

- Code style rules → use linter
- Directory listings → agent discovers
- "Follow best practices" → be specific
- Contradicting priorities → number them
- Auto-generated content → rewrite manually

## Quality Checklist

Before finalizing:
- [ ] < 300 lines total
- [ ] Commands in first 20 lines
- [ ] Every instruction executable/verifiable
- [ ] No code style rules
- [ ] Boundaries clearly defined
- [ ] No outdated information

## References

- `REFERENCE.md` — Detailed guidance, examples, research data
- `examples/` — Reference examples (for learning, not copying)
- `research/` — Original research materials (for future optimization)

## Writing Style

- Use imperative mood ("Run X", not "You should run X")
- Be specific and verifiable
- Code examples > prose descriptions
- Negative rules paired with alternatives
