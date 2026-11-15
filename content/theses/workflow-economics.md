---
title: The workflow is the unit of AI economics
theme: AI economics
order: 1
summary: The price of a token is the wrong unit. What matters is the full cost of a completed, useful task and what it produced.
updated: 2026-11-14
status: Working draft
replaces: [tokens-cheaper-bills-dont, ai-repeats-the-cloud-arc]
related: [arbitrage-window, agentic-operations-research]
---
The price of a token is the number everyone quotes, but it isn't what a business buys. A company pays for finished work: a resolved ticket, a reconciled invoice, a contract draft a lawyer accepts. The useful unit of AI economics is the cost of a completed, useful task, and most of the decisions worth making sit at that level.

One task is rarely one call. An agent plans, calls tools, reads the results, retries when something fails and checks its own work, and then a person often reviews the output and fixes what's wrong. The cost of a successful task includes the failed attempts and that review and rework, not just the price of each call. Cheaper tokens also invite longer tasks and new uses, so a falling price per token says little about the total bill.

<figure>
<a href="/theses/workflow-economics/token-price-vs-bill-illustration.png"><img src="/theses/workflow-economics/token-price-vs-bill-illustration.png" width="1099" height="465" loading="lazy" alt="Illustration with no data or scale: on the left a line labeled cost per token falls; on the right a line labeled your total bill rises; a question mark sits between them."></a>
<figcaption>An illustration, not measured data. Lower token prices can be offset by more calls, retries and longer tasks, so the bill can rise, but it can also fall when the same work simply gets cheaper. <a href="/theses/workflow-economics/token-price-vs-bill-illustration.png">Open full size</a></figcaption>
</figure>

I don't have data that settles which is more common, so I'm not assuming bills rise.

Choosing the model for each task is one of the bigger levers. A smaller, cheaper model may be good enough for a routine step, but someone has to define good enough for that task and check it, or the savings come back as rework. AT&T says its AI gateway, which uses cache-aware routing to send each request to a cost-effective model, has cut its AI costs by as much as 90% while handling about 45 billion tokens a day.[^att] Routing can matter as much as list prices, and it is only one layer. The model itself, the runtime that serves it and the cluster underneath can each be made cheaper too.

<figure>
<a href="/theses/workflow-economics/inference-optimization-stack.png"><img src="/theses/workflow-economics/inference-optimization-stack.png" width="1037" height="1355" loading="lazy" alt="Three layers of LLM inference optimization. Layer 1, model: compress and redesign the weights, through pruning, quantization, distillation and mixture-of-experts or state-space architectures. Layer 2, runtime: serve and decode faster per request, through serving engines, speculative decoding, KV caching and kernels. Layer 3, infrastructure: share and route the cluster, through GPU orchestration, utilization and compute marketplaces."></a>
<figcaption>Price per token isn’t the only cost lever: the model, the serving runtime and the shared infrastructure can each be optimized. A map of mechanisms, not a measure of savings. From my AI compute trend brief. <a href="/theses/workflow-economics/inference-optimization-stack.png">Open full size</a></figcaption>
</figure>

Returns are harder to see. In Stripe's sector data, industries that use more AI have grown productivity faster recently, but they were also growing faster before generative AI existed.[^stripe]

<figure class="narrow">
<a href="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png"><img src="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png" width="1700" height="3600" loading="lazy" alt="Three scatter plots of US sectors, annualized labor productivity growth against the share of firms using AI in 2026 H1. Latest period, 2022 Q4 to 2025 Q4: weak upward fit, R squared 0.18. Pre-pandemic, 2016 Q4 to 2019 Q4: similar upward fit, R squared 0.21. Latest minus pre-pandemic: flat fit, R squared 0.00."></a>
<figcaption>Sectors that use more AI grew faster recently, but they also grew faster before generative AI existed; net of that earlier trend, the fit is about zero. Early sector-level data on returns, not on token prices or spending, and not evidence that AI adds no value. Chart: Ernie Tedeschi, <a href="https://www.stripeeconomics.com/p/ai-and-productivity">“AI and productivity”</a>, Stripe Economics, July 23, 2026. Data: Census Bureau (BTOS), Bureau of Labor Statistics, Federal Reserve Bank of Chicago, Stripe analysis; mining excluded. <a href="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png">Open full size</a></figcaption>
</figure>

If returns don't show up in the totals yet, they have to be measured where the work happens, one workflow at a time. Cloud is a useful comparison, with limits. It pushed companies to track spend by service and team, and AI may push that discipline down to the task. It doesn't tell me models will commoditize or that applications will capture most of the value.

If this is right, finance and operations teams running agents at scale would pay for tools that tie cost, including review time, to the outcome of each workflow, and vendors who can price by outcome would have an edge. It could just as easily stay a feature, if existing cloud cost and observability tools already tag usage well enough. I'd drop the idea if teams that measure AI per workflow make no better decisions about what to run than teams that only watch the monthly bill.

[^att]: AT&T, “[The tokenomics equation](https://about.att.com/blogs/2026/the-tokenomics-equation.html),” 2026. The figure is the company's own, for its own setup.
[^stripe]: Ernie Tedeschi, “[AI and productivity](https://www.stripeeconomics.com/p/ai-and-productivity),” Stripe Economics, July 23, 2026. This is early, sector-level data about returns, not about token prices or spending.
