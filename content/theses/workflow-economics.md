---
title: The workflow is the unit of AI economics
theme: AI economics
order: 1
summary: The price of a token is the wrong unit. What matters is the full cost of a completed, useful task and what it produced.
updated: 2026-11-13
status: Working draft
replaces: [tokens-cheaper-bills-dont, ai-repeats-the-cloud-arc]
related: [arbitrage-window, agentic-operations-research]
sources:
  - title: "AT&T, “The tokenomics equation,” 2026"
    url: https://about.att.com/blogs/2026/the-tokenomics-equation.html
  - title: "Ernie Tedeschi, “AI and productivity,” Stripe Economics, July 23, 2026"
    url: https://www.stripeeconomics.com/p/ai-and-productivity
---
The price of a token is the number everyone quotes, but it isn't what a business is buying. A company pays for finished work: a resolved ticket, a reconciled invoice, a contract draft a lawyer accepts. My working thesis is that the unit of AI economics is the cost of a completed, useful task, and that most of the decisions worth making sit at that level.

One task is rarely one call. An agent plans, calls tools, reads the results, retries when something fails and checks its own work, and a person often reviews the output and fixes what's wrong. The cost of a successful task includes the failed attempts and that review and rework, not only the price of each call. Cheaper tokens also invite longer tasks and new uses, so a falling price per token says little about the total bill.

<figure>
<a href="/theses/workflow-economics/token-price-vs-bill-illustration.png"><img src="/theses/workflow-economics/token-price-vs-bill-illustration.png" width="1099" height="465" loading="lazy" alt="Illustration with no data or scale: on the left a line labeled cost per token falls; on the right a line labeled your total bill rises; a question mark sits between them."></a>
<figcaption>An illustration, not measured data. Lower token prices can be offset by more calls, retries and longer tasks, so the bill can rise, but it can also fall when the same work simply gets cheaper. From one of my slides. <a href="/theses/workflow-economics/token-price-vs-bill-illustration.png">Open full size</a></figcaption>
</figure>

I don't have data that settles which is more common, and I'm not assuming bills rise.

Choosing the model for each task is one of the biggest levers. A smaller, cheaper model may be good enough for a routine step, but someone has to define good enough for that task and check it, or the savings come back as rework. AT&T says its AI gateway, which uses cache-aware routing to send each request to a cost-effective model, has cut its AI costs by as much as 90% while handling about 45 billion tokens a day. That's the company's own figure for its own setup, but it shows that routing can matter as much as list prices.

The return side is harder to see in aggregate data so far:

<figure class="tall">
<a href="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png"><img src="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png" width="1700" height="3600" loading="lazy" alt="Three scatter plots of US sectors, annualized labor productivity growth against the share of firms using AI in 2026 H1. Latest period, 2022 Q4 to 2025 Q4: weak upward fit, R squared 0.18. Pre-pandemic, 2016 Q4 to 2019 Q4: similar upward fit, R squared 0.21. Latest minus pre-pandemic: flat fit, R squared 0.00."></a>
<figcaption>Sectors that use more AI grew faster recently, but they also grew faster before generative AI existed; net of that earlier trend, the fit is about zero. Early, sector-level data about returns, not about token prices or spending, and not evidence that AI adds no value. Chart: Ernie Tedeschi, <a href="https://www.stripeeconomics.com/p/ai-and-productivity">“AI and productivity”</a>, Stripe Economics, July 23, 2026. Data: Census Bureau (BTOS), Bureau of Labor Statistics, Federal Reserve Bank of Chicago, Stripe analysis; mining excluded. <a href="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png">Open full size</a></figcaption>
</figure>

If returns don't show up in totals yet, they have to be measured where the work happens, one workflow at a time.

Cloud is a useful comparison, with limits: it pushed companies to track spend by service and team, and AI may push that discipline down to the task. It doesn't tell me models will commoditize or that applications will capture most of the value.

If this is right, finance and operations teams running agents at scale would pay for tools that tie cost, including review time, to outcome per workflow, and vendors who can price by outcome would have an edge. The strongest counterargument is that existing cloud cost and observability tools already tag usage well enough, so per-task accounting stays a feature. I'd drop the thesis if teams that measure AI per workflow make no better decisions about what to run than teams that only watch the monthly bill.
