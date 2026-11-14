---
title: Agent governance
theme: Enterprise agent infrastructure
order: 3
summary: Agents behave less predictably than normal software, which leaves accountability unclear. That could create demand for governance written as code and for operational resilience.
updated: 2026-11-13
status: First draft
related: [agent-system-of-record, agents-need-context]
---
## The claim

Agents don't always behave the same way twice, and when one gets something wrong it isn't clear who is accountable. Companies will need governance that is built into how agents run, not just written in a policy document.

## Reasoning

- Traditional software does what its code says, and when it breaks you can usually trace why. An agent can take a different path on the same input.
- When an agent approves, sends or changes something, who owns that decision: the team that deployed it, the vendor or the person who asked it to act?
- Companies that can't answer that will probably limit what agents are allowed to do. Clearer accountability could unlock more use.
- Governance as code means writing the rules (what an agent can touch, when it needs a human, what gets logged) as policies that are enforced automatically.
- Operational resilience is the other half: what happens when an agent fails halfway through a task, and can the business keep running?

Three questions a company should be able to answer for every agent:

<figure class="framework">
<dl>
<div><dt>Access</dt><dd>What can each agent reach, and on whose authority?</dd></div>
<div><dt>Visibility</dt><dd>What is it doing, and can anyone see it?</dd></div>
<div><dt>Control</dt><dd>Who can stop it, and how quickly?</dd></div>
</dl>
<figcaption>A framework for the questions, not data.</figcaption>
</figure>

## Where value might accrue

- Policy and control layers that sit between agents and the systems they act on.
- Tools that make agent actions auditable and reversible.
- Risk and compliance teams may be the natural buyers, since accountability is already their job.

## What would change my mind

- Existing identity, access and audit tools stretching to cover agents without much change.
- Agents becoming predictable enough that the accountability question fades.
