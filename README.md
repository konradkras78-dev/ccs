# CCS — a development workflow that learns from real cases

CCS is a practical agreement between a project owner and a coding agent: carry one
bounded task from an explicit starting point to a reviewable result, retain the
reasoning that matters, and spend validation resources deliberately.

[Українською](README.uk.md)

## Start here

1. Read [the workflow](docs/WORKFLOW.md).
2. Adopt [the project agreement](templates/PROJECT_ADOPTION.md) in your repository.
3. Open a task with [the task template](templates/TASK.md).
4. Apply [validation rules](docs/VALIDATION.md) and [CI economy](docs/CI_ECONOMY.md).
5. Record a transferable surprise as a [case](templates/CASE.md), then update the
   applicable rule through [the maintenance process](docs/MAINTENANCE.md).

## What belongs here

- General rules, reusable templates and evidence-backed case studies.
- Cases that explain a failure mechanism, its limits and the resulting rule.
- A small [case index](cases/README.md), including unsuccessful hypotheses when
  they help the next developer avoid the same mistake.

Project code, credentials, production addresses, source identities, runtime logs
and account billing details remain in their project. Existing project instructions
remain effective until explicitly updated; this repository never silently changes
other repositories or authorizes deployment.

## Working principles

- One task, one coherent change, one reviewable revision.
- Facts, hypotheses, accepted decisions and future plans are distinct.
- Reuse valid evidence; rerun checks when relevant inputs actually change.
- Local, CI, native and live results have different scopes.
- Preserve ownership and history before automating recovery or migration.
- Optimize duplicate work before removing useful checks.

Run `python3 scripts/check_docs.py` for lightweight local document checks.
The repository's own CI checks documentation only; application CI examples must be
adapted to each project's real release gates.
