---
spec_name: PROVENANCE.md
spec_version: 0.1.0
category: Compliance
domain: provenancemd.dev
priority: High
volume: "Vol 14 — Agent Identity, Accountability & Compliance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# PROVENANCE.md

**Category:** Compliance
**Domain:** provenancemd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines how an agent tracks the origin, transformation history,
and trust level of every piece of data it consumes and produces.
Provenance is the chain of custody for information — who created
it, how it was modified, and whether the output can be trusted
given the quality of the inputs.

Without provenance tracking, an agent cannot answer the question
"why did you produce this output?" with anything more than "the
model generated it." PROVENANCE.md ensures every output can be
traced back to its source inputs, every transformation is logged,
and trust levels propagate correctly through the processing chain.

At fleet scale, PROVENANCE.md enables:
- Risk assessment of outputs based on input quality and source trust
- Detection of data contamination across multi-agent pipelines
- Regulatory compliance for data lineage requirements (EU AI Act, NIST AI RMF)
- Confidence calibration: low-trust inputs produce low-confidence outputs
- Forensic reconstruction of how bad data propagated through a system

### When to Create This File
Every agent that transforms data — summarizing, filtering,
aggregating, enriching, or generating content based on inputs.
Required for agents in regulated industries, agents that produce
outputs consumed by other agents, and any agent where the
trustworthiness of outputs depends on the trustworthiness of
inputs. Essential when an agent's outputs feed into human
decision-making.

### Spec

````markdown
---
agent_name: string
agent_id: string              # Must match WHOAMI.md agent_id
version: semver
provenance_level: string      # minimal | standard | comprehensive | forensic
trust_propagation: string     # strict | weighted | permissive
contamination_policy: string  # halt | quarantine | flag_and_continue | reject_and_reprocess
spec_version: string
---

# [Agent Name] — Provenance Configuration

## Input Source Registry

All data sources this agent consumes, with trust classification.

| Source | Type | Trust Level | Hash Method | Last Verified | Owner |
|--------|------|-------------|-------------|---------------|-------|
| [Source name] | [API | database | file | user_input | agent_output | web_scrape] | [verified | trusted | provisional | untrusted | unknown] | [SHA-256 | SHA-384 | none] | [date] | [who controls this source] |
| Production DB | database | verified | SHA-256 | 2025-01-15 | Platform team |
| User prompts | user_input | provisional | SHA-256 | per-request | End user |
| Agent-Alpha output | agent_output | trusted | SHA-256 | 2025-01-10 | Agent-Alpha owner |
| Web search results | web_scrape | untrusted | SHA-256 | per-request | External |
| Internal knowledge base | file | verified | SHA-256 | 2025-01-01 | Knowledge team |

### Trust Level Definitions
| Level | Definition | Allowed Actions |
|-------|------------|-----------------|
| **Verified** | Source authenticated, integrity confirmed, content validated | Full processing, can inform high-stakes decisions |
| **Trusted** | Source authenticated, integrity confirmed, content not independently validated | Full processing, flag in high-stakes outputs |
| **Provisional** | Source identity known but not cryptographically verified | Process with reduced confidence, always disclose source |
| **Untrusted** | Source cannot be authenticated or has known reliability issues | Process only with sandboxing, never use as sole basis for decisions. Apply extra injection scanning per PROMPTSHIELD.md |
| **Unknown** | Source provenance cannot be determined | Treat as untrusted, flag for human review |

_For memory and training data poisoning risks related to untrusted sources, see MEMORYSAFETY.md._

---

## Prompt Provenance

Track the origin and authority chain of every instruction the
agent receives.

For each prompt or instruction, record:

