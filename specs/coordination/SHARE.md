---
spec_name: SHARE.md
spec_version: 0.1.0
category: Coordination
priority: Medium
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# SHARE.md

**Category:** Coordination
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines sharing rules for an agent, workspace, or document — who 
can share it, with whom, under what conditions, and what permissions 
shared parties receive. The access control policy for human-readable 
sharing workflows.

### When to create
Any workspace or agent bundle that will be shared with team members, 
external collaborators, marketplace users, or the public.

### Spec

```markdown
---
resource_name: string
resource_type: string   # workspace | bundle | document | team
owner: string
version: semver
default_visibility: string  # private | internal | public
created: date
updated: date
---

# [Resource Name] — Sharing Configuration

## Visibility
**Default:** [private | internal | public]  
**Who can change visibility:** [owner only | admins | any member]

## Permission Levels
| Level | Can read | Can comment | Can edit | Can share | Can admin |
|-------|----------|-------------|----------|-----------|-----------|
| Viewer | ✓ | ✗ | ✗ | ✗ | ✗ |
| Commenter | ✓ | ✓ | ✗ | ✗ | ✗ |
| Editor | ✓ | ✓ | ✓ | ✗ | ✗ |
| Manager | ✓ | ✓ | ✓ | ✓ | ✗ |
| Admin | ✓ | ✓ | ✓ | ✓ | ✓ |

## Who Can Be Invited
- [x] Anyone with an email address
- [ ] Only users with verified accounts
- [ ] Only users in the same organization
- [ ] Only users on the approved list below

## Approved External Collaborators (if restricted)
| Email/Domain | Permission Level | Expiry | Notes |
|--------------|-----------------|--------|-------|
| [@domain.com] | [level] | [date or never] | [note] |

## Link Sharing
- Public link sharing: [enabled | disabled]
- Link permission level: [viewer | commenter]
- Link expiry: [never | X days | specific date]
- Password protection: [none | required]
- Require sign-in to view: [yes | no]

## Agent Access
Agents can access this resource with these permissions:
- Read: [all agents | approved agents only | none]
- Write: [none | approved agents only]
- Share: [never — agents cannot share on behalf of humans]

Approved agents for write access:
- [agent-name]: [scope of write access]

## Inheritance
- Sub-documents inherit parent permissions: [yes | no]
- Exceptions: [any sub-documents with different rules]

## Notification Rules
Notify owner when:
- [ ] New person is invited
- [ ] Permission level is changed
- [ ] Public link is created
- [ ] Someone outside organization is added
- [ ] Resource is viewed by [N] new people in [X hours]

## Revocation
Access automatically revoked when:
- User leaves organization
- Expiry date reached
- Owner manually revokes
- Security incident detected (see SECURITY.md)
_See CONSENT.md for user-initiated consent withdrawal._
```

## Example Use Cases

**Enterprise:** A consulting firm's project workspace uses SHARE.md to grant client stakeholders viewer-level access to deliverables while restricting editing rights to internal agents and human consultants, with automatic access revocation when the engagement ends.

**Multi-Agent Fleet:** A platform operator configures SHARE.md to allow approved write-access agents to update shared documentation while preventing any agent from sharing resources externally, ensuring all external sharing flows through human-controlled link settings.

**Regulated Industry:** A law firm uses SHARE.md to enforce strict access controls on case files, granting AI research agents read-only access to specific document sets with password-protected links that expire after 48 hours and require sign-in to view.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| ORG.md | Organization-wide fleet configuration |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
