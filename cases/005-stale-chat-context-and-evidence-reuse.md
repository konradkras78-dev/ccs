# 005 — a resumed chat did not have its unpublished candidate

Date: 2026-10-28. Status: repository-based recovery and revalidation completed.

## Symptom and evidence

A resumed environment contained an older checkout while the chat described an
unpublished implementation. Current Git state, available files and remote heads
were checked before continuing. The missing candidate could not be treated as a
reviewed or persisted result.

## Correction

Recover the exact published baseline and accepted contract, reconstruct only the
missing task-owned work, review the candidate and revalidate relevant behavior.
Keep one short current handoff; archive long investigation history. Record source
and platform identities alongside results.

A later docs-only change can reuse unchanged calculation/browser evidence. A
change to a crash fixture requires new fixture evidence and applicable gates.
Recording an observed CI result in PR metadata avoids an otherwise pointless
SHA-only commit and another identical CI run.

## Resulting rule and limits

The repository checkpoint is authoritative for what exists; chat supplies intent
and decisions, not proof that a file or check survived. Do not restore protected
configuration just to fill an unrelated source checkout. Reuse evidence based on
relevant source/inputs/platform, not the mere presence or absence of a new commit.
[Handoff template](../templates/HANDOFF.md)
