# CI economy

Optimize duplicated work before cutting release assurance. CI usage, account
allowance, cache storage and the wall time of one workflow are separate measures.

## Four defaults to adapt

1. Feature revisions use a PR workflow; main pushes have their own integration
   gate. Avoid running a complete feature matrix for both push and PR.
2. Keep one full automatic baseline platform. Use focused secondary-platform checks
   where appropriate; require complete native evidence for native-sensitive changes
   and accepted cross-platform releases. A full suite already includes its subset.
3. Make documentation-only revisions light. Classify immutable event ranges and
   fail closed when the range is unknown. Executable examples/config changes can be
   code even under docs. A docs-only green result never erases a failing code gate.
4. Cancel obsolete revisions with branch concurrency. Cache bounded dependency
   downloads/build outputs by OS/interpreter/lockfile; never runtime environments,
   credentials or private data. Budget cache storage separately.

Trigger policy is branch-versioned. Editing one branch's workflow does not update
older branches or account settings. Ready-for-review and post-merge events can add
runs even when the tested head did not change. Plan those integration gates too.

## Before a rerun

Inspect the failed job, reproduce the smallest relevant case and identify a cause
or a changed external condition. Then publish the correction or rerun only the
justified failed job. Put a known cheap regression before the expensive suite.

Do not create SHA-only commits. Record publication and CI observations in PR metadata
when that avoids triggering another identical revision.

## Forecast honestly

Inventory retained runs and every job attempt, not just successful workflows.
Separate actual runner seconds, rounded job minutes and account billing units.
Other repositories, deleted runs, tariffs and billing delay can prevent reconciliation.
Use the account's current usage counter for remaining allowance and keep a reserve;
state assumptions rather than promise an exact completion date.

Git hosting and CI execution can be separate. Investigate a dedicated runner or
external CI before migrating repository history and PRs. An actor switch does not
necessarily change which owner pays. Date provider quotas; verify current terms
when making a provider decision instead of freezing them into this workflow.

[Duplicate-run case](../cases/001-duplicate-ci-and-billing.md)
