---
title: The conversation becomes the interface
theme: Agents and enterprise systems
order: 3
summary: More contact between people and businesses may happen inside chats and message threads, where an assistant finds, compares and sometimes acts. Referrals, retrieval and purchases are different steps with very different evidence.
updated: 2026-11-13
status: Working draft
replaces: [agents-are-customers, zero-tab-interface]
related: [agent-memory-history, agent-governance]
sources:
  - title: "Adobe, 2025 holiday shopping season results, January 7, 2026"
    url: https://news.adobe.com/news/downloads/pdfs/2026/01/010726-2025-holiday-shopping-season.pdf
  - title: "Agentic Commerce Protocol"
    url: https://www.agenticcommerce.dev/
---
For most of the web's history, a business reached a customer through a page the customer opened. My thesis is that more of that contact will happen inside conversations: a person asks an assistant in a chat or message thread, and the assistant finds, compares and sometimes acts. That needs two things. Assistants need distribution where people already spend time, and businesses need to expose their catalogs, prices and actions in a form an agent can use.

Three behaviors often get lumped together here. Retrieval is an assistant answering a question with information from the web. A referral is a person clicking from that answer through to a business. An autonomous purchase is the agent completing the transaction itself. Each asks something different of a business, and the evidence for each is very different.

<figure class="stat">
<p class="stat-number">+693%</p>
<figcaption>Traffic to US retail sites from generative AI tools in the 2025 holiday season (Nov. 1 to Dec. 31), compared with a year earlier. Source: <a href="https://news.adobe.com/news/downloads/pdfs/2026/01/010726-2025-holiday-shopping-season.pdf">Adobe Analytics</a>, January 7, 2026.</figcaption>
</figure>

That figure is about referrals: people starting in an AI tool and then visiting a store. It says nothing about agents buying on their own. The action side is earlier. The Agentic Commerce Protocol is an open standard for checkout between buyers, AI agents and businesses, in which the business stays in control of what it sells. Standards like this show the plumbing being built, not that people trust agents with their money.

<figure class="narrow">
<a href="/theses/conversation-interface/referral-to-purchase.svg"><img src="/theses/conversation-interface/referral-to-purchase.svg" width="360" height="440" loading="lazy" alt="Conceptual spectrum, not measured evidence. 1. AI referral: a person asks an AI tool, then visits the store; Adobe measured +693% traffic. 2. Information retrieval: an agent reads catalogs, prices and availability. 3. Agent-completed purchase: the agent checks out on the person's behalf; checkout standards such as ACP are early. Each step down adds autonomy and needs more trust."></a>
<figcaption>Conceptual, not measured evidence: three different things an “AI commerce” figure can mean. Only the first is measured here (Adobe, above). My diagram. <a href="/theses/conversation-interface/referral-to-purchase.svg">Open full size</a></figcaption>
</figure>

Messaging is an appealing surface because it needs no new app or login, and many tasks fit a thread: a quick request, a confirmation, a reminder, a simple choice. Detailed comparisons and anything visual fit less well. I built a small [event finder for iMessage](/building/#messaging-event-agent) that suggests events that fit your calendar. It's a prototype that shows the shape of the idea, not evidence that people want it.

Businesses that depend on people seeing their interface, through ads, upsells or onboarding, would feel this first. Those that make their products easy for agents to understand and buy could gain, as could whoever runs identity and payments for agent-initiated purchases. The strongest counterargument is that people keep using assistants for research but still choose and pay on familiar sites, so referrals grow and autonomous purchases stay rare. I'd change my mind if agent-completed purchases stay negligible after checkout standards are widely available, or if messaging platforms close off third-party agents.
