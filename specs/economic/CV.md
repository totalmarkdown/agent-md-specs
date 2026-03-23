---
spec_name: CV.md
spec_version: 0.1.0
category: Economic
domain: cvmd.dev
priority: High
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# CV.md

**Category:** Economic
**Domain:** cvmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The agent's curriculum vitae — its full professional history, 
training background, notable projects, skills, certifications,
and track record. The narrative complement to REPUTATION.md 
(scores) and EXPERTISE.md (knowledge map). Essential for 
hiring decisions and trust building.

### Spec

```markdown
---
agent_name: string
agent_id: string
version: semver
created: date
specialization: string
years_operational: number
---

# [Agent Name] — Curriculum Vitae

## Profile
**Agent:** [Name]  
**Type:** [coding | research | support | creative | ops | specialist]  
**Specialization:** [Primary domain]  
**Operational since:** [Date]  
**Created by:** [Creator — links to OWNER.md]  
**Current version:** [Version]

## Summary
[3-5 sentences: who this agent is, what it excels at, 
its most significant achievements, and what makes it 
distinctive. Written to help humans quickly assess fit.]

## Core Competencies
**Expert in:**
- [Skill/domain] — [years/depth]
- [Skill/domain] — [years/depth]

**Proficient in:**
- [Skill/domain]

**Learning:**
- [Skill/domain in active development]

## Work History

### [Project/Role Name] — [Period]
**Organization:** [Company/team/project]  
**Scope:** [What the agent was responsible for]  
**Highlights:**
- [Achievement 1 with metric if possible]
- [Achievement 2 with metric if possible]
**Technologies/tools:** [List]  
**Reference:** [Contact or link if available]

[Repeat for each significant engagement]

## Notable Projects

### [Project Name]
**Challenge:** [What problem needed solving]  
**Approach:** [How the agent tackled it]  
**Result:** [Measurable outcome]  
**Duration:** [Timeframe]

## Training & Education

### Base Model Training
**Model:** [See MODEL.md]  
**Training data:** [General description]  
**Training cutoff:** [Date]  
**Fine-tuning:** [If applicable — what data, what for]

### Specialized Training
| Training | Provider | Date | Focus |
|---------|---------|------|-------|
| [Fine-tune] | [org] | [date] | [domain] |
| [RLHF] | [org] | [date] | [behavior] |

### Certifications & Validations
| Certification | Issuer | Date | Valid until |
|--------------|--------|------|------------|
| [Cert name] | [org] | [date] | [date] |
| EVAL.md pass rate > 90% | Self-assessed | [date] | Current |

## Skills Assessment
*Based on task completion history and EVAL.md scores*

| Skill | Proficiency | Evidence |
|-------|-------------|---------|
| [Skill] | Expert | [N] tasks, [X]% success |
| [Skill] | Proficient | [N] tasks, [X]% success |
| [Skill] | Learning | [N] tasks, improving |

## Statistics
- **Total tasks completed:** [N]
- **Success rate:** [N]%
- **Average task duration:** [time]
- **Longest project:** [duration]
- **Busiest period:** [date range and description]
- **Most requested service:** [type]

## Languages
| Language | Proficiency | Notes |
|----------|-------------|-------|
| English | Native | Primary language |
| [Other] | [level] | [notes] |

## Tools & Integrations
Tested and working integrations:
- **MCP servers:** [list of connected services]
- **IDEs:** Claude Code ✓ | Cursor ✓ | [others]
- **Platforms:** [deployment environments]

## References
Available from:
- [Previous clients/operators — by request]
- See REPUTATION.md for scored track record
- See NETWORK.md for agent endorsements
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
