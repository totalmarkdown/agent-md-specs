# Governance

> Living document. Last updated 2026-04-18. Changes happen via PR
> against this file with the `governance` label. Substantive changes
> require a 14-day public comment window.

## Current Status

agent-md-specs is currently maintained by TotalMarkdown.ai. As the
project matures and gains community adoption, governance will evolve
toward a more formal structure (see "Future Governance" below).

All contributions are CC0 1.0 Universal (public domain). No CLA is
required, but contributors must sign off commits under the Developer
Certificate of Origin — see "DCO" below.

## How Specs Are Managed

### Proposing a New Spec (Extended Tier)

1. Open a GitHub Discussion in the ["Ideas" category](https://github.com/totalmarkdown/agent-md-specs/discussions/categories/ideas).
   Include: spec name, category, purpose, at least 2 real-world use cases.
2. Community discussion period: 14 days minimum.
3. If accepted, file an Issue using the "Spec proposal" template, then
   submit a PR following the spec template format.
4. Maintainer merges after validation passes and 1 approval.

### Modifying an Existing Spec (Extended Tier)

1. Open a GitHub Issue describing the proposed change, or link to an
   existing Discussion.
2. Submit a PR referencing the Issue.
3. Maintainer merges after validation passes and 1 approval.

### Core Tier Changes — RFC Process

Changes to Core tier specs (47 specs) require the **RFC process**:

- **New Core spec** (including Extended → Core promotion)
- **Breaking change** to a Core spec's frontmatter or required fields
- **Core → Extended demotion** or **Deprecation**
- **Draft → Proposed** or **Proposed → Stable** promotion

Process:

1. **File an RFC issue** using the "Core spec RFC" template. Title
   format: `RFC: [change description] for [SPEC.md]`.
2. **Review period** — 14 days minimum for Proposed stage, 30 days for
   Stable. No merge before the window closes, regardless of approvals.
3. **Approval threshold** — 2 maintainer approvals + no unresolved
   blocking objections. Blocking objections must cite a specific
   problem; style preferences are non-blocking.
4. **Implementation PR** — references the RFC issue.
5. **Decision logged** in the RFC issue close comment, referencing the
   merged PR and the review window.

See [SPEC_LIFECYCLE.md](./SPEC_LIFECYCLE.md) for the full lifecycle.

### Spec Tiers

- **Core** — essential specs recommended for all production agents (47 specs).
- **Extended** — valuable specs for specific use cases (132 specs).

See [Discussion #17 — Core/Extended boundary criteria](https://github.com/totalmarkdown/agent-md-specs/discussions/17)
for the live debate on tier-promotion rules.

### Versioning

- Individual specs use semver in their YAML frontmatter (`spec_version`).
- The library itself is versioned by volume (Vol 1-16) combined with
  semantic releases (current: v1.3.0).
- Breaking changes to Core specs require a new major version plus a
  migration guide.

## Developer Certificate of Origin (DCO)

Every commit must be signed off with `git commit -s`, which appends:

```
Signed-off-by: Your Name <your.email@example.com>
```

By signing off, you attest that:

> (a) The contribution was created in whole or in part by you and you
> have the right to submit it under the CC0 1.0 Universal license; or
> (b) the contribution is based on previous work that is covered by an
> appropriate open-source license and you are authorized to submit it
> under that license; or
> (c) the contribution was provided directly to you by some other
> person who certified (a), (b), or (c) and you have not modified it.

This is the same DCO used by the Linux Foundation, Apache, and most
CNCF projects. No separate CLA is required.

## Technical Steering Committee (TSC)

### Today

- **1 seat** — `@totalmarkdown` (founding maintainer).

### Target (by Q4 2026)

- **5 seats** — founding maintainer + 4 external members representing:
  security / identity (e.g. SPIFFE, OIDC, IAM background), compliance
  (GDPR / HIPAA / SOC 2 background), multi-agent frameworks (LangChain,
  CrewAI, AutoGen, or equivalent), and a community-representative seat.
- **Term length** — 2 years, renewable. Staggered so no more than 3
  seats turn over in a single year.

### Nomination process

1. Anyone may nominate a candidate via an Issue labeled
   `tsc-nomination`. Self-nominations welcome.
2. Include: candidate's public GitHub handle, relevant expertise, and
   why they'd be a good fit for one of the target seats.
3. The sitting TSC reviews within 14 days. Seat is filled by majority
   vote of existing TSC members; ties go to the founding maintainer
   until the committee reaches 3 members.
4. The nominee must accept the seat publicly via a comment on the
   nomination issue.

### TSC responsibilities

- Approve Core-tier RFC merges (2 approvals required).
- Resolve blocking-objection disputes that can't be settled in the RFC
  thread.
- Approve foundation-hosting or ownership-transfer decisions.
- Publish a public meeting cadence once the TSC has 3+ members.

### Conflict of interest

TSC members must disclose financial or employment relationships that
could influence their decisions. Any member may recuse from a specific
decision. Disclosures go in a `TSC.md` file (to be created when the
TSC has 2+ members).

## Succession and Bus-Factor

If TotalMarkdown.ai ceases maintenance:

1. The sitting TSC assumes stewardship automatically.
2. If no TSC exists, the project enters a 90-day hibernation window.
   Any GitHub user with ≥3 merged PRs may propose a continuation plan
   via a public Issue.
3. If no credible continuation plan emerges in 90 days, the repo is
   archived with a pointer to the latest community fork.

Because all content is CC0 public domain, forks are always permitted
and require no permission.

## Naming and Trademark Policy

"agent-md-specs" is descriptive and not claimed as a trademark.
Third parties may freely use the name in references, blog posts, and
derived works. For name-clash clarity:

- **Forks** should use a distinguishing qualifier (e.g.
  `yourorg/agent-md-specs-enterprise`, not
  `yourorg/agent-md-specs`). This is a courtesy request, not a legal
  requirement.
- **Derived specifications** should use their own file names (not
  re-use the names of existing specs) to avoid confusion.
- **Claiming endorsement** from TotalMarkdown.ai or the TSC requires
  written agreement.

## Security Reviewer

Security vulnerability reports go to `security@totalmarkdown.ai` (see
[SECURITY.md](./SECURITY.md)). Because this is currently a
single-point-of-failure contact:

- The TSC, once seated, will appoint a second security contact.
- Reports are acknowledged within 48 hours; if no acknowledgement
  within 72 hours, reporters may escalate via a private email to any
  TSC member.

## Decision Log

Substantive governance decisions are recorded as GitHub Issues with
the `governance` label. Closed governance issues form the project's
decision log. For a machine-queryable list:

```
gh issue list --repo totalmarkdown/agent-md-specs \
    --label governance --state all --limit 200
```

Historic decisions (before the `governance` label existed) are noted
in [CHANGELOG.md](./CHANGELOG.md).

## Future Governance

As adoption grows, we intend to:

- **Seat the TSC** — target 3 external members by end of Q3 2026.
- **Formalize the RFC process** — publish RFC-0001 describing RFC
  numbering and lifecycle (see [ROADMAP.md](./ROADMAP.md)).
- **Evaluate foundation hosting** — LF AI & Data, OpenSSF, AAIF, or
  CNCF Sandbox. Decision target: end of Q4 2026.
- **Seek alignment** with AAIF, NIST AI Agent Standards Initiative,
  and ISO/IEC JTC 1/SC 42.
- **Accept nominations** for spec category maintainers once the TSC is
  seated.

## Contact

- GitHub Discussions: <https://github.com/totalmarkdown/agent-md-specs/discussions>
- Governance issues: <https://github.com/totalmarkdown/agent-md-specs/issues?q=label%3Agovernance>
- Code of Conduct violations: `conduct@totalmarkdown.ai`
- Security: `security@totalmarkdown.ai`
- Maintained by: [TotalMarkdown.ai](https://totalmarkdown.ai)

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
