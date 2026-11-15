---
title: An agent’s memory needs a history
theme: Agents and enterprise systems
order: 1
summary: A company can rent models but own what its workflows learn, if each correction, rule and outcome is kept with its source, history and permissions.
updated: 2026-11-14
status: Working draft
replaces: [agents-need-context, data-is-the-moat, agent-system-of-record]
related: [agent-governance, conversation-interface]
source_note: Based on adaptive-context research from September 2026
---
Agents fail in familiar ways when they lack context. They don't know how a company does things, which document is current or why a rule exists.

The usual answer is more memory. In many workflows, though, **memory is only useful if it has a history**: what the agent believed, where that came from, when it changed and which facts supported each decision.

## What a company can own

Competitors can buy the same models. What they can't buy is a company's own corrections, rules and outcomes, if those are kept as reusable knowledge with a record of where each came from, who may use it and whether it worked.

A company can own that context and its workflows while renting model access, and switch providers without losing it. That doesn't mean every company should own the whole stack.

In Theory Ventures' picture of the harness, the model is the disposable layer and the trace around it is what lasts.[^harness]

<figure>
<a href="/theses/agent-memory-history/who-holds-the-reins.png"><img src="/theses/agent-memory-history/who-holds-the-reins.png" width="1800" height="952" loading="lazy" alt="Theory Ventures diagram, Who Holds the Reins? An enterprise sends prompts and context to a harness, such as Claude Code, Codex, Cursor or Grok Build, which decides what to send to a frontier model and what to hold back, and logs every session trace. The frontier model is labelled the disposable layer, swapped each generation, while the trace outlives it. A training loop sends logged traces to train the next model."></a>
<figcaption>Models get swapped; the context and feedback around them can outlive any one model. Not every harness trains models, training on traces depends on contracts and permissions, and running a harness doesn’t by itself confer rights to the data. Diagram: Theory Ventures, via Tomasz Tunguz, <a href='https://tomtunguz.com/the-harness-is-the-new-battleground/'>“The Harness Is the New Battleground”</a>. <a href="/theses/agent-memory-history/who-holds-the-reins.png">Open full size</a></figcaption>
</figure>

I'd put the company at the center instead. It rents the model, and what its workflows learn stays with it for the next run.

<figure class="wide">
<a href="/theses/agent-memory-history/company-context-loop.svg"><picture><source media="(min-width: 700px)" srcset="/theses/agent-memory-history/company-context-loop-wide.svg" width="640" height="285"><img src="/theses/agent-memory-history/company-context-loop.svg" width="360" height="472" loading="lazy" alt="The company keeps what its workflows learn. 1. Model access, rented and replaceable. 2. Workflow execution, agents complete real tasks. 3. Retained company context: corrections, rules and outcomes with provenance and permissions. 4. Improved workflow, the next run uses what was learned. Feedback from each run loops back into execution."></picture></a>
<figcaption>The company rents model access and keeps what its workflows learn. <a href="/theses/agent-memory-history/company-context-loop.svg">Open full size</a></figcaption>
</figure>

## A booking you can explain later

A hypothetical clinic scheduling agent shows what that takes. Answering a question about open slots is easy. Completing the work means identifying the patient, applying the practice's rules, getting approval, saving the appointment and checking that it saved.

When staff correct it, the correction should improve the next booking rather than disappear into a chat log. If someone later asks why a booking was made, the record should show which rule and which version applied. The W3C's PROV standard already describes this kind of provenance.[^prov]

## Memory doesn't grant access

What an agent knows is not what it may do. Access decisions belong in authorization systems built for that job, such as Google's Zanzibar.[^zanzibar] Memory can record that access was granted; it shouldn't grant it.

Where the model runs is a separate choice too. On-device, on-premises, private cloud and disconnected setups trade privacy against cost, upkeep and quality. Running locally isn't a moat or a security guarantee on its own, and neither is data. Data helps only if it improves an outcome, the company may use it and someone keeps it current.

I'd expect the first buyers to be risk and compliance teams in regulated businesses, since explaining decisions is already their job, though I haven't tested that. The obvious objection is that agent platforms and systems of record will add versioned memory and audit logs as features. I'd change my mind if compliance teams accept ordinary application logs as enough to explain an agent's decisions, or if incumbents ship provenance that holds up in a real audit.

[^harness]: The diagram is credited to Theory Ventures and appears in Tomasz Tunguz, “[The Harness Is the New Battleground](https://tomtunguz.com/the-harness-is-the-new-battleground/).”
[^prov]: W3C, “[PROV-Overview: An Overview of the PROV Family of Documents](https://www.w3.org/TR/prov-overview/),” 2013. PROV defines provenance as information about the entities, activities and people involved in producing a piece of data.
[^zanzibar]: Pang et al., “[Zanzibar: Google’s Consistent, Global Authorization System](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/),” USENIX ATC 2019.
