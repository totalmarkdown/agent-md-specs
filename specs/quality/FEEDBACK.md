---
spec_name: FEEDBACK.md
spec_version: 0.1.0
category: Quality
domain: feedbackmd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# FEEDBACK.md

**Category:** Quality
**Domain:** feedbackmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines how an agent collects, processes, and learns from feedback 
on its outputs — both automated feedback (eval scores) and human 
feedback (thumbs up/down, corrections, comments).

### Spec

```markdown
---
agent_name: string
version: semver
feedback_enabled: boolean
auto_learn: boolean        # Can agent update its behavior based on feedback?
created: date
updated: date
---

# [Agent Name] — Feedback Configuration

## Feedback Collection

### Automated feedback (always on)
- Eval scores from EVAL.md test suite: [run frequency]
- Task completion rate: tracked automatically
- Error rate: tracked automatically
- User correction rate: [how often users edit agent output]

### Human feedback (if enabled)
Users can provide feedback via:
- [ ] Thumbs up/down on individual outputs
- [ ] Star rating (1-5) per task
- [ ] Written correction (user edits output)
- [ ] Explicit comment/note
- [ ] Flagging as inappropriate

## Feedback Processing

### What feedback is acted on automatically
- Written corrections: saved to TRAINING.md for future few-shot examples
- Consistent thumbs-down pattern: flag for human review
- Output flagged as inappropriate: escalate immediately, stop task

### What requires human review
- Any feedback suggesting safety or ethics concern
- Pattern of low ratings (3+ consecutive below [threshold])
- Feedback suggesting capability gap (agent consistently wrong on topic)

## Learning Loop
If auto_learn is enabled:
1. Collect [N] examples of positive feedback
2. Collect [N] examples of corrected output
3. When [threshold] reached: propose TRAINING.md update
4. Human reviews proposed changes before applying
5. Re-run EVAL.md suite to verify improvement

Auto-learn never modifies: SOUL.md, POLICY.md, SECURITY.md, ESCALATION.md
(Only updates: TRAINING.md, optionally SKILL.md descriptions)

## Feedback Privacy
- Feedback stored: [location]
- Retention: [X days]
- Anonymized before analysis: [yes | no]
- User can delete their feedback: [yes | no]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
