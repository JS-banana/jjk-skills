#!/bin/bash
# Validate AGENTS.md/CLAUDE.md quality
# Usage: bash validate.sh [file]

set -e

FILE="${1:-AGENTS.md}"

if [ ! -f "$FILE" ]; then
    echo "❌ File not found: $FILE"
    exit 1
fi

echo "📋 Validating: $FILE"
echo ""

# Check 1: Line count
LINES=$(wc -l < "$FILE")
if [ "$LINES" -gt 300 ]; then
    echo "❌ Too many lines: $LINES (target: < 300)"
elif [ "$LINES" -gt 200 ]; then
    echo "⚠️  Lines: $LINES (approaching limit, consider splitting)"
else
    echo "✅ Lines: $LINES"
fi

# Check 2: Commands section exists and is early
if grep -q "^## Commands" "$FILE" || grep -q "^## Key Commands" "$FILE"; then
    CMD_LINE=$(grep -n "^## Commands\|^## Key Commands" "$FILE" | head -1 | cut -d: -f1)
    if [ "$CMD_LINE" -lt 20 ]; then
        echo "✅ Commands section at line $CMD_LINE (good: early in file)"
    else
        echo "⚠️  Commands section at line $CMD_LINE (consider moving earlier)"
    fi
else
    echo "❌ No '## Commands' section found"
fi

# Check 3: No code style rules
STYLE_PATTERNS="single quotes|double quotes|indentation|spacing|formatting|prettier|eslint config"
if grep -qi "$STYLE_PATTERNS" "$FILE"; then
    echo "⚠️  Possible code style rules detected (use linter instead)"
else
    echo "✅ No code style rules"
fi

# Check 4: Boundaries section
if grep -q "^## Boundaries" "$FILE"; then
    echo "✅ Boundaries section found"
    if grep -q "### Never" "$FILE"; then
        echo "✅ 'Never' subsection found"
    else
        echo "⚠️  Consider adding '### Never' subsection"
    fi
else
    echo "⚠️  No '## Boundaries' section (consider adding)"
fi

# Check 5: No vague instructions
VAGUE_PATTERNS="follow best practices|be careful|handle gracefully|write clean|proper error handling"
if grep -qi "$VAGUE_PATTERNS" "$FILE"; then
    echo "⚠️  Vague instructions detected (be specific and verifiable)"
else
    echo "✅ No vague instructions"
fi

# Check 6: File size
SIZE=$(wc -c < "$FILE")
if [ "$SIZE" -gt 32768 ]; then
    echo "❌ File too large: $SIZE bytes (Codex limit: 32KiB)"
elif [ "$SIZE" -gt 10240 ]; then
    echo "⚠️  File size: $SIZE bytes (consider splitting)"
else
    echo "✅ File size: $SIZE bytes"
fi

echo ""
echo "📊 Summary"
echo "   Lines: $LINES / 300"
echo "   Size:  $SIZE bytes / 32768"
echo ""

# Overall assessment
ISSUES=0
[ "$LINES" -gt 300 ] && ISSUES=$((ISSUES + 1))
[ "$SIZE" -gt 32768 ] && ISSUES=$((ISSUES + 1))

if [ "$ISSUES" -eq 0 ]; then
    echo "✅ Validation passed"
else
    echo "❌ Found $ISSUES critical issue(s)"
    exit 1
fi
