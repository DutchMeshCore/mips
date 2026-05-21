# Mesh Improvement Proposals (MIP)

GitHub: [DutchMeshCore/mips](https://github.com/DutchMeshCore/mips)

This repository is the canonical home for Mesh Improvement Proposals.

MIPs are community proposals for decisions that affect mesh operations, standards, recommendations, and governance. The goal is simple: clear written decisions, public discussion, and a durable history.

The process works in both private and public GitHub repositories.

## Pull request governance

This repository uses [PullPact](https://pullpact.online) for reaction voting on pull requests. MIP decision windows, objections, and written outcomes are defined in [`PROCESS.md`](PROCESS.md#pullpact-and-mip). PullPact currently runs in **report-only** mode; maintainers merge after MIP gates are met.

[Install PullPact](https://github.com/apps/pullpact/installations/new) · [pullpact.online](https://pullpact.online)

## What belongs here

- Technical recommendations used across the mesh
- Operational and coordination rules
- Process changes for how the community decides
- Informational guidance and best practices

## What does not belong here

- MeshCore source code and implementation details
- Private moderation logs
- Sensitive security reports (see `SECURITY.md`)

## Proposal flow

1. Open an idea as an Issue.
2. Draft a proposal as a Pull Request.
3. Discuss and revise in public.
4. Move to Candidate when text is stable.
5. Decide after the decision window.
6. Merge into `proposals/` with final status and rationale.

## Repository layout

- `proposals/`: accepted or historical MIP documents
- `drafts/`: active draft proposals
- `templates/`: proposal and decision templates
- `.github/`: workflows, issue forms, and PR template

## Start here

- Process: [`PROCESS.md`](PROCESS.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
- Contributing guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Security disclosure: [`SECURITY.md`](SECURITY.md)

