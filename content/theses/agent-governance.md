---
title: Agent governance is a runtime problem
theme: Agents and enterprise systems
order: 2
summary: Agents act while they run, so governing them means scoped authorization, traces, monitoring, revocation and recovery as actions happen, not only policy written in advance.
updated: 2026-11-13
status: Working draft
replaces: [cybersecurity-timelines]
related: [agent-memory-history, conversation-interface]
sources:
  - title: "OWASP GenAI Security Project, LLM06:2025 Excessive Agency"
    url: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
  - title: "IETF RFC 7009, OAuth 2.0 Token Revocation, 2013"
    url: https://www.rfc-editor.org/rfc/rfc7009
---
Most governance is written before software runs: a policy, an approval, a review. Agents make that harder, because the same agent can take different steps on the same input, and its actions happen while it works. My thesis is that agent governance has to operate at runtime: authorization scoped to each task, a trace of what the agent did, monitoring while it acts, a fast way to revoke access and a way to recover when something goes wrong. Three questions frame it:

<figure class="framework">
<dl>
<div><dt>Access</dt><dd>What can each agent reach, and on whose authority?</dd></div>
<div><dt>Visibility</dt><dd>What is it doing, and can anyone see it?</dd></div>
<div><dt>Control</dt><dd>Who can stop it, and how quickly?</dd></div>
</dl>
<figcaption>A framework for the questions, not data.</figcaption>
</figure>

Much of this already exists. Identity and access tools issue scoped, short-lived credentials, and standards such as OAuth 2.0 token revocation define how to cut access off. Security teams already automate a lot of detection and response, and logging and observability tools record what systems do. OWASP's guidance on excessive agency in LLM applications points to the same controls: give an agent only the tools and permissions it needs, and require human approval for high-impact actions.

The possible gap is in tying these together around an agent's task. Existing tools mostly see a service account making calls. They may not see that the calls belong to one agent run, on whose behalf it acted, which step it had reached, or how to undo the three things it already changed when it is stopped halfway. Recovery is the least solved part: revoking a credential stops new actions but doesn't reverse finished ones. Cheaper models help attackers and defenders at once, which raises the stakes, but I don't have numbers on how fast either side is moving, so I'm not leaning on that here.

The natural buyers are security, risk and platform teams who already own access and incident response. The strongest counterargument is that identity, security and observability vendors extend their products to cover agents, and governance becomes a set of features in tools companies already run. I'd drop this if companies running many agents in production can answer the three questions above with their existing stack, including stopping an agent mid-task and undoing its partial work.
