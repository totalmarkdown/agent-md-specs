---
spec_name: SHARE.md
spec_version: 0.1.0
category: Coordination
domain: sharemd.dev
priority: Medium
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# SHARE.md

**Category:** Coordination
**Domain:** sharemd.dev
**Priority:** Medium
**Version:** 0.1.0

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
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
