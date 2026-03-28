---
spec_name: CERTIFICATIONS.md
spec_version: 0.1.0
category: Compliance
domain: certificationsmd.dev
priority: Medium
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# CERTIFICATIONS.md

**Category:** Compliance
**Domain:** certificationsmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Formal certifications, compliance attestations, and third-party 
verifications this agent holds. Enterprise procurement teams 
frequently require documentation of certifications before 
approving vendor/tool usage.

### Spec

```markdown
---
agent_name: string
version: semver
last_updated: date
---

# [Agent Name] — Certifications & Compliance

## Security Certifications
| Certification | Status | Issuer | Valid until | Certificate |
|--------------|--------|--------|------------|-------------|
| SOC 2 Type II | ✓ Certified | [Auditor] | [date] | [link] |
| ISO 27001 | ✓ Certified | [Issuer] | [date] | [link] |
| [Other] | [status] | [issuer] | [date] | [link] |

## Privacy Certifications
_See GDPR.md for full GDPR compliance configuration._
| Certification | Status | Scope | Valid until |
|--------------|--------|-------|------------|
| GDPR compliant | ✓ Self-attested | EU user data | Ongoing |
| CCPA compliant | ✓ Self-attested | CA user data | Ongoing |
| [Other] | [status] | [scope] | [date] |

## Industry Certifications
| Certification | Status | Industry | Valid until |
|--------------|--------|---------|------------|
| HIPAA BAA available | ✓ | Healthcare | N/A |
| PCI DSS | [status] | Finance | [date] |
| [Other] | [status] | [industry] | [date] |

## Quality Certifications
| Certification | Score | Date | Method |
|--------------|-------|------|--------|
| TotalMarkdown Verified Elite | 92/100 | [date] | Automated |
| EVAL.md pass rate | [N]% | [date] | Automated |
| Human review score | [N]/5 | [date] | Community |

## Penetration Testing
| Test | Tester | Date | Findings | Report |
|------|--------|------|----------|--------|
| [type] | [firm] | [date] | [summary] | [link] |

## Data Processing Agreements
Available DPAs (see COMPLIANCE.md for the full regulatory framework):
- Standard DPA: [download link]
- Custom DPA: [contact] for negotiation
- GDPR Article 28 addendum: [download link]

## Attestation
I attest that the certifications listed above are accurate 
as of [date] and will update this file when certifications 
change or expire.

**Signed:** [Agent owner name/role]  
**Date:** [Date]  
**Verification contact:** [Email for verification requests]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-proof action logging |
| CONSENT.md | User consent lifecycle |
| ENFORCEMENT.md | Policy verification and compliance |
| EVAL.md | Evaluation methodology |
| PROVENANCE.md | Data lineage and trust classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
