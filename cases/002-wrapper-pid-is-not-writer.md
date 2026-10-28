# 002 — a wrapper's PID was not the resource owner's PID

Date: 2026-10-28. Status: two related paths observed; limits differ by platform.

## Symptoms

On a mobile Linux userspace, SIGTERM to the runtime leader was accepted but ignored
by its PRoot wrapper; the real writer continued. A separate Windows crash fixture
sometimes reopened SQLite after killing/waiting for a virtual-environment launcher
and observed active-writer or IO failures.

## Evidence and correction

The mobile process tree identified a wrapper ignoring SIGTERM and a descendant
holding the writer lock/database. A controlled signal to that verified writer
produced a new supervised session and advancing usable samples.

The old Windows fixture did not record the writer PID. CPython's Windows venv
redirector creates a child process and waits for it; terminating the redirector is
not waiting for that child's termination. This is a source-supported explanation
for the historical race, not a retrospective proof of its missing process tree.

The corrected synthetic fixture launches the base interpreter with explicit local
source, reports os.getpid(), asserts it equals Popen.pid before kill, waits for the
actual writer, and closes pipes. The isolated regression and full native Windows
suite passed. Production locks/retries were not relaxed.

## Resulting rule and limits

Before signals, verify current PID, start identity, ancestry/group and owned lock
as appropriate to the platform. Never select a process by an old PID/name alone.
After recovery, require fresh advancing data and unchanged source identity.
Graceful exit does not qualify hard crash, supervisor death, whole app death or
reboot. A bounded sleep is not a substitute for proving the target process.

Primary reference: [CPython v3.13.9 redirector](https://github.com/python/cpython/blob/v3.13.9/PC/venvlauncher.c).
[Validation scopes](../docs/VALIDATION.md)
