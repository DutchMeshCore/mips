# MIP Process

This document defines how Mesh Improvement Proposals are created, discussed, and decided.

## Purpose

The MIP process gives the community a lightweight and transparent way to make shared decisions and keep a durable record of why those decisions were made.

## Roles

- **Author**: writes and updates the proposal.
- **Contributors**: review, discuss, and raise objections.
- **Maintainers**: keep process quality, labels, numbering, and decision records consistent.

Maintainers administer the process. They do not unilaterally set technical outcomes.

## Proposal Types

- `Standard`: technical and interoperability recommendations.
- `Operational`: operations, coordination, moderation, onboarding, docs.
- `Informational`: guidance without a binding decision.
- `Process`: changes to this process.

## Scope Levels

- `National`: intended for wide mesh use within a country or national community.
- `Regional`: specific region, city, or operator group.
- `Experimental`: trial with explicit review date or expiry.
- `Recommendation`: preferred default, not mandatory.

## Proposal Lifecycle

1. **Idea** (Issue): problem statement and early options.
2. **Draft** (PR): structured proposal using the template.
3. **Discussion** (PR): active revision and tradeoff analysis.
4. **Candidate** (PR label + status update): stable text, ready for decision.
5. **Decision window**: fixed period where objections and final support are gathered.
6. **Accepted / Rejected / Withdrawn**: outcome recorded with rationale.
7. **Active / Superseded**: lifecycle updates after acceptance.

## Promotion Rules

### Idea to Draft

A proposal should move from Issue to Draft PR when:

- the problem is clear,
- the scope is identified,
- at least one implementation direction exists.

### Draft to Candidate

A proposal may be marked `Candidate` when:

- template fields are complete,
- open questions are either resolved or explicitly listed,
- there are no unresolved blocking feedback threads in the PR.

Only maintainers may apply `status:candidate`.

When marking `Candidate`, maintainers also remove the `WIP` label so PullPact can evaluate votes during the decision window. See [PullPact and MIP](#pullpact-and-mip).

## Decision Windows

- **Standard window**: 14 days from the moment the proposal is marked `Candidate`.
- **Urgent window**: 72 hours for time-sensitive operational or safety needs.

The decision window starts only after:

- `Status: Candidate` is present in the proposal text,
- the PR has `status:candidate` label,
- maintainers post a short "decision window started" comment with start and end timestamps.

Window extensions are allowed when substantial new information appears late in the window.

## Consensus Rules

Default decision method is rough consensus.

A proposal is accepted when:

- there is clear support from participants involved in the affected scope,
- objections were addressed in writing,
- no unresolved serious objection remains.

## Serious Objection Criteria

A serious objection must explain at least one of:

- legal or regulatory risk,
- interoperability breakage,
- major reliability degradation,
- unreasonable operational burden,
- unacceptable migration risk for current operators.

Unsupported disagreement without impact analysis is not a serious objection.

## PullPact And MIP

This repository uses [PullPact](https://pullpact.online) for pull request voting. PullPact and the MIP process work together:

- **PullPact** counts reactions on the PR description and updates a PullPact check. Thresholds are in [`.pullpact.yaml`](.pullpact.yaml).
- **MIP process** runs decision windows, handles serious objections in writing, and requires a recorded `Decision` section before merge.

### Voting

- Vote on the **pull request description** using `+1`, `-1`, and `eyes` as configured in `.pullpact.yaml`.
- Reactions on review comments or PullPact comments do not count.
- Use PR discussion for technical detail and serious objections.
- Maintainers may run a **fallback vote** in PR comments when reaction counts are unclear or disputed.

### Labels And Automation

- Authors add `WIP` to proposal PRs in **Draft**. PullPact pauses while `WIP` or `DONTMERGE` is present.
- Maintainers remove `WIP` only when marking **Candidate** and starting the decision window.
- Do not remove `WIP` early to gather votes on unstable text.

### PullPact Phase: Report Only

`resolution.on_pass` is `report`. PullPact shows vote results but does not merge PRs. Maintainers merge manually after all [merge requirements](#merge-requirements) are met.

### PullPact Phase: Automated Merge (optional)

Maintainers may later set `resolution.on_pass` to `merge` when contributors are used to reaction voting. Rules then include:

- `merge_cooldown_hours` (336) matches the standard 14-day decision window.
- Maintainers post the decision summary and update the proposal `Decision` section before removing `WIP`.
- **Emergency** proposals: maintainers merge manually per [Emergency Path](#emergency-path). Do not rely on PullPact alone for urgent timing.

### Merge Requirements

Before a proposal PR merges to `main`:

1. Outcome decided (`Accepted`, `Rejected`, or `Withdrawn`) with rationale in the `Decision` section.
2. Applicable decision window completed, or emergency path followed.
3. PullPact check reflects passing thresholds for the active voting period (no `WIP` during the window).
4. Maintainers assign the final `mip-NNNN` filename and place accepted text under `proposals/` when applicable.

## Fallback Voting

Use PR description reactions as the default signal. If rough consensus is unclear, maintainers may call an explicit vote in the PR with options:

- `Yes`
- `No, with reason`
- `Abstain`
- `Block, with technical or operational reason`

`Block` requires written rationale. Maintainers can only overrule `Block` with a recorded explanation in the decision summary.

## Decision Summary Requirement

Before merge or closure, maintainers must post and copy into the proposal `Decision` section:

- outcome (`Accepted`, `Rejected`, `Withdrawn`),
- effective date,
- concise rationale,
- unresolved concerns, if any,
- rollout expectations or next review date.

## Regional And Experimental Guardrails

Regional or experimental proposals must not be represented as national defaults unless explicitly superseded by a national proposal.

Experimental proposals must include one of:

- `Review Date: YYYY-MM-DD`
- `Expiry Date: YYYY-MM-DD`

At review or expiry, maintainers update status to `Accepted`, `Active`, `Superseded`, `Withdrawn`, or `Rejected`.

## Emergency Path

Emergency proposals are allowed for immediate safety, legal, or severe operational risk.

Rules:

- use `status:candidate` and `emergency` labels,
- 72-hour urgent window,
- clear temporary mitigation language,
- mandatory public follow-up review within 30 days,
- maintainers merge manually; PullPact does not shorten the emergency window.

Emergency outcomes may be reverted by follow-up review if evidence changes.

## Numbering And Filenames

- Final format: `mip-0001-short-title.md`
- Draft format: `mip-draft-short-title.md`
- Maintainers assign and confirm final numbers at merge.

Numbers are never reused.

## Superseding

When a proposal replaces another:

- update old proposal status to `Superseded`,
- add `Superseded-By: MIP-XXXX`,
- add reciprocal reference in the new proposal.

