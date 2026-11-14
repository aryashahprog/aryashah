---
title: Agents can help formulate the optimization problem
theme: AI in operations
order: 2
summary: Operations research already re-plans continuously and under uncertainty. The bottleneck is often turning messy operational knowledge into objectives and constraints, which agents might help with under human review.
updated: 2026-11-13
status: Working draft
related: [frontline-and-physical-ai, workflow-economics]
sources:
  - title: "Rawlings, Mayne and Diehl, Model Predictive Control: Theory, Computation, and Design, 2nd ed."
    url: https://sites.engineering.ucsb.edu/~jbraw/mpc/
  - title: "Birge and Louveaux, Introduction to Stochastic Programming, 2nd ed., Springer, 2011"
    url: https://doi.org/10.1007/978-1-4614-0237-4
  - title: "AhmadiTeshnizi, Gao and Udell, “OptiMUS: Scalable Optimization Modeling with (MI)LP Solvers and Large Language Models,” 2024"
    url: https://arxiv.org/abs/2402.10172
  - title: "Ramamonjison et al., “NL4Opt Competition: Formulating Optimization Problems Based on Their Natural Language Descriptions,” 2023"
    url: https://arxiv.org/abs/2303.08233
---
Established optimization methods already handle changing conditions. Model predictive control re-solves a plan over a rolling horizon, while stochastic programming accounts for uncertainty. The opportunity I’m interested in comes before the solver: turning messy operational information into a problem it can solve.

Formulation is often a bottleneck in its own right. Before anything can be optimized, someone has to decide what the objective is, which constraints are real and which data to trust, and that knowledge is scattered across emails, spreadsheets, policies and people's heads. The authors of OptiMUS, an LLM-based agent that formulates and solves linear and mixed-integer programs from natural-language descriptions, argue that most such problems are still solved by hand because formulating them takes expertise. The NL4Opt competition was set up to study the same step.

My thesis is that agents can help turn messy operational information into candidate objectives and constraints, propose revisions when conditions change and explain exceptions, with a person reviewing before anything changes the plan. Results so far come from benchmark problems, not live operations, so I'm not claiming agents do this better than experienced analysts.

One way to structure it, as a proposed architecture: an operations world model that reflects the operation as it is, forecasts, models of how workers and customers actually behave, and an optimizer that draws on the other three.

The failure cases matter as much as the upside:

- Wrong constraints: the agent encodes a rule that doesn't exist or misses one that does, and the solver returns a confident plan that can't or shouldn't be carried out.
- Drift: the formulation is right on day one and slowly stops matching how the operation works.
- Unsafe actions: a plan goes to people or equipment without anyone checking it.

Each one argues for keeping proposals reviewable and changes reversible.

Planning teams in logistics, manufacturing and scheduling, who already pay for solvers and consultants, are the likely beneficiaries. The strongest counterargument is that formulation depends on tacit knowledge agents can't reach, so experts still do the real work and agents only save typing. I'd change my mind if, in live deployments, agent-proposed formulations need so much correction that they save analysts no time, or if the errors they introduce outweigh the gains.
