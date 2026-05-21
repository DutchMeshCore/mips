# Governance

This repository is governed by community process, public discussion, written decisions, and [PullPact](https://pullpact.online) voting on pull requests. See [`PROCESS.md`](PROCESS.md#pullpact-and-mip) for how MIP and PullPact fit together.

## Governance Principles

- Openness by default
- Clear written rationale
- Process neutrality by maintainers
- Practical, low-friction participation
- Respect for regional operational realities

## Maintainers

Maintainers are process stewards. They are responsible for:

- triaging issues and proposal PRs,
- ensuring templates and required fields are complete,
- assigning proposal numbers,
- managing status labels (`WIP`, `status:candidate`, `emergency`, and related),
- coordinating PullPact voting windows (remove `WIP` only when a decision window starts),
- recording decision outcomes consistently.

Maintainers are not sole decision makers on technical outcomes.

## Maintainer Actions

Maintainers may:

- label proposals and update status metadata,
- request revisions for process completeness,
- start or extend decision windows,
- summarize consensus state and final outcomes,
- merge proposal PRs when MIP gates are met (PullPact is in report-only phase until automated merge is enabled in `.pullpact.yaml`).

Maintainers must not:

- merge accepted proposals without a written decision summary,
- bypass decision windows except emergency path defined in `PROCESS.md`,
- remove `WIP` before a proposal is `Candidate` and its decision window should begin,
- hide unresolved objections from decision records.

## Adding Maintainers

New maintainers are added through a proposal or consensus in a governance issue.

Suggested criteria:

- demonstrated constructive participation,
- consistent review activity,
- trusted by operators across different regions.

## Removing Maintainers

Removal may occur for inactivity, repeated process violations, or conduct issues.

Process:

1. public concern raised in governance issue,
2. evidence and response window,
3. decision recorded by remaining maintainers with rationale.

## Conflict Handling

When maintainers disagree on process outcome:

1. document disagreement in the relevant PR or issue,
2. request one extra maintainer review,
3. if still unresolved, use fallback vote and record rationale.

## Transparency Requirements

- Use public issues and PRs for proposal work.
- Keep decision rationale in proposal documents.
- Keep administrative actions auditable through labels, comments, and merges.

