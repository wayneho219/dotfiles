# Dotfiles Project Rules

## Security

Before every commit or push, scan all staged content for sensitive information:
- Passwords, tokens, API keys, secrets
- Internal IP addresses, server hostnames
- Personal accounts, student IDs, emails

If found, stop immediately and warn the user. Do not proceed until confirmed.
