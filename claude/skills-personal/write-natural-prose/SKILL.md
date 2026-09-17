---
name: write-natural-prose
description: Draft, rewrite, and edit natural, context-specific prose with a credible authorial voice while preserving factual accuracy. Use for reports, essays, academic writing, business documents, emails, articles, narratives, and other prose when the user asks to reduce formulaic AI-like writing, avoid templated structure, match a document type or personal style, or make text sound more natural. Do not use to evade AI detection or misrepresent authorship.
---

# Write Natural Prose

Produce clear, natural prose whose voice, structure, and level of formality fit the document and its audience. Improve writing quality without fabricating identity, experience, evidence, or imperfections.

## Core principles

- Preserve the user's meaning, factual claims, uncertainty, and constraints.
- Adapt vocabulary, tone, pacing, structure, and degree of formality to the document type, audience, purpose, and language variety.
- Retain concrete context: names, dates, examples, mechanisms, constraints, stakes, and causal links that are supported by the source material.
- Prefer specific verbs and claims over generic praise, filler, and vague abstractions.
- Vary sentence length and paragraph rhythm when it improves readability. Allow natural asymmetry, but keep grammar and logic correct.
- Build paragraphs around the needs of the argument, not a repeated template. Let paragraph length vary with content.
- Use transitions only when the relationship between ideas needs signaling. Prefer explicit logical connections over stock phrases.
- Preserve an established authorial voice. When no voice sample exists, infer a restrained, credible voice from the task rather than inventing a persona.
- Treat factual accuracy, verifiability, and attribution as higher priorities than stylistic naturalness.

## Workflow

1. Identify the document type, audience, purpose, desired effect, language variety, length, and any supplied voice samples.
2. Extract non-negotiable facts, quotations, citations, terminology, claims, and formatting constraints. Mark missing information instead of filling it with invention.
3. Choose a fitting register and structure. Determine which ideas deserve emphasis, which can be compressed, and which need concrete support.
4. Draft or revise at the level of meaning first. Remove generic openings, canned transitions, repetitive framing, and conclusions that merely restate prior sentences. Cross-check against `references/checklist.md` for concrete phrase-level tells (Chinese and English) — hit phrases get replaced locally, not rewritten wholesale.
5. Edit for voice and rhythm. Vary syntax naturally, replace abstract filler with supported specifics, and break unnecessary symmetry without forcing quirks.
6. Verify fidelity. Check every name, number, date, quotation, citation, and source-dependent claim against provided or verified material.
7. Run the final checklist. If essential context is unavailable, state the gap or use a clearly labeled placeholder.

When rewriting, do not change the author's position or strengthen weak evidence silently. If a substantial structural change could alter emphasis, briefly disclose it with the result.

## Prohibited practices

- Do not claim, promise, or optimize for bypassing AI detectors. Do not use detector scores as a quality standard.
- Do not fabricate personal memories, firsthand experience, emotions, credentials, interviews, quotations, citations, sources, data, or research findings.
- Do not insert misspellings, grammar errors, false starts, contradictions, fake uncertainty, or random irregularities to imitate a human.
- Do not disguise plagiarism, remove required attribution, or misrepresent authorship.
- Do not add unsupported specificity. Concrete detail must come from the user, source material, common knowledge appropriate to the task, or verified research.
- Do not mechanically vary words or sentence lengths. Variation must serve meaning, emphasis, or readability.
- Do not force every section into equal length, every paragraph into topic-support-summary form, or every point into a three-part list.
- Do not append a generic summary, moral, outlook, or call to action unless the genre and purpose call for one.

## Document-type rules

### Academic writing

- Prioritize precision, traceable reasoning, cautious claims, stable terminology, and consistent citation style.
- Distinguish evidence, interpretation, inference, and speculation.
- Preserve discipline-specific conventions and define specialized terms when the audience requires it.
- Never invent references. Flag incomplete bibliographic data and unsupported claims.
- Avoid ornamental variation when repetition is needed for technical clarity.
- The motivation→method→result shape of an abstract is a genre convention, not an AI tell — don't break it. But don't let a source draft's empty framing openers ("本研究旨在探討X", "This paper aims to explore X") survive a rewrite either: cut the frame and lead directly with the concrete gap, finding, or mechanism, without adding any claim the source didn't make.

### Business reports and proposals

- Lead with the decision, finding, risk, or requested action when appropriate.
- Tie claims to evidence, operational impact, ownership, timing, and constraints.
- Use headings and lists only when they improve scanning or decision-making.
- Avoid inflated claims, empty strategic language, and conclusions that repeat the executive summary.

### Emails and workplace messages

- Make the purpose, relevant context, requested action, owner, and timing easy to find.
- Match the relationship and stakes: concise for routine coordination, more explicit for sensitive or consequential topics.
- Avoid ceremonial openings, excessive politeness, and redundant closing summaries.

### Essays, commentary, and articles

- Establish a clear angle rather than a generic topic introduction.
- Develop ideas through concrete examples, observed tensions, evidence, or consequences.
- Allow pacing and paragraph shape to follow the argument. Avoid predictable thesis-three-points-recap structure unless it genuinely fits.
- End on the last necessary insight, implication, or unresolved question rather than a mechanical recap.

### Personal statements and first-person writing

- Use only experiences, motives, and reflections supplied by the user.
- Ask for or mark missing personal details that are essential to credibility.
- Preserve the user's level of confidence and emotional register; do not manufacture vulnerability or epiphanies.

### Creative and narrative prose

- Maintain point of view, tense, character knowledge, and setting continuity.
- Prefer scene-specific detail and purposeful rhythm over generic atmosphere.
- Use stylistic irregularity deliberately and consistently, not as camouflage.

### Technical and instructional writing

- Optimize for correctness, sequence, prerequisites, edge cases, and unambiguous terminology.
- Keep repeated terms when synonym substitution could confuse readers.
- Use steps, tables, or lists when the task is genuinely procedural or comparative.

## Final checklist

- [ ] Does the register fit the document, audience, purpose, and locale?
- [ ] Are the main point and logical relationships clear without stock transitions?
- [ ] Does each paragraph earn its place and follow the content rather than a template?
- [ ] Are sentence lengths and structures varied for meaning rather than artificially randomized?
- [ ] Have vague claims, filler, overstatement, and redundant summaries been removed?
- [ ] Are concrete details supported by the user, source material, or verified research?
- [ ] Are facts, names, dates, numbers, quotations, and citations accurate and consistent?
- [ ] Is the author's supplied voice preserved without inventing a persona or experience?
- [ ] Are headings and lists used only where they improve comprehension?
- [ ] Does the ending perform a real function instead of merely announcing or repeating a conclusion?
- [ ] Could any wording imply false authorship, fabricated evidence, or detector evasion? If so, revise it.
