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

One task is rarely one call. An agent plans, calls tools, reads the results, retries when something fails and checks its own work, so the cost of a task depends on how many steps it takes and how often it starts over, not only on the price of each step. Cheaper tokens also invite new uses. A falling price per token therefore says little about the total bill: it can fall because the same work got cheaper or rise because there is more work. I don't have data that settles which is more common, and I'm not assuming bills rise.

Engineering choices move the cost side a lot. AT&T says its AI gateway, which uses cache-aware routing to send each request to a cost-effective model, has cut its AI costs by as much as 90% while handling about 45 billion tokens a day. That's the company's own figure for its own setup, but it shows that how work is routed can matter as much as list prices.

The return side is harder to see in aggregate data so far:

<figure class="tall">
<a href="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png"><img src="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png" width="1700" height="3600" loading="lazy" alt="Three scatter plots of US sectors, annualized labor productivity growth against the share of firms using AI in 2026 H1. Latest period, 2022 Q4 to 2025 Q4: weak upward fit, R squared 0.18. Pre-pandemic, 2016 Q4 to 2019 Q4: similar upward fit, R squared 0.21. Latest minus pre-pandemic: flat fit, R squared 0.00."></a>
<figcaption>Sectors that use more AI grew faster recently, but they also grew faster before generative AI existed; net of that earlier trend, the fit is about zero. Early, sector-level data about returns, not about token prices or spending, and not evidence that AI adds no value. Chart: Ernie Tedeschi, <a href="https://www.stripeeconomics.com/p/ai-and-productivity">“AI and productivity”</a>, Stripe Economics, July 23, 2026. Data: Census Bureau (BTOS), Bureau of Labor Statistics, Federal Reserve Bank of Chicago, Stripe analysis; mining excluded. <a href="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png">Open full size</a></figcaption>
</figure>

If returns don't show up in totals yet, they have to be measured where the work happens, one workflow at a time.

Cloud is a useful comparison, with limits. It turned capacity into something rented and pushed companies to track spend by service and team; AI may push the same discipline down to the task. The analogy doesn't tell me models will commoditize or that applications will capture most of the value. Frontier models still differ in capability, and model companies also sell applications.

If this is right, finance and operations teams running agents at scale would pay for tools that tie cost to outcome per workflow, and vendors who can price by outcome would have an edge. The strongest counterargument is that existing cloud cost and observability tools already tag usage well enough, so per-task accounting stays a feature. I'd drop the thesis if teams that measure AI per workflow make no better decisions about what to run than teams that only watch the monthly bill.
