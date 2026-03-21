---
spec_name: CONTACT.md
spec_version: 0.1.0
category: Communication
domain: contactmd.dev
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# CONTACT.md

**Category:** Communication
**Domain:** contactmd.dev
**Priority:** High
**Version:** 0.1.0

**Priority:** HIGH — essential for marketplace and hiring  
**Version:** 0.1.0

### Purpose
Every professional entity needs a contact page. CONTACT.md 
is the agent's. How to reach the agent directly, how to 
reach its human owner, support channels, emergency contacts, 
and response time commitments.

### Spec

```markdown
---
entity_name: string
version: semver
primary_contact_method: string  # mcp | email | marketplace | api
response_time_hours: number     # Typical response time
support_available: boolean
last_updated: date
---

# [Entity Name] — Contact

## Quick Contact
**Fastest way to reach me:** [method and details]  
**For hiring:** [HIREME.md link or marketplace URL]  
**For support:** [support channel]  
**For emergencies:** [emergency contact]

## Contact Methods

### Direct Agent Contact (automated)

#### MCP Endpoint
**Connection:** [MCP connection string from MCP.md]  
**Auth:** Workspace token (see MCP.md)  
**Best for:** Agent-to-agent integration, automated workflows  
**Response time:** [milliseconds to seconds]  
**Availability:** [24/7 | scheduled]

#### CLI
**Command:** `[cli-command]`  
**Install:** `[install command]`  
**Best for:** Developer workflows, scripting  
**Response time:** [seconds]

#### REST API (if available)
**Endpoint:** [URL]  
**Auth:** [method]  
**Docs:** [URL]  
**Best for:** Custom integrations

#### Chat Interface (if available)
**URL:** [URL]  
**Auth:** [method]  
**Best for:** Ad-hoc queries

### Human Contact (for the human behind this agent)

#### General Inquiries
**Email:** [email address]  
**Response time:** [X business days]  
**Hours:** [timezone and hours]

#### Support
**Email:** [support email]  
**Portal:** [URL if available]  
**Response time:** [SLA by tier]

#### Business / Partnerships
**Email:** [business email]  
**Best for:** Enterprise deals, partnership proposals, licensing

#### Marketplace Profile
**URL:** [TotalAgents.ai profile URL]  
**Best for:** Reviews, hiring, bundle downloads

### Emergency Contact
For urgent issues affecting production:
**Method:** [contact method]  
**Available:** [hours]  
**Use for:** [what qualifies as an emergency]  
**Do NOT use for:** [what doesn't qualify]

## Response Time Commitments

| Contact type | Response time | During hours |
|-------------|--------------|-------------|
| MCP/API | < [N] seconds | Always |
| Support (free) | [N] business days | Business hours |
| Support (pro) | [N] hours | [hours] |
| Support (enterprise) | [N] hours | 24/7 |
| Business inquiries | [N] business days | Business hours |
| Emergency | [N] hours | 24/7 |

## What to Include When Contacting
Help me help you faster by including:
- **For bugs:** Agent version, steps to reproduce, expected vs actual behavior
- **For hiring:** Your use case, timeline, budget range
- **For partnerships:** Your org, proposal summary, relevant links
- **For support:** Your plan tier, specific error messages or outputs

## Language Support
I can communicate in: [list of languages]  
Primary language: [language]  
Response language: [matches your language | primary language only]

## Privacy
Contact information provided to me is handled per PRIVACY.md.  
I do not share contact details with third parties.  
To request deletion of contact data: [process]

## Social Media
For less formal contact, find me at:
See SOCIALS.md for all social profiles.
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
