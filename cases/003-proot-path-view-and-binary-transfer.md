# 003 — the same file had different native and guest path views

Date: 2026-10-28. Status: consistent-runtime binary probe, transfer and restore passed.

## Symptom and evidence

A consistent SQLite backup was created inside an Ubuntu PRoot runtime. Native host
checks rejected its apparent symlink, while guest lstat/open reported a regular
file. Following one known alias still encountered a second refused path component.
The differing filesystem views were the important evidence; neither view alone
proved malicious substitution or archive corruption.

## Correction

Use the same reviewed runtime to create, verify and stream the archive. Before
creating a fresh archive, verify the binary channel with a small deterministic
payload through exactly that path. Keep stderr separate, use no PTY, stream bytes
without text decoding, compare size and digest, and restore/verify a fresh copy.
Do not repeatedly copy stale archives while changing unrelated assumptions.

## Resulting rule and limits

Path checks belong to a specified filesystem view. Do not globally permit symlinks
or remove no-follow protections in response to one compatibility problem. Select a
consistent adapter with explicit validation. Prefer SQLite's backup facility for a
live database; preserve source collection and prior backups.

This qualifies the tested capture/transfer/restore path only; it does not approve
arbitrary alias resolution or every host/guest filesystem combination.
[Workflow](../docs/WORKFLOW.md)