```yaml
prompt_provenance:
  prompt_hash: "sha256:..."            # Hash of the prompt content
  issuer: "human:jane@org.com"         # Who issued the prompt
  issuer_verified: true                # Was issuer identity verified via ATTESTATION
  channel: "api | cli | slack | agent" # How the prompt arrived
  channel_authenticated: true          # Was the channel itself authenticated
  delegation_chain:                    # If prompt passed through other agents (see DELEGATION.md)
    - agent: "orchestrator-01"
      received: "ISO-8601"
      modified: false                  # Did the intermediary modify the prompt
      modification_hash: null          # If modified, hash of modification
    - agent: "router-03"
      received: "ISO-8601"
      modified: true
      modification_hash: "sha256:..."
      modification_reason: "Added context from knowledge base"
  original_prompt_hash: "sha256:..."   # Hash of prompt before any modifications
  prompt_injection_scan: "clean"       # clean | suspicious | blocked
```

### Prompt Trust Scoring
| Factor | Weight | Score |
|--------|--------|-------|
| Issuer verified via ATTESTATION | 0.30 | [0.0-1.0] |
| Channel authenticated | 0.20 | [0.0-1.0] |
| No intermediary modifications | 0.20 | [0.0-1.0] |
| Prompt injection scan clean | 0.20 | [0.0-1.0] |
| Delegation chain valid | 0.10 | [0.0-1.0] |
| **Composite trust score** | **1.00** | **[0.0-1.0]** |

Actions based on composite score:
- **0.8 - 1.0:** Process normally
- **0.5 - 0.79:** Process with elevated logging, flag output
- **0.2 - 0.49:** Process only non-sensitive tasks, require human review
- **Below 0.2:** Reject, log, alert

---

## Context Window Snapshot

At each significant decision point, capture a hash of the full
context window state. This enables post-hoc verification that
the agent's context was not corrupted or injected.

| Decision Point | Context Hash | Input Count | Token Count | Timestamp |
|----------------|-------------|-------------|-------------|-----------|
| [task start] | `sha256:...` | [N inputs] | [N tokens] | [ISO-8601] |
| [before tool call] | `sha256:...` | [N inputs] | [N tokens] | [ISO-8601] |
| [before output] | `sha256:...` | [N inputs] | [N tokens] | [ISO-8601] |

Snapshot includes:
- Hash of all system instructions in context
- Hash of all user/agent messages in context
- Hash of all tool call results in context
- Total token count (detect unexpected growth indicating injection)

---

## Transformation Log

Document how inputs are processed into outputs. Every
transformation that modifies data is recorded and logged
to AUDITTRAIL.md for tamper-resistant retention.

```yaml
transformation:
  transform_id: "uuid-v4"
  timestamp: "ISO-8601"
  type: "summarize | filter | aggregate | enrich | generate | translate | classify | extract"
  input_refs:
    - source: "Production DB"
      hash: "sha256:..."
      trust_level: "verified"
      records_count: 1500
    - source: "User prompt"
      hash: "sha256:..."
      trust_level: "provisional"
  operation: "Summarized 1500 customer records into quarterly report"
  parameters:
    model: "claude-sonnet-4-20250514"
    temperature: 0.1
    max_tokens: 4096
  output_hash: "sha256:..."
  output_trust_level: "provisional"   # Degraded: one input was provisional
  data_loss: "yes — individual records summarized to aggregates"
  reversible: false
  confidence: 0.88
```

### Trust Propagation Rules
**Mode:** [strict | weighted | permissive]

| Mode | Rule |
|------|------|
| **Strict** | Output trust = minimum trust of all inputs |
| **Weighted** | Output trust = weighted average by input significance |
| **Permissive** | Output trust = trust of primary input (others are supplementary) |

This agent uses: [selected mode]

---

## Data Classification Escalation

When an agent combines or processes data, the resulting sensitivity
may exceed that of any individual input. These rules detect and
handle classification escalation.

| Trigger | Escalation | Action |
|---------|-----------|--------|
| Combining 2+ "Internal" PII datasets | Internal -> Confidential | Reclassify output, restrict access, log escalation |
| Aggregating anonymized data to re-identifiable level | Public -> Confidential | Halt processing, alert privacy officer, log. Aggregated data may require new consent (see CONSENT.md) |
| Enriching data with external sources | Maintain or escalate | Re-evaluate classification post-enrichment |
| Cross-referencing datasets from different jurisdictions | Apply strictest jurisdiction | Apply most restrictive data handling rules |
| Any input classified "Restricted" | Output is Restricted | Apply Restricted handling regardless of transformation |

