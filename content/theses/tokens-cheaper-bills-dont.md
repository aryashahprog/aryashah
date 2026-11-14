---
title: Tokens get cheaper, AI bills don’t
theme: AI economics
order: 1
summary: Cost per token keeps falling, but enterprise AI bills may stay flat or rise as agents use far more of them. Measure ROI per agent or workflow, not per token.
updated: 2026-11-13
status: First draft
related: [ai-repeats-the-cloud-arc, arbitrage-window]
---
## The claim

The price of a token keeps falling, but a company's total AI bill may stay flat or go up. Cheaper tokens invite much more usage, especially from agents. So the useful question isn't "what does a token cost?" but "what does this agent or workflow cost, and what does it return?"

## Reasoning

- When something gets cheaper, people usually find more ways to use it. I'd expect the same here.
- Agents push this further. One task can involve many model calls: planning, using tools, retrying, checking its own work. A team might go from a few prompts a day to thousands of calls without anyone deciding to "use more AI."
- So a falling price per token and a rising total bill don't contradict each other. Both can be true.
- If that's right, price per token says little about whether AI is paying off. A finance team would rather know what a workflow costs end to end and what it replaces or produces.

What I'm assuming: that usage grows faster than prices fall. I haven't checked that against real enterprise spending.

The payoff side is also hard to see in aggregate data so far. Stripe Economics compared AI adoption across US sectors with labor productivity growth:

<figure class="tall">
<a href="/theses/tokens-cheaper-bills-dont/sector-productivity-vs-ai-adoption.png"><img src="/theses/tokens-cheaper-bills-dont/sector-productivity-vs-ai-adoption.png" width="1700" height="3600" loading="lazy" alt="Three scatter plots of US sectors, annualized labor productivity growth against the share of firms using AI in 2026 H1. Latest period, 2022 Q4 to 2025 Q4: weak upward fit, R squared 0.18. Pre-pandemic, 2016 Q4 to 2019 Q4: similar upward fit, R squared 0.21. Latest minus pre-pandemic: flat fit, R squared 0.00."></a>
<figcaption>Sectors that use more AI grew faster recently, but they also grew faster before generative AI existed; net of that earlier trend, the fit is about zero. This is early, sector-level data, not evidence that AI adds no value. Chart: Ernie Tedeschi, <a href="https://www.stripeeconomics.com/p/ai-and-productivity">“AI and productivity”</a>, Stripe Economics, July 23, 2026. Data: Census Bureau (BTOS), Bureau of Labor Statistics, Federal Reserve Bank of Chicago, Stripe analysis; mining excluded. <a href="/theses/tokens-cheaper-bills-dont/sector-productivity-vs-ai-adoption.png">Open full size</a></figcaption>
</figure>

That's one more reason to measure cost and return per workflow rather than wait for it to show up in totals.

## Where value might accrue

- Tools that track cost and outcome per agent or per workflow, so a team can see which ones are worth running.
- Vendors who can price by the outcome a workflow delivers rather than by usage.
- Workflows where one agent run replaces enough human time that a bigger bill is still a good deal.

## What would change my mind

- Enterprise AI spend falling roughly in line with token prices as adoption matures.
- Usage leveling off once the obvious workflows are automated.
- Existing cloud cost tools turning out to handle per-workflow ROI well enough that nothing new is needed.
