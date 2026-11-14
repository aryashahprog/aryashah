---
title: An agent’s memory needs a history
theme: Agents and enterprise systems
order: 1
summary: In regulated work, an agent’s memory is only useful if it records where each fact came from, how it changed and which facts supported each decision.
updated: 2026-11-13
status: Working draft
replaces: [agents-need-context, data-is-the-moat, agent-system-of-record]
related: [agent-governance, conversation-interface]
sources:
  - title: "W3C, PROV-Overview: An Overview of the PROV Family of Documents, 2013"
    url: https://www.w3.org/TR/prov-overview/
  - title: "Pang et al., “Zanzibar: Google’s Consistent, Global Authorization System,” USENIX ATC 2019"
    url: https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/
---
Agents fail in familiar ways when they lack context. They don't know how a company does things, which document is current or why a rule exists. The usual answer is more memory. My thesis is narrower: in some workflows, memory is only useful if it has a history. That means recording what the agent believed, where it came from, when it changed and which facts supported each decision.

Take a regulated workflow such as a credit limit review or an insurance claim. An agent updates a customer's status, and months later someone asks why. The latest value isn't enough. A reviewer needs the earlier value, the source document, the version of the policy that applied and the step where the agent acted on it. That is provenance plus version history, and neither idea is new: the W3C PROV standard describes provenance as information about the entities, activities and people involved in producing a piece of data. The open question is whether agent memory gets built with it from the start or has it bolted on after an audit goes badly.

Memory and permissions should stay separate. What an agent knows is not the same as what it may do, and access decisions belong in authorization systems built for that job, such as Google's Zanzibar, which handles access control for services like Drive and Calendar. An agent's memory can record that access was granted; it shouldn't be the place where access is granted.

Data is part of this, but it isn't automatically a moat. A lot of company data is messy, duplicated or not very different from a competitor's, and better general models may need less of it. What could be hard to copy is a checked record of how decisions were actually made in one specific workflow.

The likely buyer is a risk or compliance team in a regulated business, because explaining decisions is already their job. That demand is a hypothesis; I haven't tested it with buyers. The strongest counterargument is that agent platforms and existing systems of record will add versioned memory and audit logs as features, leaving no room for a separate product. I'd change my mind if compliance teams accept ordinary application logs as enough to explain an agent's decisions, or if incumbents ship provenance that holds up in a real audit.
