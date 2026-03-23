---
spec_name: SOCIALS.md
spec_version: 0.1.0
category: Social
domain: socialsmd.dev
priority: Medium
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# SOCIALS.md

**Category:** Social
**Domain:** socialsmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
All social media and community presence for an agent or its creator — 
where to follow updates, see demos, engage with the community, 
and discover new releases.

### Spec

```markdown
---
agent_name: string
version: semver
primary_social: string   # Where most activity happens
last_updated: date
---

# [Agent Name] — Social Presence

## Where to Find Us

### Primary Channel: [Platform]
**URL:** [link]  
**Handle:** [@handle]  
**What we post:** [types of content]  
**Posting frequency:** [daily | weekly | major updates only]  
**Best for:** [why follow here]

### GitHub
**Organization:** github.com/[org]  
**Agent repo:** github.com/[org]/[repo]  
**Stars:** [N] ⭐  
**What's here:** Source, issues, releases, discussions  
**Contribute:** See CONTRIBUTING.md in repo

### X / Twitter
**Handle:** [@handle]  
**URL:** x.com/[handle]  
**What we post:** Updates, tips, community highlights  
**Notifications:** Follow for release announcements

### LinkedIn
**Page:** linkedin.com/company/[name]  
**What's here:** Professional updates, case studies, enterprise news

### Discord
**Server:** discord.gg/[invite]  
**Key channels:**
- #announcements — releases and major updates
- #support — get help
- #showcase — share what you built
- #feedback — suggest improvements

### YouTube
**Channel:** youtube.com/@[handle]  
**What's here:** Demo videos, tutorials, deep-dives  
**Subscribe for:** Video walkthroughs of new features

### Reddit
**Community:** reddit.com/r/[subreddit]  
**What's here:** Community discussion, help, showcases

### Hacker News
**Profile:** news.ycombinator.com/user?id=[username]  
**We post here:** Major releases, technical writeups

### Bluesky
**Handle:** @[handle].bsky.social  
**What we post:** [content type]

## Creator / Author Socials
*The human(s) behind this agent:*

| Person | Role | X/Twitter | GitHub | LinkedIn |
|--------|------|-----------|--------|---------|
| [name] | [role] | [@handle] | [handle] | [URL] |

## Community
**Total followers (all platforms):** [N]  
**Most active community:** [platform]  
**Community manager:** [handle or "automated"]

## Press & Media
For press inquiries: [contact]  
Press kit: [URL]  
Media mentions: [URL]

## Newsletter
**Subscribe:** [URL]  
**Frequency:** [weekly | monthly | major releases]  
**What you get:** [content description]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
