> **Note**: This is a reference example for learning purposes, not a template to copy.
> Generate your AGENTS.md based on the six essential sections principle.

# [Project Name] - CLI Tool

## Stack
[Language] / [CLI framework] / [Key libraries]

## Commands
- Build: `[command]`
- Test: `[command]`
- Lint: `[command]`
- Install locally: `[command]`
- Run: `[command] [args]`

## Conventions
- All CLI args parsed with [framework] derive macros
- Error messages go to stderr, data output to stdout
- Exit codes: 0 = success, 1 = user error, 2 = internal error
- Use [logging framework], not println!

## Non-Obvious Patterns
- Config file location: `~/.config/[tool]/config.toml` (XDG compliant)
- [Pattern 2: counter-intuitive decision and why]

## Arguments
```
[tool] [command] [options]

Commands:
  command1    Description of command1
  command2    Description of command2

Options:
  -f, --flag    Description of flag
  -o, --opt     Description of option with value
```

## Boundaries
### Always
- Validate all user input
- Provide helpful error messages
- Show help when no args provided

### Ask First
- Modify config file format
- Change default behavior
- Add new subcommand

### Never
- Write to system directories without permission
- Expose internal errors to user
- Break backward compatibility

## Testing
- Unit tests for core logic
- Integration tests for CLI commands
- Test error cases and edge cases
- Run `[test command]` before marking complete
