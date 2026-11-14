---
title: An agent’s memory needs a history
theme: Agents and enterprise systems
order: 1
summary: A company can rent models but own what its workflows learn, if each correction, rule and outcome is kept with its source, history and permissions.
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
Agents fail in familiar ways when they lack context. They don't know how a company does things, which document is current or why a rule exists. The usual answer is more memory. My thesis is narrower: in many workflows, memory is only useful if it has a history. That means recording what the agent believed, where it came from, when it changed and which facts supported each decision.

Competitors can buy the same models. What they can't buy is a company's own corrections, rules and outcomes, if those are kept as reusable knowledge with a record of where each came from, who may use it and whether it worked. A company can own that context and its workflows while renting model access, and switch providers without losing it. That doesn't mean every company should own the whole stack.

<figure class="narrow">
<img src="/theses/agent-memory-history/company-context-loop.svg" width="360" height="520" alt="Proposed framework, not measured evidence: 1. Model access, rented and replaceable. 2. Workflow execution, agents complete real tasks. 3. Retained company context, corrections, rules and outcomes with provenance and permissions. 4. Improved workflow, the next run uses what was learned. Feedback from each run loops back into execution.">
<figcaption>A proposed framework, not measured evidence: the company rents model access but keeps what its workflows learn. My diagram, adapted from one of my slides.</figcaption>
</figure>

Take a hypothetical clinic scheduling agent. Answering a question about open slots is easy. Completing the work means identifying the patient, applying the practice's rules, getting approval, saving the appointment and checking that it saved. When staff correct it, the correction should improve the next booking rather than disappear into a chat log. And if someone later asks why a booking was made, the record should show which rule and which version applied. The W3C PROV standard already describes this kind of provenance, as information about the entities, activities and people involved in producing a piece of data.

Memory and permissions should stay separate. What an agent knows is not what it may do, and access decisions belong in authorization systems built for that job, such as Google's Zanzibar. Memory can record that access was granted; it shouldn't grant it.

Where the model runs is a separate choice. On-device, on-premises, private cloud and fully disconnected setups trade privacy against cost, upkeep and quality. Running locally isn't a moat or a security guarantee on its own, and neither is data: it becomes an advantage only if it improves an outcome, the company may use it and someone keeps it current.

The likely first buyer is a risk or compliance team in a regulated business, because explaining decisions is already their job. That demand is a hypothesis I haven't tested. The strongest counterargument is that agent platforms and existing systems of record will add versioned memory and audit logs as features. I'd change my mind if compliance teams accept ordinary application logs as enough to explain an agent's decisions, or if incumbents ship provenance that holds up in a real audit.
