---
title: Cheap software shifts value beyond the build
theme: AI economics
order: 2
summary: As simple software gets cheap to build, value moves to what surrounds the code. Distribution, domain access, integration, maintenance and trust.
updated: 2026-11-14
status: Working draft
related: [workflow-economics]
---
Building simple software is getting much cheaper. Someone who can describe a tool clearly can often get a working version in an afternoon, which changes the build-or-buy decision for small, single-purpose tools. What it doesn't change much is everything around the code, and that is where I think the value moves.

For now there is an arbitrage in it. While the tools are new and unevenly used, people who build quickly can make something useful before others notice the opportunity. The window narrows as more people use the same tools and the obvious gaps get filled.

The more lasting effect is a split between disposable and durable software. A disposable tool solves one person's problem this week; if it breaks, they rebuild it or move on. A durable product has to keep working for other people for years. It has to fit the systems they already use, keep up as those systems change, offer support when something goes wrong and earn trust with their data. Cheaper code lowers the cost of the first version far more than the cost of the rest. Distribution still decides who hears about a product, and domain access still decides who understands a problem well enough to solve the right one.

<figure class="narrow">
<a href="/theses/arbitrage-window/beyond-the-build.svg"><img src="/theses/arbitrage-window/beyond-the-build.svg" width="360" height="512" loading="lazy" alt="Conceptual, not measured evidence. Building the first version is much cheaper with AI coding tools. Still needed for a durable product: distribution, who hears about it; domain access, knowing which problem to solve; integration, fitting the systems people use; maintenance, keeping up as those change; trust, meaning support, reliability and care with data."></a>
<figcaption>Conceptual, not measured evidence: cheaper code shrinks the first step, not the five after it. My diagram. <a href="/theses/arbitrage-window/beyond-the-build.svg">Open full size</a></figcaption>
</figure>

The difference shows up as soon as a tool leaves the person who built it. Say an employee uses a coding agent to make an app their team starts relying on. Building it takes the same effort either way. Running it for other people doesn't: someone has to own sign-in, decide which data it may touch, keep an audit trail and pay for it.

<figure class="tall">
<a href="/theses/arbitrage-window/build-vs-operate.png"><img src="/theses/arbitrage-window/build-vs-operate.png" width="1360" height="1923" loading="lazy" alt="Illustrative comparison. Unmanaged app: employee, coding agent, production, with no SSO, no audit trail, unknown data access and unknown cost. Proposed managed deployment: employee, coding agent, a managed platform, then production, with enterprise SSO, audit logging, scoped data sources and cost per user."></a>
<figcaption>Building looks the same in both columns; operating doesn’t. Once an employee-built app reaches production, someone has to own sign-in, approved data access, an audit trail and its cost. Illustrative, adapted from one of my slides, with a product name replaced by a generic managed platform. <a href="/theses/arbitrage-window/build-vs-operate.png">Open full size</a></figcaption>
</figure>

None of this means anyone can build anything. Complex, regulated or high-reliability software still needs expertise, testing and someone accountable for it, and a working demo is not a product people depend on.

So the people who gain are individuals and small teams building tools for their own work, along with businesses whose value already sits in distribution, integrations, data or trust rather than in the code. The most exposed are simple, single-purpose products sold mainly on features that are now cheap to reproduce.

The case against is that self-built tools cost more to maintain than people expect, so most teams drift back to buying and the window closes almost as soon as it opens. If, two years from now, small teams still aren't replacing purchased tools with their own in any meaningful number, or the cost of building simple software stops falling, I'll have been wrong.