Classification escalation events are logged in AUDITTRAIL.md with
action_type "classification_escalation."

---

## Output Provenance Statement

Every output produced by this agent includes (or can produce on
request) a provenance statement documenting its lineage.

```yaml
output_provenance:
  output_id: "uuid-v4"
  output_hash: "sha256:..."
  produced_by: "agent-id"
  produced_at: "ISO-8601"

  input_sources:
    - source: "Production DB"
      contribution: "primary"          # primary | supplementary | contextual
      trust_level: "verified"
      records_used: 1500
    - source: "User prompt"
      contribution: "contextual"
      trust_level: "provisional"

  transformations_applied:
    - "filter: date range 2025-Q1"
    - "aggregate: sum by region"
    - "summarize: natural language report"

  composite_trust: 0.78               # Weighted trust of all inputs
  confidence: 0.85                    # Agent's self-assessed confidence

  limitations:
    - "Based on data available as of 2025-01-15"
    - "Web search results not independently verified"
    - "Summarization may lose nuance from individual records"

  verification:
    reproducible: false                # Can this exact output be reproduced
    methodology_documented: true       # Are all steps documented above
    human_reviewed: false              # Was output reviewed by human before delivery
```

---

## Contamination Policy

**Policy:** [halt | quarantine | flag_and_continue | reject_and_reprocess]

Contamination occurs when untrusted, corrupted, or adversarial
data enters the processing pipeline. For adversarial input
detection, see PROMPTSHIELD.md.

### Detection Triggers
- Input from "untrusted" or "unknown" source used in high-stakes output
- Prompt injection detected in any input (see PROMPTSHIELD.md)
- Hash mismatch on a previously-verified input source
- Trust level of an input source downgraded during processing
- Anomalous input size or format suggesting injection

### Response by Policy Level
| Policy | Trigger Response | Output Handling | Notification |
|--------|-----------------|-----------------|--------------|
| **Halt** | Stop all processing immediately | No output produced | Alert human + security team |
| **Quarantine** | Isolate contaminated input, continue with clean inputs only | Output marked as "partial — contaminated input excluded" | Alert human |
| **Flag and continue** | Process all inputs, flag contaminated ones | Output includes contamination warning and affected sections | Log warning |
| **Reject and reprocess** | Remove contaminated input, restart processing from clean inputs | Clean output produced, may be incomplete | Log event |

### Post-Contamination
1. Log contamination event in AUDITTRAIL.md
2. Identify all outputs that used the contaminated input
3. Flag downstream agents that consumed those outputs
4. Assess whether contamination was adversarial (escalate to PROMPTSHIELD.md)
5. Update Input Source Registry trust level as appropriate
6. Post-incident review within [24 hours]
````

## Example Use Cases

**Enterprise:** A financial research agent tracks the trust level of every data source (Bloomberg API as "verified," web-scraped earnings estimates as "untrusted") and automatically downgrades output confidence when any untrusted source contributes to an investment recommendation.

**Multi-Agent Fleet:** A content-generation pipeline of five agents uses PROVENANCE.md to trace a published article back through each transformation step (research, drafting, fact-checking, editing, formatting), enabling editors to pinpoint exactly where an inaccuracy was introduced.

**Regulated Industry:** A pharmaceutical company's drug-interaction analysis agent maintains forensic-level provenance records so that FDA auditors can trace any safety recommendation back to its source clinical trial data, transformation logic, and the trust level assigned to each input.

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| OUTPUT.md | Output formats and delivery |
| DATA.md | Data handling and governance |
| AUDITTRAIL.md | Tamper-proof action logging |
| PROMPTSHIELD.md | Prompt injection defense |
| ATTESTATION.md | Identity verification and credential lifecycle |
| PRIVACY.md | Data privacy handling |
| DELEGATION.md | Authority chain and authorization |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
