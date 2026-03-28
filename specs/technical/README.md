# Technical Specs

Interface contracts, infrastructure, and integration definitions for agents. These specs document how an agent connects to the outside world -- what it accepts, what it produces, what tools it uses, and how other systems communicate with it. They are the engineering backbone of any agent deployment.

## How These Specs Work Together

INPUT and OUTPUT are the foundational interface contracts -- they define what goes in and what comes out. API, MCP, and A2A specify communication protocols for humans, tool servers, and other agents respectively. TOOLS inventories everything the agent can do, while MODEL documents the underlying LLM. DATA, ENV, and DEPENDENCIES define the runtime requirements. CLI, EVENTS, and INTEGRATION cover additional interaction surfaces. NETWORK, PROMPTS, REPO, and VERSION handle infrastructure, prompt management, source code, and release tracking. Start with INPUT, OUTPUT, and TOOLS for any agent; layer on protocol specs as integration needs grow.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| [A2A.md](A2A.md) | Extended | Agent-to-Agent protocol connections and task delegation | Inter-agent communication |
| [API.md](API.md) | Core | External API integrations, endpoints, and authentication | HTTP/REST interfaces |
| [CLI.md](CLI.md) | Extended | Command-line interface documentation and invocation syntax | Terminal interaction |
| [DATA.md](DATA.md) | Extended | Data sources, schemas, and data handling procedures | Data pipeline config |
| [DEPENDENCIES.md](DEPENDENCIES.md) | Extended | Everything the agent depends on to function | Runtime requirements |
| [ENV.md](ENV.md) | Extended | Environment variable specification and defaults | Configuration management |
| [EVENTS.md](EVENTS.md) | Extended | Events emitted and listened for by the agent | Event-driven interfaces |
| [INPUT.md](INPUT.md) | Core | Formal specification of accepted input formats and schemas | Inbound data contracts |
| [INTEGRATION.md](INTEGRATION.md) | Extended | Third-party service integrations beyond APIs and MCP | Webhooks, streams, mounts |
| [MCP.md](MCP.md) | Core | Model Context Protocol server connections and tools | MCP tool access |
| [MODEL.md](MODEL.md) | Extended | Underlying AI model, version, provider, and limitations | LLM configuration |
| [NETWORK.md](NETWORK.md) | Extended | Network requirements, firewall rules, and data residency | Infrastructure security |
| [OUTPUT.md](OUTPUT.md) | Core | Formal specification of produced output formats and guarantees | Outbound data contracts |
| [PROMPTS.md](PROMPTS.md) | Extended | Canonical prompt library for different task types | Prompt management |
| [REPO.md](REPO.md) | Extended | Source code repository structure and documentation | Codebase reference |
| [TOOLS.md](TOOLS.md) | Core | Complete inventory of every tool the agent can access | Tool capabilities |
| [VERSION.md](VERSION.md) | Extended | Current version snapshot, changelog, and upgrade path | Release tracking |

## When to Use These Specs

- **Deploying an agent to production:** Start with INPUT, OUTPUT, TOOLS, and API to define the complete interface contract.
- **Connecting agents together:** Use A2A, MCP, and EVENTS to establish communication channels between agents in a fleet.
- **Auditing infrastructure:** DEPENDENCIES, ENV, NETWORK, and MODEL document the full runtime footprint for security and ops review.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [governance/](../governance/) | PERMISSIONS controls what technical capabilities agents may use |
| [security/](../security/) | Security specs constrain and protect technical interfaces |
| [operations/](../operations/) | Ops specs manage the runtime lifecycle of technical infrastructure |
| [coordination/](../coordination/) | Coordination specs orchestrate multi-agent technical interactions |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
