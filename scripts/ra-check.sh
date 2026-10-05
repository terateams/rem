#!/bin/sh
# RA仓规 check. Run from the repository root: sh scripts/ra-check.sh
RA_VERSION=0.6.1
fail=0
err() { echo "FAIL: $1"; fail=1; }

# Rule 1: one root AGENTS.md, small enough for Codex
if [ -f AGENTS.md ]; then
  [ "$(wc -c < AGENTS.md)" -le 32768 ] || err "AGENTS.md is larger than 32 KiB"
else
  err "AGENTS.md is missing in the repository root"
fi

# Rule 2: no other instruction files
for f in .github/copilot-instructions.md; do
  [ ! -e "$f" ] || err "$f must not exist"
done
for d in .github/instructions; do
  [ ! -d "$d" ] || err "$d/ must not exist"
done

# Rule 3: no nested AGENTS.md
nested=$(find . \( -path ./.git -o -path ./node_modules \) -prune -o -name AGENTS.md -print | grep -v '^\./AGENTS\.md$')
[ -z "$nested" ] || err "nested AGENTS.md found: $nested"

# Rules 8 and 9: skills
if [ -d .agents/skills ]; then
  for d in .agents/skills/*/; do
    [ -d "$d" ] || continue
    n=$(basename "$d")
    s="${d}SKILL.md"
    if [ ! -f "$s" ]; then err "$s is missing"; continue; fi
    grep -q "^name: *$n *$" "$s" || err "$s: name must be $n"
    desc=$(grep -m1 '^description:' "$s" | sed 's/^description: *//')
    [ -n "$desc" ] || err "$s: description is missing"
    [ "${#desc}" -le 1024 ] || err "$s: description is longer than 1024 characters"
  done
fi

[ "$fail" -eq 0 ] && echo "RA仓规 $RA_VERSION: OK"
exit "$fail"
