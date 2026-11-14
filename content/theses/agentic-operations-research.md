---
title: Agents can help formulate the optimization problem
theme: AI in operations
order: 2
summary: Operations research already re-plans continuously and under uncertainty. The bottleneck is often turning messy operational knowledge into objectives and constraints, which agents might help with under human review.
updated: 2026-11-14
status: Working draft
related: [frontline-and-physical-ai, workflow-economics]
---
Established optimization methods already handle changing conditions. Model predictive control re-solves a plan over a rolling horizon, while stochastic programming accounts for uncertainty.[^mpc] The opportunity I'm interested in comes before the solver: turning messy operational information into a problem it can solve.

Formulation is often a bottleneck in its own right. Before anything can be optimized, someone has to decide what the objective is, which constraints are real and which data to trust, and that knowledge is scattered across emails, spreadsheets, policies and people's heads. The authors of OptiMUS, an LLM-based agent that formulates and solves linear and mixed-integer programs from natural-language descriptions, argue that most such problems are still solved by hand because formulating them takes expertise.[^optimus] The NL4Opt competition was set up to study the same step.[^nl4opt]

That is where I think agents can help: turning messy information into candidate objectives and constraints, proposing revisions when conditions change and explaining exceptions, with a person reviewing before anything changes the plan. Results so far come from benchmark problems, not live operations, so I'm not claiming agents do this better than experienced analysts.

One way to structure it, as a proposed architecture, is four layers: an operations world model that reflects the operation as it is, forecasts, models of how workers and customers actually behave, and an optimizer that draws on the other three.

<figure class="narrow">
<a href="/theses/agentic-operations-research/formulation-loop.svg"><img src="/theses/agentic-operations-research/formulation-loop.svg" width="360" height="764" loading="lazy" alt="Proposed architecture, not measured evidence. Messy operational information goes to an agent that drafts candidate objectives and constraints; a person approves, edits or rejects the draft; the reviewed formulation feeds four proposed layers: world model, forecasts, behavior models and an optimizer drawing on the other three; the reviewed plan goes into use with changes reversible; drift and exceptions from deployment feed the next draft."></a>
<figcaption>A proposed architecture, not measured evidence: the agent drafts, a person reviews, and deployment feedback flows back into the next draft. My diagram. <a href="/theses/agentic-operations-research/formulation-loop.svg">Open full size</a></figcaption>
</figure>

The world-model layer has its own loop once a plan is running. It takes in what sensors report, predicts what each candidate action would do, and lets a planner with a safety check choose one or hand the decision to a person.

<figure class="slim">
<a href="/theses/agentic-operations-research/deployment-loop.png"><img src="/theses/agentic-operations-research/deployment-loop.png" width="422" height="1599" loading="lazy" alt="Deployment loop: live sensors, then candidate actions, then predicted outcomes, then a planner and safety check, then an action or a request for human help."></a>
<figcaption>The world-model layer at run time: predict what each candidate action would do, then let a planner and safety check pick one or hand off to a person. It illustrates one layer, not the whole thesis. Crop from an Engage brief on world models. <a href="/theses/agentic-operations-research/deployment-loop.png">Open full size</a></figcaption>
</figure>

The failure cases matter as much as the upside. An agent can encode a rule that doesn't exist or miss one that does, and the solver will return a confident plan that can't or shouldn't be carried out. A formulation can be right on day one and slowly drift away from how the operation actually works. And a plan can reach people or equipment without anyone checking it. Each of these argues for keeping proposals reviewable and changes reversible.

Planning teams in logistics, manufacturing and scheduling, who already pay for solvers and consultants, are the likely beneficiaries. Formulation may depend on tacit knowledge agents can't reach, in which case experts still do the real work and agents only save typing. I'd change my mind if, in live deployments, agent-proposed formulations need so much correction that they save analysts no time, or if the errors they introduce outweigh the gains.

[^mpc]: Rawlings, Mayne and Diehl, [*Model Predictive Control: Theory, Computation, and Design*](https://sites.engineering.ucsb.edu/~jbraw/mpc/), 2nd ed.; Birge and Louveaux, [*Introduction to Stochastic Programming*](https://doi.org/10.1007/978-1-4614-0237-4), 2nd ed., Springer, 2011.
[^optimus]: AhmadiTeshnizi, Gao and Udell, “[OptiMUS: Scalable Optimization Modeling with (MI)LP Solvers and Large Language Models](https://arxiv.org/abs/2402.10172),” 2024.
[^nl4opt]: Ramamonjison et al., “[NL4Opt Competition: Formulating Optimization Problems Based on Their Natural Language Descriptions](https://arxiv.org/abs/2303.08233),” 2023.
