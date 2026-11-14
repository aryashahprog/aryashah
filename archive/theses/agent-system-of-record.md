---
title: Agent system of record
theme: Enterprise agent infrastructure
order: 4
summary: Agents working across silos may need narrow cross-system permissions plus versioned memory that keeps why a fact changed. Risk and compliance teams in regulated workflows could be the buyer.
updated: 2026-11-13
status: First draft
related: [agents-need-context, agent-governance, data-is-the-moat]
---
## The claim

As agents work across departments, companies may need a system of record built for them. Two parts: narrow permissions that cross silos, and versioned memory that keeps why a fact changed, not only its latest value.

## Reasoning

- Agents are most useful when they can work across silos, but broad access is exactly what risk teams won't allow. Narrow, task-specific permissions across systems are a possible middle ground.
- When an agent updates a fact, such as a customer's status or a limit, the latest value isn't enough in a regulated workflow. Someone will want to know when it changed, what changed it and why.
- Risk and compliance teams in regulated workflows could be the buyer, since they already care about audit trails.

## Where this could fall short

Generic memory or checkpointing on its own may end up as a feature of agent platforms rather than a product. The more defensible version is probably tied to permissions and auditability inside a specific regulated workflow.

## How this differs from related notes

[Agents fail without context](/theses/agents-need-context/) is about what agents need to know. [Agent governance](/theses/agent-governance/) is about rules and accountability for what they do. This note is about the record itself: who was allowed to touch what, and the history of why facts changed.

## Where value might accrue

- A system that becomes the place compliance teams check to explain an agent's actions.
- Vertical products in regulated workflows where that record is required.

## What would change my mind

- Agent platforms shipping permissions and versioned memory that are good enough for compliance teams.
- Compliance teams accepting existing logs as sufficient.
