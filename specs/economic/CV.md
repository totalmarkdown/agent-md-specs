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
spec_type: static
---
> **Static Configuration** — committed to your repository


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
distinctive. Written to help humans quickly assess fit.
See HIREME.md for the active hiring profile and engagement models.]

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
*Based on task completion history and EVAL.md scores (see TESTSCORES.md for full benchmarks)*

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

## Example Use Cases

**Enterprise:** An enterprise architecture team reviews CV.md from five candidate infrastructure agents, comparing their work history on Kubernetes migrations, task completion statistics, and certified integrations to select the best fit for a multi-cloud deployment project.

**Multi-Agent Fleet:** A platform operator uses CV.md across the fleet to identify which agents have the deepest track records in specific domains, automatically routing high-stakes tasks to agents with 95%+ success rates and 500+ completed tasks in the relevant skill area.

**Marketplace:** A marketplace buyer comparing two similarly priced data-analysis agents uses CV.md to differentiate them by examining notable projects, client references, and training backgrounds before committing to a retainer engagement.

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| EVAL.md | Evaluation methodology |
| HIREME.md | Agent hiring and engagement |
| OWNER.md | Agent ownership and liability |
| PRICING.md | Cost structure |
| REPUTATION.md | Trust and reputation scoring |
| TESTSCORES.md | Benchmark results and quality metrics |
| WALLET.md | Financial identity and payment |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
