---
name: git-workflow
description: >
  Git operation rules for this user. Apply whenever performing git commits,
  branches, pushes, or pull requests.
---

## Commits

Use Conventional Commits format: `<type>([optional scope]): <description>`.
No co-author trailer.

## Branches

Default branch is `Wayne-Dev` — never delete it.
Feature/Bugfix branches should be named as `<type>/<description>`.

## Timing

Only commit or push when explicitly asked.

## Pull Requests

Always open a PR (`Wayne-Dev` → `main`) using GitHub CLI (`gh`).
Never push directly to `main`.
No "🤖 Generated with Claude Code" in PR body.

## .gitignore

Before the first commit in a new project, suggest a `.gitignore` and wait for confirmation.

## Security

Before every commit or push, scan all staged content for sensitive information:
- Passwords, tokens, API keys, secrets
- Internal IP addresses, server hostnames
- Personal accounts, student IDs, emails

If found, stop immediately and warn the user. Do not proceed until confirmed.
