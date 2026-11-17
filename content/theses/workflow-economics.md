---
title: The workflow is the unit of AI economics
theme: AI economics
order: 1
summary: The price of a token is the wrong unit. What matters is the full cost of a completed, useful task and what it produced.
started: 2026-11-01
updated: 2026-11-14
status: Working draft
replaces: [tokens-cheaper-bills-dont, ai-repeats-the-cloud-arc]
related: [arbitrage-window, agentic-operations-research]
---
The price of a token is the number everyone quotes, but it isn't what a business buys. A company pays for finished work: a resolved ticket, a reconciled invoice, a contract draft a lawyer accepts.

**The useful unit of AI economics is the cost of a completed, useful task**, and most of the decisions worth making sit at that level.

## One task, many calls

An agent plans, calls tools, reads the results, retries when something fails and checks its own work. Then a person often reviews the output and fixes what's wrong. The cost of a successful task includes the failed attempts and that review and rework.

Cheaper tokens also invite longer tasks and new uses, so a falling price per token says little about the total bill.

<figure>
<a href="/theses/workflow-economics/token-price-vs-bill-illustration.png"><img src="/theses/workflow-economics/token-price-vs-bill-illustration.png" width="1099" height="465" loading="lazy" alt="A sketch with no scale: on the left a line labeled cost per token falls; on the right a line labeled your total bill rises; a question mark sits between them."></a>
<figcaption>Lower token prices can be offset by more calls, retries and longer tasks, so the bill can rise. It can also fall when the same work simply gets cheaper. <a href="/theses/workflow-economics/token-price-vs-bill-illustration.png">Open full size</a></figcaption>
</figure>

I don't have data that settles which is more common, so I'm not assuming bills rise.

<figure class="signal">
<a href="https://x.com/AnthropicAI/status/1949898502688903593" target="_blank" rel="noopener noreferrer" aria-label="Read Anthropic's original weekly rate-limit announcement on X"><img src="/theses/signals/claude-rate-limits.png" width="554" height="154" loading="lazy" alt="Anthropic announces new weekly limits for Claude Pro and Max, estimating that they will affect fewer than five percent of subscribers based on then-current usage."></a>
<figcaption><strong class="signal-label">A familiar signal: Claude's weekly usage limits</strong>Anthropic's announcement is a reminder that a subscription price does not describe an unlimited workload. How many tasks agents run, how long they run and how often they retry still matter; this post alone does not measure cost per successful task.<span class="signal-attribution">Anthropic, July 28, 2025. Screenshot excerpt; illustration omitted.</span> <a class="signal-source" href="https://x.com/AnthropicAI/status/1949898502688903593" target="_blank" rel="noopener noreferrer">Read the original post ↗</a> <a href="/theses/signals/claude-rate-limits.png">Open screenshot full size</a></figcaption>
</figure>

## Routing is a lever

A smaller, cheaper model may be good enough for a routine step, but someone has to define good enough for that task and check it, or the savings come back as rework.

AT&T says its AI gateway, which uses cache-aware routing to send each request to a cost-effective model, has cut its AI costs by as much as 90% while handling about 45 billion tokens a day.[^att] Routing is only one layer. The model, the runtime that serves it and the cluster underneath can each be made cheaper too.

<figure class="wide">
<a href="/theses/workflow-economics/inference-optimization-stack.svg"><picture><source media="(min-width: 700px)" srcset="/theses/workflow-economics/inference-optimization-stack-wide.svg" width="640" height="220"><img src="/theses/workflow-economics/inference-optimization-stack.svg" width="360" height="399" loading="lazy" alt="The LLM inference optimization stack. Layer 1, model: compress and redesign the weights, through pruning, quantization, distillation and mixture-of-experts or state-space architectures. Layer 2, runtime: serve and decode faster per request, through serving engines, speculative decoding, KV caching and kernels. Layer 3, infrastructure: share and route the cluster, through GPU orchestration, utilization and compute marketplaces."></picture></a>
<figcaption>Three layers where inference can be made cheaper, besides the price per token. From my AI compute trend brief. <a href="/theses/workflow-economics/inference-optimization-stack.svg">Open full size</a></figcaption>
</figure>

## Returns are harder to see

In Stripe's sector data, industries that use more AI have grown productivity faster recently, but they were also growing faster before generative AI existed.[^stripe]

<figure class="narrow">
<a href="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png"><img src="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png" width="1700" height="3600" loading="lazy" alt="Three scatter plots of US sectors, annualized labor productivity growth against the share of firms using AI in 2026 H1. Latest period, 2022 Q4 to 2025 Q4: weak upward fit, R squared 0.18. Pre-pandemic, 2016 Q4 to 2019 Q4: similar upward fit, R squared 0.21. Latest minus pre-pandemic: flat fit, R squared 0.00."></a>
<figcaption>Net of the earlier trend, the fit is about zero. That is early sector-level data, not evidence that AI adds no value. Chart: Ernie Tedeschi, <a href='https://www.stripeeconomics.com/p/ai-and-productivity'>“AI and productivity”</a>, Stripe Economics, July 23, 2026. Data: Census Bureau (BTOS), Bureau of Labor Statistics, Federal Reserve Bank of Chicago, Stripe analysis; mining excluded. <a href="/theses/workflow-economics/sector-productivity-vs-ai-adoption.png">Open full size</a></figcaption>
</figure>

If returns don't show up in the totals yet, they have to be measured where the work happens, one workflow at a time. Cloud pushed companies to track spend by service and team, and AI may push that discipline down to the task. The comparison has limits: it doesn't tell me models will commoditize or that applications will capture most of the value.

Finance and operations teams running agents at scale would pay for tools that tie cost, including review time, to the outcome of each workflow, and vendors who can price by outcome would have an edge.

It could just as easily stay a feature of existing cloud cost and observability tools. I'd drop the idea if teams that measure AI per workflow make no better decisions about what to run than teams that only watch the monthly bill.

[^att]: AT&T, “[The tokenomics equation](https://about.att.com/blogs/2026/the-tokenomics-equation.html),” 2026. The figure is the company's own, for its own setup.
[^stripe]: Ernie Tedeschi, “[AI and productivity](https://www.stripeeconomics.com/p/ai-and-productivity),” Stripe Economics, July 23, 2026. This is early, sector-level data about returns, not about token prices or spending.
