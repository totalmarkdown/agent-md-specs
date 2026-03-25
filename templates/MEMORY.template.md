---
spec_name: MEMORY.md
spec_version: 0.1.0
category: Coordination
domain: specmd.dev
priority: P1
tier: core
---

# [REPLACE THIS — Agent Name] — Memory Configuration

<!-- Individual agent memory: what is remembered, how, and for how long -->

## Memory Architecture
- **Short-term:** [REPLACE THIS — in-context window | scratchpad | none]
- **Long-term:** [REPLACE THIS — vector DB | key-value store | file-based | none]
- **Episodic:** [REPLACE THIS — session logs | conversation history | none]

## Storage Backend
- **Provider:** [REPLACE THIS — e.g. Pinecone, ChromaDB, PostgreSQL, local files]
- **Location:** [REPLACE THIS — connection string or path]
- **Embedding model:** [REPLACE THIS — model used for vector storage, or "N/A"]

## What Gets Remembered
| Category | Stored | Retention | Example |
|----------|--------|-----------|---------|
| Task outcomes | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| User preferences | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| Learned patterns | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| Errors and fixes | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## What Is Never Stored
<!-- Sensitive data that must not persist in memory -->
- [REPLACE THIS — e.g. passwords, API keys, PII]
- [REPLACE THIS — e.g. raw user credentials]
- [REPLACE THIS]

## Recall Strategy
- **Retrieval method:** [REPLACE THIS — semantic search | keyword | recency | hybrid]
- **Max recall items:** [REPLACE THIS — number of memories returned per query]
- **Relevance threshold:** [REPLACE THIS — minimum similarity score, or "none"]

## Memory Hygiene
- **Compaction:** [REPLACE THIS — how old memories are summarized or pruned]
- **Deduplication:** [REPLACE THIS — strategy for removing redundant entries]
- **Expiry sweep:** [REPLACE THIS — frequency of TTL-based cleanup]

## Related Specs
- MEMORYSAFETY.md: [REPLACE THIS — path]
- SHAREDCONTEXT.md: [REPLACE THIS — path]
- SESSION.md: [REPLACE THIS — path]
