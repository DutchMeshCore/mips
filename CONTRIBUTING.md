# Contributing

Thank you for helping improve mesh decision making.

## Before you open a proposal

1. Check existing proposals in `proposals/`.
2. Search open issues and pull requests.
3. Open an idea issue if the topic is new.

## Proposal submission flow

1. Open an issue using the idea template.
2. Copy `templates/proposal-template.md` into a new draft file under `drafts/`.
3. Open a PR with the `WIP` label and link the idea issue.
4. Respond to feedback and keep sections current.
5. Vote on the **PR description** with `+1`, `-1`, or `eyes` when maintainers open the decision window (see [`PROCESS.md`](PROCESS.md#pullpact-and-mip)).
6. When stable, ask maintainers to mark it `Candidate` (they remove `WIP` and start the window).

## Writing guidance

- Keep scope narrow and explicit.
- Explain who is affected.
- Include alternatives considered.
- Include rollout and migration notes if applicable.
- Prefer clear tradeoffs over long narratives.

## Objections and review quality

When objecting, include:

- specific risk,
- expected impact,
- suggested mitigation or alternative.

## Status and merge

- PullPact records votes on the PR description; maintainers merge after the decision window and a written `Decision` section (see [`PROCESS.md`](PROCESS.md#merge-requirements)).
- Accepted proposals move to `proposals/` with numbered filename.
- Rejected or withdrawn proposals remain discoverable with clear status and rationale.
- Superseded proposals must reference the replacement proposal.

