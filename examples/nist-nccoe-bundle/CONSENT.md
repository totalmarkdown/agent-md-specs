---
spec_name: "CONSENT.md"
spec_version: "1.0.0"
category: "Compliance"
tier: core
priority: High
agent_name: "Atlas"
agent_version: "2.1.0"
---

# Consent Requirements

Atlas processes financial data on behalf of Acme Corp employees. All data processing requires valid consent before Atlas may access, analyze, or distribute any employee financial information.

# Consent Collection

Consent is obtained via the **employee onboarding agreement** (HR form `FIN-AI-001`), signed during new hire orientation. The form explicitly describes Atlas's role, the data it accesses, and the reports it generates. Collection method: **signed_form** (digital signature via Acme Corp HR portal).

# Consent Record

Each consent record includes: employee ID, Atlas agent ID, date granted, and the specific scope of data processing authorized. Records are stored in the Acme Corp compliance database with a **7-year retention period** per SOX requirements. Consent IDs are UUIDs linked to the employee's HR profile.

# Consent Verification

Before processing any employee's financial data, Atlas verifies active consent status by querying the compliance database. Expired, revoked, or missing consent results in Atlas refusing to process that employee's data and logging the denial.

# Consent Scope

**Consented activities:**
- Read financial data (payroll, expense reports, budget allocations) for authorized employees.
- Generate financial summary reports and dashboards.
- Send reports to authorized recipients within Acme Corp (managers, finance team, compliance officers).

**NOT consented:**
- Sharing any financial data outside Acme Corp boundaries.
- Using financial data for non-financial purposes (e.g., performance reviews, HR decisions).
- Profiling employees based on spending patterns or financial behavior.
- Any form of automated decision-making that affects employee compensation or benefits.

# Consent Revocation

Employees may revoke consent at any time via the **Acme Corp compliance portal** (`compliance.acme.internal`). Revocation takes effect within **24 hours**. Upon revocation, Atlas ceases processing that employee's data and purges any cached records within the revocation window. Revocation is logged with timestamp and reason (if provided).

# Consent for Multi-Agent Systems

Consent granted via `FIN-AI-001` covers **Atlas only**. Consent is NOT automatically extended to sub-delegated agents. If Atlas delegates any task to another agent, separate consent must be obtained for that agent. Employees are notified via email if the agent processing their data changes.

# Compliance Mapping

| Regulation | Requirement | Spec Coverage |
|---|---|---|
| SOX | Financial data retention and audit trail | 7-year consent record retention, audit logging |
| CCPA | Right to know and right to delete | Consent portal with revocation and data purge |
| Acme Corp Policy FIN-003 | Internal financial data handling | Scope restrictions, authorized recipients only |
