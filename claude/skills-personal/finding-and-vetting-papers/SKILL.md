---
name: finding-and-vetting-papers
description: Use when searching for academic papers to cite, and especially when picking a "main reference" or anchor citation for a thesis/paper — checks whether a candidate is only an arXiv/preprint or has actually been peer-reviewed before treating it as authoritative.
---

# Finding and Vetting Papers

## Overview
Web search treats arXiv preprints and peer-reviewed publications as equally citable. They are not equally authoritative. This skill exists to prevent anchoring a thesis's core contribution to a paper that turns out to be an unreviewed preprint.

## When to use
- Searching literature for a new research direction
- Picking a "main reference" / anchor citation that a thesis's contribution builds on or differentiates from
- A candidate paper only exists on arXiv, ResearchGate, or a lab GitHub page
- Re-checking existing references before a thesis defense/submission

## Reference tiers

| Tier | Use as | Don't use as |
|---|---|---|
| Peer-reviewed — acceptance verified on the venue's own page or a DOI | Main/anchor reference, differentiation baseline | — |
| arXiv/preprint, no verified acceptance | Supporting citation, coverage of a fast-moving field, "concurrent work" | Main/anchor reference the core contribution is measured against |
| Preprint that claims "to appear at X" | Unverified until independently confirmed | Citing the claimed venue as fact |

## Verification steps

1. Search `"<title>" <suspected venue> accepted` (e.g. `"AgentSpec" ICSE 2026 accepted`)
2. Confirm on the venue's own site (conf.researchr.org, ndss-symposium.org, usenix.org, dl.acm.org, ieeexplore) or a DOI — not the arXiv listing text or the paper's own abstract
3. No independent confirmation after a couple of searches → treat as preprint-tier and say so explicitly, don't assume peer review

## Recency

Age matters or doesn't depending on what the citation is *for*, not a fixed cutoff:

| Citation's role | Recency rule |
|---|---|
| Describing the current state of the art (what attacks/defenses/systems exist now, how the field looks today) | Prefer the last ~2 years in fast-moving fields (e.g. LLM agent security) — an older source here misrepresents the current landscape |
| Foundational method, original definition, or a technique that's still the standard way to do something | Age is irrelevant — cite the canonical/original source regardless of date |

If unsure which bucket a citation falls in, ask: "if this paper were replaced by this year's equivalent, would the sentence it supports still say the same thing?" Yes → foundational, age doesn't matter. No → it's a SOTA claim, prefer recent.

## Swapping in a more authoritative reference

- Check topical overlap first: does the new paper already solve the gap your contribution claims to fill? If yes, the novelty claim needs to change, not just the citation.
- Keep the original preprint as a supporting citation if still relevant — demote it, don't discard it.

## Workflow

1. WebSearch for candidates
2. Tier each candidate (table above)
3. Run verification steps on anything being considered as a main reference
4. Import to Zotero via `zotero_add_items_by_identifier`; tag or collection by tier (`preprint` vs `peer-reviewed`) so the tier stays visible later

## Common mistakes

- Trusting arXiv's subject listing or the abstract's "to appear at X" as proof of acceptance — verify independently
- Treating "well-cited on arXiv" as equivalent to peer review
- Discarding a preprint entirely instead of demoting it to supporting reference
- Swapping in a new main reference without re-checking topical overlap — can silently invalidate the novelty claim
