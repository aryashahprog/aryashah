---
title: Cheap software shifts value beyond the build
theme: AI economics
order: 2
summary: As simple software gets cheap to build, value moves to what surrounds the code. Distribution, domain access, integration, maintenance and trust.
updated: 2026-11-13
status: Working draft
related: [workflow-economics]
---
Building simple software is getting much cheaper. Someone who can describe a tool clearly can often get a working version in an afternoon, which changes the build-or-buy decision for small, single-purpose tools. My thesis is that this moves value away from the act of building and toward everything around it.

There is a temporary arbitrage in that. While the tools are new and unevenly used, people who build quickly can make something useful before others notice the opportunity. The window narrows as more people use the same tools and the obvious gaps get filled.

The more lasting effect is a split between disposable and durable software. A disposable tool solves one person's problem this week; if it breaks, they rebuild it or move on. A durable business has to keep working for other people for years. It has to integrate with the systems they already use, keep up as those systems change, offer support when something goes wrong and earn trust with their data. Cheaper code lowers the cost of the first version far more than the cost of the rest. Distribution still decides who hears about a product, and domain access still decides who understands a problem well enough to solve the right one.

<figure class="narrow">
<a href="/theses/arbitrage-window/beyond-the-build.svg"><img src="/theses/arbitrage-window/beyond-the-build.svg" width="360" height="512" loading="lazy" alt="Conceptual, not measured evidence. Building the first version is much cheaper with AI coding tools. Still needed for a durable product: distribution, who hears about it; domain access, knowing which problem to solve; integration, fitting the systems people use; maintenance, keeping up as those change; trust, meaning support, reliability and care with data."></a>
<figcaption>Conceptual, not measured evidence: cheaper code shrinks the first step, not the five after it. My diagram. <a href="/theses/arbitrage-window/beyond-the-build.svg">Open full size</a></figcaption>
</figure>

This isn't a claim that anyone can build anything. Complex, regulated or high-reliability software still needs expertise, testing and someone accountable for it, and a working demo is not the same as a product people depend on.

<figure class="tall">
<a href="/theses/arbitrage-window/build-vs-operate.png"><img src="/theses/arbitrage-window/build-vs-operate.png" width="1360" height="1923" loading="lazy" alt="Illustrative comparison. Unmanaged app: employee, coding agent, production, with no SSO, no audit trail, unknown data access and unknown cost. Proposed managed deployment: employee, coding agent, a managed platform, then production, with enterprise SSO, audit logging, scoped data sources and cost per user."></a>
<figcaption>Building looks the same in both columns; operating doesn’t. Once an employee-built app reaches production, someone has to own sign-in, approved data access, an audit trail and its cost. Illustrative, adapted from one of my slides, with a product name replaced by a generic managed platform. <a href="/theses/arbitrage-window/build-vs-operate.png">Open full size</a></figcaption>
</figure>

The people who benefit are individuals and small teams building tools for their own work, and businesses whose value already sits in distribution, integrations, data or trust rather than in the code. The most exposed are simple, single-purpose products sold mainly on features that are now cheap to reproduce.

The strongest counterargument is that self-built tools cost more to maintain than people expect, so most teams drift back to buying, and the window closes almost as soon as it opens. I'd change my mind if, two years from now, small teams still aren't replacing purchased tools with their own in any meaningful number, or if the cost of building simple software stops falling.
