# CCS task cycle

The owner supplies intent, constraints and acceptance. The agent resolves routine
implementation choices and carries authorized work through publication. Explicit
current instructions govern scope; repository rules provide the project defaults.

## 1. Establish the starting point

Record repository, branch, HEAD and worktree state. Read the current handoff and
only the canonical contracts relevant to this task. Do not overwrite unexpected
changes or assume that a previous chat's unpublished files still exist.

## 2. Make the task concrete

Use [TASK](../templates/TASK.md): goal, change, invariants, inputs, checks, non-goals
and done condition. Specify a model/effort only when the owner or environment has
an applicable policy; do not invent globally available model names or prices.
Missing information should block only the work that actually depends on it.

## 3. Implement and investigate

Keep changes coherent and bounded. Begin with short representative checks. On a
failure, capture the smallest useful evidence, form a falsifiable hypothesis and
correct the cause. Do not reset data, remove ownership checks or broaden retry
rules just to make a test green.

## 4. Review, then certify

Review the candidate diff before final expensive checks. Keep relevant source,
inputs and settings fixed. Apply [validation](VALIDATION.md), including native
release gates where applicable. Run a new full suite when material changes or a
required gate invalidate previous evidence, not after every unrelated docs edit.

## 5. Publish a reviewable result

Update the short [handoff](../templates/HANDOFF.md) and relevant documentation.
Stage task-owned files, commit one coherent revision, publish the feature branch
and create/update one PR. State exact head, checks, failures and limitations.
Publishing a PR does not by itself authorize merge or live deployment. A current
explicit authorization can approve those actions without another permission cycle.

## 6. Accept and integrate

Acceptance names an exact revision. Recheck remote head/base before integration.
For stacked PRs, inspect ancestry and merge the accepted dependency chain once;
avoid reapplying commits already included in the accepted head. Preserve useful
branches and evidence; deletion is a separate action.

A Draft-to-ready transition can itself trigger CI. Before integration, account for
ready-event and main-push gates in the budget; do not change accepted source just
to hide a redundant event. Configure project triggers deliberately for future work.

## 7. Capture the lesson

If the task exposed a transferable surprise, add a sanitized [case](../templates/CASE.md)
and follow [maintenance](MAINTENANCE.md). Keep project-specific reports in the
project. A general rule must state where it applies and where it does not.

See [CI economy](CI_ECONOMY.md) and [the case index](../cases/README.md).
