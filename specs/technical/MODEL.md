---
spec_name: MODEL.md
spec_version: 0.1.0
category: Technical
priority: High
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# MODEL.md

**Category:** Technical
**Priority:** High
**Version:** 0.1.0 **Type:** Static

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
_See BUDGET.md for cost controls and spending limits._
| Operation | Typical tokens | Approx cost |
|-----------|--------------|-------------|
| Standard task | [N input / N output] | $[X] |
| Complex task | [N input / N output] | $[X] |
| Per hour at capacity | N/A | $[X] |

## Compliance Notes
For organizations with model governance requirements (see EUAIACT.md for EU AI Act classification):
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

## Example Use Cases

**Enterprise:** A product team uses MODEL.md to document their customer support agent's primary model (Claude Sonnet), fallback model (GPT-4o), and local option (Llama 3 via Ollama), with cost profiles showing $0.003 per standard task to justify budget allocation.

**Multi-Agent Fleet:** A marketplace operator requires MODEL.md for every listed agent, enabling buyers to filter agents by context window size, multimodal capabilities, and training cutoff date before selecting the right agent for their use case.

**Regulated Industry:** An EU-based enterprise uses MODEL.md compliance notes to verify that their agent's model provider has a Data Processing Agreement, processes data in EU regions, and is approved for GDPR-compliant workloads before deploying in production.

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
