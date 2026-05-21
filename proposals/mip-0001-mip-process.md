# MIP-0001: Mesh Improvement Proposal Process

Status: Active
Type: Process
Scope: National
Author: Mesh maintainers
Created: 2026-05-17
Discussion: https://github.com/DutchMeshCore/mips/issues/1
Decision Deadline: 2026-05-31
Review Date:
Expiry Date:
Supersedes:
Superseded-By:

## Summary

Adopt a lightweight repository-based process for mesh decisions using Issues for ideas, Pull Requests for formal proposals, and Markdown files as a durable decision record.

## Motivation

Community decisions need a shared and transparent process that is simple enough to use regularly while still producing clear and reviewable outcomes.

## Proposal

Use the process defined in `PROCESS.md`, including:

- proposal types and scope levels,
- lifecycle and status transitions,
- 14-day standard decision window,
- 72-hour urgent window,
- rough consensus default with fallback voting,
- PullPact reaction voting on PR descriptions (see `PROCESS.md`).

## Impact

All participants can propose and review decisions with one public workflow. PullPact supplies visible vote counts on pull requests. Maintainers gain consistent rules for status handling and decision recording.

## Alternatives

- Ad-hoc chat decisions: fast but poor traceability.
- Maintainer-only decisions: low community trust and weak auditability.

## Rollout

Immediately apply this process to new proposals. Existing ad-hoc norms can be migrated incrementally as new MIPs are introduced.

## Compatibility

Requires the PullPact GitHub App and `.pullpact.yaml` for PR voting. No changes to mesh runtime software. Governance remains documentation-first with maintainer-recorded decisions.

## Decision

Outcome: Accepted, set to Active
Rationale: Provides a low-friction governance baseline with clear windows and accountability.
Effective Date: 2026-05-17
Unresolved Concerns: None

