# Validation without repeated busywork

Sequence: implementation → focused checks/fixes → candidate review → final heavy
checks → publication. Exploratory runs are useful but are not final certification
when relevant inputs changed afterward.

## Evidence scope

| Evidence | Proves | Does not prove |
| --- | --- | --- |
| Diff/code review | Changes match inspected contracts | Runtime success |
| Offline tests | Tested inputs and platform behavior | Real service readiness |
| Native CI | Tested OS/interpreter/revision | Another OS, ARM or mobile behavior |
| Live qualification | The specific observed path and environment | Other failure modes |

Record source/revision, relevant inputs/settings, platform/interpreter, commands,
results and limitations. A skipped test is not PASS for its platform.

Reuse evidence when relevant identities are unchanged. Documentation edits do not
invalidate calculation tests. Changes to a crash fixture do invalidate its prior
result; repeat affected checks and required release gates. Do not start an extra
benchmark merely to populate a report.

Validate recovery through behavior: actual owned writer exits, a new process/session
starts, source identity is retained, and fresh usable progress advances. An accepted
signal, an empty error field or a process named running is insufficient.

Use [HANDOFF](../templates/HANDOFF.md) for the compact current state. Archive long
investigations; keep current decisions easy to find.
