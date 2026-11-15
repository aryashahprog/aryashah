---
title: Agent governance is a runtime problem
theme: Agents and enterprise systems
order: 2
summary: Agents act while they run, so governing them means scoped authorization, traces, monitoring, revocation and recovery as actions happen, not only policy written in advance.
published: 2026-11-13
updated: 2026-11-14
status: Working draft
replaces: [cybersecurity-timelines]
related: [agent-memory-history, conversation-interface]
---
Most governance is written before software runs: a policy, an approval, a review. Agents strain that model. The same agent can take different steps on the same input, and its actions happen while it works.

So **governing agents has to happen at runtime**: authorization scoped to each task, a trace of what the agent did, monitoring while it acts, a quick way to revoke access and a way to recover when something goes wrong. It comes down to three questions.

<figure class="wide">
<a href="/theses/agent-governance/access-visibility-control.svg"><picture><source media="(min-width: 700px)" srcset="/theses/agent-governance/access-visibility-control-wide.svg" width="640" height="165"><img src="/theses/agent-governance/access-visibility-control.svg" width="360" height="313" loading="lazy" alt="Three questions for governing agents. Access: what can each agent reach, and on whose authority? Visibility: what is it doing, and can anyone see it? Control: who can stop it, and how quickly?"></picture></a>
<figcaption>Three questions to ask of any agent running in production. <a href="/theses/agent-governance/access-visibility-control.svg">Open full size</a></figcaption>
</figure>

## Most of the parts already exist

Identity and access tools issue scoped, short-lived credentials, and standards such as OAuth 2.0 token revocation define how to cut access off.[^rfc7009] Security teams already automate a lot of detection and response, and logging and observability tools record what systems do.

OWASP's guidance on excessive agency in LLM applications points to the same controls: give an agent only the tools and permissions it needs, and require human approval for high-impact actions.[^owasp]

## The missing piece is the task

The gap, if there is one, is in tying these together around an agent's task. Existing tools mostly see a service account making calls. They may not see that the calls belong to one agent run, on whose behalf it acted, which step it had reached, or how to undo the three things it already changed when it is stopped halfway.

One way to close part of that gap is to check the action as well as the caller. An identity check confirms who is calling. An intent check asks whether this particular action was in the plan approved for this task, and in that design an out-of-scope action is stopped before it runs.

<figure class="wide">
<a href="/theses/agent-governance/identity-vs-intent.png"><picture><source media="(min-width: 700px)" srcset="/theses/agent-governance/identity-vs-intent-wide.png" width="2760" height="944"><img src="/theses/agent-governance/identity-vs-intent.png" width="1423" height="1573" loading="lazy" alt="Two workflows. Identity check only: agent reasoning, an identity check of who is calling, then the action runs; the credentials were valid but the action itself was never approved. With an intent check: agent reasoning, a signed plan, an intent check of whether the action was in the plan, then the action runs; out-of-scope actions are blocked before they run and logged."></picture></a>
<figcaption>An identity check asks who is calling; an intent check asks whether this action was approved for the task. One possible design, not a validated security guarantee. <a href="/theses/agent-governance/identity-vs-intent.png">Open full size</a></figcaption>
</figure>

## Recovery is the least solved part

Revoking a credential stops new actions but doesn't reverse finished ones. Cheaper models help attackers and defenders at once, which raises the stakes, but I don't have numbers on how fast either side is moving, so I'm not leaning on that here.

Security, risk and platform teams, who already own access and incident response, are the natural buyers. They may never need a separate product. Identity, security and observability vendors could extend what they sell to cover agents, and governance would become a set of features in tools companies already run.

I'd drop this if companies running many agents in production can answer the three questions with their existing stack, including stopping an agent mid-task and undoing its partial work.

[^rfc7009]: IETF, “[RFC 7009: OAuth 2.0 Token Revocation](https://www.rfc-editor.org/rfc/rfc7009),” 2013.
[^owasp]: OWASP GenAI Security Project, “[LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/).”
