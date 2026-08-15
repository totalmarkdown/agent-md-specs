<!--
Thanks for contributing to agent-md-specs. Please fill in the sections
below so we can review your PR quickly. PRs with unchecked boxes will
be held until the checklist is complete.
-->

## Summary

<!-- One-paragraph description of what this PR does and why. -->

## Related Issue or RFC

<!-- Link: Fixes #123, or "RFC: <title> — #456" -->

## Type of change

- [ ] Bug fix (existing spec / schema / doc correction)
- [ ] New Extended-tier spec
- [ ] Core-tier change (requires RFC — linked above)
- [ ] Documentation only
- [ ] CI / workflow / tooling
- [ ] Other (describe):

## Checklist

- [ ] I have read [CONTRIBUTING.md](../CONTRIBUTING.md) and [GOVERNANCE.md](../GOVERNANCE.md).
- [ ] **I agree to release this contribution under CC0 1.0 Universal** (public domain, no restrictions).
- [ ] If this touches a spec file, I ran `agent-md-validate` on the changed file and it passes.
- [ ] If this adds a new Core spec, I have also added a matching JSON Schema in `schemas/` (or opened a tracking issue).
- [ ] If this touches frontmatter, I checked the required fields: `spec_name`, `spec_version`, `category`, `tier`, `status` — plus `priority` when the spec is `tier: core`. (`maintained_by`, `license` and `spec_type` are conventional, not schema-enforced. There is no `domain` field; adding one fails CI.)
- [ ] If this is a Core-tier change, a linked RFC has been open for ≥14 days.
- [ ] I updated `CHANGELOG.md` under the appropriate heading.
- [ ] I updated `INDEX.md` if this adds or renames a spec.
- [ ] No broken relative markdown links in files I touched.

## Test evidence

<!-- Paste validator output, test command output, or screenshots. -->

```text
$ agent-md-validate <path>
...
```
