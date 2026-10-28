# 001 — duplicated CI consumed an unexpected allowance

Date: 2026-10-28. Status: corrected workflow observed on a native Windows/Linux run.

## Symptom and evidence

A development project approached its hosted CI allowance while still iterating.
The retained run inventory contained 139 workflows and 59 revisions executed once
for push and once for a PR. Summed job execution did not equal the account's
allowance counter. These aggregate values describe one incident, not an expected
saving for every project.

## Mechanism and correction

A feature branch satisfied both triggers. The workflow also ran a desktop subset
alongside a full Windows suite that already included it. The correction restricted
push to main, retained PR code checks, classified docs-only updates, skipped the
redundant subset and added cancellation/cache controls. A new feature revision
produced one PR run and passed the requested Linux/Windows checks.

## Limits and resulting rule

Retained repository jobs cannot reconstruct unseen/deleted/account-wide usage.
Do not equate wall time, actual job seconds or an assumed OS multiplier with a
billing statement. Subsequent Draft-to-ready and main-push events are separate
integration costs and must be planned explicitly.

Apply [CI economy](../docs/CI_ECONOMY.md). Keep exact run IDs and billing exports in
the project rather than the public casebook.
