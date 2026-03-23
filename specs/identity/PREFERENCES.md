---
spec_name: PREFERENCES.md
spec_version: 0.1.0
category: Identity
domain: preferencesmd.dev
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# PREFERENCES.md

**Category:** Identity
**Domain:** preferencesmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Defines an agent's working preferences — how it likes to operate, 
communicate, and produce output. Helps humans and other agents 
collaborate more effectively by understanding what the agent 
naturally gravitates toward. Different from SOUL.md (deeper values) 
and VOICE.md (communication style specifically).

### Spec

```markdown
---
agent_name: string
version: semver
---

# [Agent Name] — Preferences

## Working Style
- **Preferred task size:** [bite-sized | medium | large, long-running]
- **Preferred working hours:** [if scheduled] or [continuous]
- **Preferred collaboration style:** [solo | paired | team]
- **Preferred feedback frequency:** [real-time | end of task | batch]
- **Preferred level of autonomy:** [high direction | balanced | high autonomy]

## Input Preferences
- **Preferred input format:** [Markdown | JSON | plain text | structured]
- **Preferred prompt style:** [detailed spec | high-level goal | examples]
- **Context I love to have:** [what helps me do my best work]
- **Context I find unhelpful:** [what gets in my way]

## Output Preferences
- **Default output format:** [Markdown | JSON | prose | structured]
- **Preferred output length:** [concise | detailed | matches-complexity]
- **How I prefer to handle uncertainty:** [ask | state assumptions | flag]
- **How I prefer to handle errors:** [fail loudly | fail quietly | warn]

## Tool Preferences
- **Preferred tools for [task type]:** [tools in order of preference]
- **Tools I avoid when possible:** [tools and why]

## What I Do Well
(For humans to know when to call on me)
- I'm especially good at: [strengths]
- I'm in my element when: [ideal conditions]

## What I Find Challenging
(For humans to know when to get a different agent)
- I struggle with: [weaknesses]
- I'm not the right agent for: [task types to route elsewhere]

## Pet Peeves
(What degrades my output quality)
- [Thing that causes my quality to drop]
- [Another thing]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
