# 004 — a short observation gap invalidated an entire hour

Date: 2026-10-28. Status: revised product policy implemented and offline/native-CI
validated; live device deployment is a separate gate.

## Symptom and evidence

After a brief acquisition restart, shorter recent intervals were usable but the
latest hourly interval was unavailable for every asset. Replay reproduced the
result: strict completeness inside the hour, not a reset of all historical data,
caused the difference between timeframes.

## Decision and correction

The product owner accepted an exploratory observed-flow view: an interval with at
least 50% nominal observed time may be displayed with its coverage. Fully missing
or mostly missing intervals remain unavailable. The threshold is a product decision,
not a universal statistical rule.

Missing observation is not an invented zero movement. Preserve raw observations,
compute only supported adjacent movements, and do not bridge a gap/restart as if
its unseen path were known. Keep coverage, observed token totals and historical
price readiness separate. Unpriced nonzero movement must not become monetary zero.

## Resulting rule and limits

Discuss what the product needs to infer before imposing acquisition perfection.
Distinguish incomplete observation, unusable calculation, insufficient historical
baseline and missing valuation. Preserve the ability to audit them independently.
Data interpolation and historical truth are separate choices and need explicit
approval; no threshold restores activity that was never observed.
[Validation](../docs/VALIDATION.md)
