---
spec_name: CONTACT.md
spec_version: 0.1.0
category: Communication
priority: High
tier: core
---

# [REPLACE THIS — Agent Name] — Contact Endpoints

<!-- How to reach this agent: discovery, invocation, and communication channels -->

## Primary Endpoint
- **Protocol:** [REPLACE THIS — MCP | A2A | REST | gRPC | WebSocket | CLI]
- **URL / Address:** [REPLACE THIS — endpoint URL or connection string]
- **Auth required:** [REPLACE THIS — API key | OAuth | mTLS | none]

## Discovery
- **Registry:** [REPLACE THIS — where this agent is listed for discovery]
- **Agent Card URL:** [REPLACE THIS — URL to A2A agent card, or "N/A"]
- **Health check:** [REPLACE THIS — URL or command to verify agent is alive]

## Communication Channels

| Channel | Address | Purpose | Async |
|---------|---------|---------|-------|
| [REPLACE THIS — e.g. API] | [REPLACE THIS] | [REPLACE THIS — task invocation] | [REPLACE THIS — true | false] |
| [REPLACE THIS — e.g. Webhook] | [REPLACE THIS] | [REPLACE THIS — event notification] | [REPLACE THIS] |
| [REPLACE THIS — e.g. Queue] | [REPLACE THIS] | [REPLACE THIS — batch processing] | [REPLACE THIS] |

## Message Format
- **Request schema:** [REPLACE THIS — JSON schema reference, or "freeform"]
- **Response schema:** [REPLACE THIS — JSON schema reference, or "freeform"]
- **Max payload size:** [REPLACE THIS — e.g. 1MB]

## Rate Limits
- **Requests per minute:** [REPLACE THIS]
- **Concurrent connections:** [REPLACE THIS]
- **Backpressure strategy:** [REPLACE THIS — queue | reject | throttle]

## Availability
- **Uptime target:** [REPLACE THIS — e.g. 99.9%, best-effort, business-hours]
- **Maintenance window:** [REPLACE THIS — scheduled downtime, or "none"]
- **Status page:** [REPLACE THIS — URL to check agent status, or "none"]

## Human Escalation
- **Owner contact:** [REPLACE THIS — email or handle for the agent's operator]
- **Escalation path:** [REPLACE THIS — how to reach a human if agent is unresponsive]

## Related Specs
- ID.md: [REPLACE THIS — path]
- WHOAMI.md: [REPLACE THIS — path]
- TEAM.md: [REPLACE THIS — path]
