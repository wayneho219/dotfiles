---
name: git-workflow
description: >
  Git operation rules for this user. Apply whenever performing git commits,
  branches, pushes, or pull requests.
---

## Timing

Only commit, push, or open a PR when explicitly asked.

## Commits

Use Conventional Commits, written in English. No co-author trailer.
Stage files by name (`git add <file>`), never `git add -A` / `git add .`.

Before every commit or push, scan the staged changes for passwords, tokens,
API keys, and IP addresses. If any is found, stop and tell the user — do not commit.

## Branches

`Wayne-Dev` is the primary development branch — never delete it.
`main` is the protected integration branch on GitHub — never push to it directly.
If the repo has no `Wayne-Dev`, ask the user before creating branches.

Feature/bugfix branches: `<type>/<description>`, branched off `Wayne-Dev`.
Flow: feature → `Wayne-Dev` (rebase) → PR to `main`.
After a PR to `main` is merged, sync `Wayne-Dev` with `main`.

## Pull Requests

When asked to open one: `Wayne-Dev` → `main`, via `gh`.
No "🤖 Generated with Claude Code" in the body.

## Destructive operations

No `push --force`, `reset --hard`, or `--no-verify` unless the user explicitly asks.

## .gitignore

New project, first commit: propose a `.gitignore` and wait for confirmation.
