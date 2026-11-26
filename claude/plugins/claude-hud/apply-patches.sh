#!/usr/bin/env bash
# Re-apply local claude-hud layout patches after a plugin update.
# Patches: drop git:( ) wrapper, project before model, fixed 7-cell bars, hide weekly reset time.
# Idempotent: running it on already-patched files changes nothing.
set -euo pipefail

d=$(ls -d "${CLAUDE_CONFIG_DIR:-$HOME/.claude}"/plugins/cache/claude-hud/claude-hud/*/ | sort -V | tail -1)
r="$d/dist/render/lines"
echo "patching $d"

# project.js: branch without git:( ), project first
perl -0pi -e '
  s/gitPart = `\$\{gitColor\(.git:\(., colors\)\}\$\{gitInner\.join\(. .\)\}\$\{gitColor\(.\)., colors\)\}`;/gitPart = gitInner.join(" ");/;
  s/if \(projectPart && gitPart\) \{\s*parts\.push\(`\$\{projectPart\} \$\{gitPart\}`\);\s*\}\s*else if \(projectPart\) \{\s*parts\.push\(projectPart\);\s*\}\s*else if \(gitPart\) \{\s*parts\.push\(gitPart\);\s*\}/if (projectPart) parts.unshift(projectPart);\n    if (gitPart) parts.push(gitPart);/s;
' "$r/project.js"

# identity.js: context bar fixed at 7 cells
perl -pi -e 's/coloredBar\(percent, getAdaptiveBarWidth\(\), colors\)/coloredBar(percent, 7, colors)/' "$r/identity.js"

# usage.js: usage bars 7 cells, no weekly reset time
perl -0pi -e '
  s/const barWidth = getAdaptiveBarWidth\(\);/const barWidth = 7;/;
  s/resetAt: ctx\.usageData\.sevenDayResetAt,(\s*colors,\s*usageBarEnabled,\s*barWidth,\s*forceLabel: true,)/resetAt: null,$1/;
' "$r/usage.js"

grep -q 'parts.unshift(projectPart)' "$r/project.js" && grep -q 'gitPart = gitInner.join' "$r/project.js" \
  && grep -q 'coloredBar(percent, 7' "$r/identity.js" && grep -q 'resetAt: null' "$r/usage.js" \
  && grep -Eq 'const barWidth = 7' "$r/usage.js" \
  && echo "ok" || { echo "some patch did not apply — plugin source changed, patch by hand"; exit 1; }
