# Complete Manual Pattern

## When to Use

- CLI tools
- Tools that need detailed usage instructions
- No separate documentation site
- Users need to understand all features

## Structure

```markdown
# Project Name - One-line description

[Badges]

> Brief description

## Features
## How to Use
## Installation
## Customization
## Configuration
## Troubleshooting
## Development
## License
```

## Example: bat Style

```markdown
# bat - a cat clone with wings

[![Build Status](https://github.com/sharkdp/bat/actions/workflows/CICD.yml/badge.svg)](https://github.com/sharkdp/bat/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> A cat(1) clone with syntax highlighting and Git integration.

## Features

- **Syntax highlighting** for 200+ languages
- **Git integration** shows file changes
- **Show non-printable characters** like tabs and backspaces
- **Automatic paging** with less/more
- **Smart file detection** handles binary files gracefully

## How to Use

### Basic Usage

```bash
# View a file
bat README.md

# View multiple files
bat src/*.js

# Read from stdin
curl -s https://example.com | bat -l html
```

### Integration with Other Tools

#### fzf

```bash
# Use bat as preview for fzf
fzf --preview 'bat --color=always --style=numbers --line-range=:500 {}'
```

#### find

```bash
# View all JavaScript files
find . -name "*.js" -exec bat {} +
```

#### tail

```bash
# Watch a file with syntax highlighting
tail -f /var/log/syslog | bat -l syslog
```

#### git

```bash
# Use bat as git pager
git config --global pager.diff "bat --style=numbers"
git config --global pager.show "bat --style=numbers"
```

#### man

```bash
# Use bat as man pager
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
```

## Installation

### On Ubuntu (using apt)

```bash
sudo apt install bat
```

### On macOS (using Homebrew)

```bash
brew install bat
```

### On Windows (using Scoop)

```bash
scoop install bat
```

### On Windows (using Chocolatey)

```bash
choco install bat
```

### On Arch Linux

```bash
sudo pacman -S bat
```

### On Fedora

```bash
dnf install bat
```

### On Alpine Linux

```bash
apk add bat
```

### Build from Source

```bash
git clone https://github.com/sharkdp/bat.git
cd bat
cargo install --path .
```

### Using Cargo

```bash
cargo install bat
```

## Customization

### Themes

```bash
# List available themes
bat --list-themes

# Use a specific theme
bat --theme="Monokai Extended" file.js

# Set default theme
export BAT_THEME="Monokai Extended"
```

### Output Style

```bash
# Show only line numbers
bat --style=numbers file.js

# Show only changes
bat --style=changes file.js

# Show full output
bat --style=full file.js

# Combine styles
bat --style=numbers,changes file.js
```

### Decorations

```bash
# Disable decorations
bat --decorations=never file.js

# Force decorations
bat --decorations=always file.js
```

### Line Ranges

```bash
# Show lines 10-20
bat --line-range=10:20 file.js

# Show first 50 lines
bat --line-range=:50 file.js

# Show from line 100
bat --line-range=100: file.js
```

### Highlight Lines

```bash
# Highlight line 5
bat --highlight-line=5 file.js

# Highlight lines 5-10
bat --highlight-line=5:10 file.js

# Highlight multiple ranges
bat --highlight-line=5:10 --highlight-line=20:25 file.js
```

## Configuration

### Configuration File

Generate default configuration:

```bash
bat --generate-config-file
```

Configuration file location:
- Linux/macOS: `~/.config/bat/config`
- Windows: `%APPDATA%\bat\config`

### Example Configuration

```bash
# Set theme
--theme="Monokai Extended"

# Set style
--style="numbers,changes"

# Set tab width
--tabs=4

# Set map syntax
--map-syntax "*.conf:INI"
--map-syntax ".ignore:Git Ignore"
```

### Environment Variables

```bash
# Set theme
export BAT_THEME="Monokai Extended"

# Set style
export BAT_STYLE="numbers,changes"

# Set config file
export BAT_CONFIG_PATH="/path/to/config"

# Set cache directory
export BAT_CACHE_PATH="/path/to/cache"
```

## Troubleshooting

### Colors not showing

```bash
# Force color output
bat --color=always file.js

# Check terminal support
echo $TERM
```

### Slow startup

```bash
# Disable paging
bat --paging=never file.js

# Use faster pager
bat --pager="less -R" file.js
```

### Binary files detected incorrectly

```bash
# Force text mode
bat --wrap=never file.js

# Specify language
bat -l javascript file.js
```

### Windows issues

```bash
# Use --no-paging on Windows
bat --no-paging file.js

# Use Windows-style paths
bat "C:\Users\file.js"
```

## Development

### Build

```bash
git clone https://github.com/sharkdp/bat.git
cd bat
cargo build
```

### Test

```bash
cargo test
```

### Benchmarks

```bash
cargo bench
```

## Maintainers

- [sharkdp](https://github.com/sharkdp)
- [eth-p](https://github.com/eth-p)

## License

[MIT](./LICENSE) or [Apache 2.0](./LICENSE-APACHE)
```

## Key Principles

1. **Comprehensive Usage**: Show all major use cases
2. **Integration Examples**: How to use with other tools
3. **Multi-Platform Installation**: Cover all major platforms
4. **Customization Depth**: All configuration options
5. **Troubleshooting**: Common issues and solutions
6. **Development Info**: How to build and test

## Checklist

- [ ] Title with concise description
- [ ] Badges (CI, license, version)
- [ ] One-line description
- [ ] Features list
- [ ] Basic usage examples
- [ ] Integration with other tools
- [ ] Installation table (all platforms)
- [ ] Customization options
- [ ] Configuration file docs
- [ ] Environment variables
- [ ] Troubleshooting section
- [ ] Development section
- [ ] License
