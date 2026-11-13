---
title: Agentic operations research
theme: AI in operations
order: 3
featured: 3
summary: Agents may run the operations research loop continuously, reformulating and re-solving problems as conditions change. Real deployment outcomes should be the test.
updated: 2026-11-13
status: First draft
related: [frontline-and-physical-ai, agents-need-context]
---
## The claim

Operations research usually solves a snapshot: given today's data, find the best schedule, route or plan. Agents may be able to run that loop continuously, going back and forth between defining the problem and solving it as conditions change.

## Reasoning

- In practice, a lot of the hard work is formulating the problem: what to optimize, which constraints are real and which data to trust. That step is where agents might help most.
- A continuous loop matters because the real world keeps moving. A plan built on Monday's data can be stale by Tuesday.

## Four proposed layers

1. **Operations world model:** an up-to-date picture of the operation as it actually is.
2. **Forecasting:** what is likely to happen next.
3. **Human behavior models:** how workers and customers actually respond, since plans fail when they assume people will follow them exactly.
4. **Optimizer:** chooses what to do given the other three.

## How to test it

Real deployment outcomes, not benchmarks alone. Did costs, delays or service actually improve in a live operation, and did the people running it trust it enough to keep using it?

## Where value might accrue

- Whoever builds and maintains the operations world model, since it's hard to build and hard to replace.
- Teams that deploy this in a specific operation and can show real results.

## What would change my mind

- Continuous re-solving not beating periodic planning in live operations.
- Agents not being reliable enough to handle problem formulation.
- Operations teams being unwilling to hand over that much control.
