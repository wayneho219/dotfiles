#!/usr/bin/env bash
# DGX Spark version of claude/plugins/claude-hud/apply-patches.sh, written for claude-hud 0.8.0
# (the macOS script's regexes don't match 0.8.0 source). Re-run after every plugin update.
# Patches: drop git:( ) wrapper and move branch to the end of line 1, fixed 7-cell bars,
# hide weekly reset time, "resets in" -> ↻, reset countdown as HH:MM.
# Idempotent: running it on already-patched files changes nothing.
set -euo pipefail

d=$(ls -d "${CLAUDE_CONFIG_DIR:-$HOME/.claude}"/plugins/cache/claude-hud/claude-hud/*/ | sort -V | tail -1)
r="$d/dist/render/lines"
echo "patching $d"

# project.js: branch without git:( ), as its own segment at the end of line 1
perl -pi -e 's/gitPart = `\$\{gitColor\(vcsLabel, colors\)\}\$\{gitInner\.join\(. .\)\}\$\{gitColor\(.\)., colors\)\}`;/gitPart = gitInner.join(" ");/' "$r/project.js"
perl -0pi -e '
  s/if \(projectWithDirs && gitPart\) \{.*?\n    else if \(gitPart\) \{\n        push\(gitPart, .project.\);\n    \}/if (projectWithDirs) {\n        push(projectWithDirs, \x27project\x27);\n    }/s;
  s/(\n    if \(parts\.length === 0\) \{)/\n    if (gitPart) {\n        push(gitPart, \x27git\x27);\n    }$1/ unless /push\(gitPart, .git.\)/;
' "$r/project.js"

# identity.js: context bar fixed at 7 cells
perl -pi -e 's/coloredBar\(percent, getAdaptiveBarWidth\(\), colors, contextThresholds\)/coloredBar(percent, 7, colors, contextThresholds)/' "$r/identity.js"

# usage.js: usage bars 7 cells, no weekly reset time
perl -0pi -e '
  s/const barWidth = getAdaptiveBarWidth\(\);/const barWidth = 7;/;
  s/resetAt: ctx\.usageData\.sevenDayResetAt,(\s*windowMs: SEVEN_DAY_WINDOW_MS,)/resetAt: null,$1/g;
' "$r/usage.js"

# en.js: "resets in" -> ↻
perl -pi -e 's/"format\.resetsIn": "resets in"/"format.resetsIn": "↻"/' "$d/dist/i18n/en.js"

# format-reset-time.js: countdown under 24h as HH:MM
perl -pi -e '
  s/return mins > 0 \? `\$\{hours\}h \$\{mins\}m` : `\$\{hours\}h`;/return `\${String(hours).padStart(2, "0")}:\${String(mins).padStart(2, "0")}`;/;
  s/return `\$\{diffMins\}m`;/return `00:\${String(diffMins).padStart(2, "0")}`;/;
' "$d/dist/render/format-reset-time.js"

grep -q 'gitPart = gitInner.join' "$r/project.js" && grep -q "push(gitPart, 'git')" "$r/project.js" \
  && ! grep -q "push(\`\${projectWithDirs} \${gitPart}\`" "$r/project.js" \
  && grep -q 'coloredBar(percent, 7' "$r/identity.js" \
  && grep -q 'const barWidth = 7' "$r/usage.js" && [ "$(grep -c 'resetAt: null' "$r/usage.js")" -ge 2 ] \
  && grep -q '"format.resetsIn": "↻"' "$d/dist/i18n/en.js" \
  && grep -q 'return `00:' "$d/dist/render/format-reset-time.js" \
  && echo "ok" || { echo "some patch did not apply — plugin source changed, patch by hand"; exit 1; }
