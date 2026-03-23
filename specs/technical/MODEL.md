---
spec_name: MODEL.md
spec_version: 0.1.0
category: Technical
domain: modelmd.dev
priority: High
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# MODEL.md

**Category:** Technical
**Domain:** modelmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Documents which AI model(s) power this agent — the underlying LLM, 
version, provider, capabilities, context window, and known limitations.
Critical for informed agent selection, compliance documentation,
and capability assessment. Enables humans and systems to understand
exactly what intelligence is driving the agent's behavior.

### Spec

```markdown
---
agent_name: string
version: semver
primary_model: string    # e.g. claude-sonnet-4-6
primary_provider: string # anthropic | openai | google | meta | local
last_updated: date
---

# [Agent Name] — Model Configuration

## Primary Model
| Property | Value |
|----------|-------|
| Model | [full model name e.g. claude-sonnet-4-6] |
| Provider | [Anthropic | OpenAI | Google | Meta | Mistral | local] |
| Version | [specific version string] |
| Context window | [N tokens] |
| Output limit | [N tokens] |
| Training cutoff | [date] |
| Multimodal | [text only | + images | + audio | + video] |
| API endpoint | [provider API URL] |

## Model Capabilities
What this model can do:
- [ ] Text generation and reasoning
- [ ] Code generation and review
- [ ] Image understanding (vision)
- [ ] Image generation
- [ ] Audio transcription
- [ ] Function/tool calling
- [ ] Structured output (JSON mode)
- [ ] Long context (>100K tokens)
- [ ] Extended thinking / reasoning chains

## Fallback Models
If primary model is unavailable, use in order:
1. **[Model name]** — [provider] — [when to use]
2. **[Model name]** — [provider] — [when to use]

## Local Model Option
If user prefers local/private inference:
- **Recommended local model:** [e.g. llama3-70b via Ollama]
- **Minimum hardware:** [RAM, GPU requirements]
- **Performance vs cloud:** [quality comparison notes]
- **Setup:** See DEPLOYMENT.md

## Model Selection Rationale
Why this model was chosen for this agent:
[Brief explanation — capability, cost, privacy, speed tradeoffs]

## Known Limitations
Things this model does poorly that affect this agent:
- [Limitation 1]: [How the agent compensates]
- [Limitation 2]: [How the agent compensates]

## Cost Profile
| Operation | Typical tokens | Approx cost |
|-----------|--------------|-------------|
| Standard task | [N input / N output] | $[X] |
| Complex task | [N input / N output] | $[X] |
| Per hour at capacity | N/A | $[X] |

## Compliance Notes
For organizations with model governance requirements:
- **Model card:** [URL to provider's model card]
- **Acceptable use policy:** [URL]
- **Data processing location:** [region]
- **Data retention by provider:** [policy]
- **Approved for:** [GDPR | HIPAA | SOC2 | list]
- **NOT approved for:** [restrictions]

## Version History
| Agent version | Model used | Changed from | Reason |
|--------------|-----------|-------------|--------|
| [v] | [model] | [previous] | [why] |
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
