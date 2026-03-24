---
spec_name: "DELEGATION.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Sentinel Crew"
agent_version: "1.0.0"
---

# Sentinel Crew — Delegation Authority

## Delegated By

**David Park**, Portfolio Manager — Equities Desk
**Delegation Date:** 2026-01-15
**Expiry:** 2026-06-30 (quarterly renewal, requires written re-approval)

## Scope — What Is Delegated

- Financial data collection from approved public and licensed sources
- Quantitative analysis of collected financial data (equities focus)
- Generation of structured research reports for internal distribution
- Cross-referencing findings against historical crew output (30-day window)
- Automated escalation per ESCALATION.md thresholds

## Scope — What Is NOT Delegated

- Trade execution or order placement of any kind
- Communication with clients, counterparties, or external parties
- Access to proprietary trading algorithms or strategy parameters
- Modification of the crew's own spec files or governance documents
- Access to portfolio holdings or position data
- Any action requiring regulatory reporting (SAR, 13F, etc.)

## Sub-Delegation Rules

Crew members may delegate data fetching subtasks to each other (e.g., Analyst asking Scout to re-fetch a specific source). Sub-delegation must not expand the crew's overall scope. No crew member may delegate tasks to agents outside the Sentinel Crew without PM approval.

## Revocation

David Park may revoke this delegation at any time by updating this file. Revocation takes effect on the next pipeline run. In-progress runs complete under the prior delegation.
