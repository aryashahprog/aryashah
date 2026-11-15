---
title: Frontline AI starts with one costly task
theme: AI in operations
order: 1
summary: For people who work with their hands, AI may start as guidance on one specific, expensive task, built from expert reasoning and checked outcomes, not as a general assistant or a robot.
started: 2026-11-01
updated: 2026-11-14
status: Working draft
related: [agentic-operations-research]
---
Most AI products assume someone at a desk. The people who repair equipment, inspect sites or run warehouse floors work with their hands busy and often away from a screen.

For them, I think **AI will start as help with one specific, costly task**, where mistakes or delays are expensive and experienced people are scarce, rather than as a general assistant or a robot.

## A loop built from expert work

Capture how experienced people do the task and why they make the choices they do, use that to guide the next person through it, and feed checked outcomes back so the procedure improves.

<figure class="wide">
<a href="/theses/frontline-and-physical-ai/physical-workflow.svg"><picture><source media="(min-width: 700px)" srcset="/theses/frontline-and-physical-ai/physical-workflow-wide.svg" width="640" height="191"><img src="/theses/frontline-and-physical-ai/physical-workflow.svg" width="360" height="355" loading="lazy" alt="Capture, learn, guide, check. 1. Observe work, capturing first-person task context. 2. Learn expertise from expert reasoning and outcomes. 3. Guide execution and check the next task. Verified outcomes feed back to improve the next procedure."></picture></a>
<figcaption>Capture how experts do a task, learn from their reasoning and results, guide the next person, and feed checked outcomes back in. <a href="/theses/frontline-and-physical-ai/physical-workflow.svg">Open full size</a></figcaption>
</figure>

Here is a hypothetical case, not something I've deployed. A technician servicing an unfamiliar machine gets step-by-step guidance by voice or through a headset. The system flags a skipped step before it causes a failure, and whether the repair held is recorded and used to improve the next set of instructions.

Whether that pays off depends on how often the task happens, what an error costs and whether the guidance is actually right.

## The data has to be collected on purpose

The hard part is the first step of the loop: getting a record of how skilled people actually do physical work. Each way of collecting it trades accuracy against cost and scale.

<figure class="wide">
<a href="/theses/frontline-and-physical-ai/data-routes.svg"><picture><source media="(min-width: 700px)" srcset="/theses/frontline-and-physical-ai/data-routes-wide.svg" width="640" height="228"><img src="/theses/frontline-and-physical-ai/data-routes.svg" width="360" height="390" loading="lazy" alt="Four ways to gather physical-task data. Teleoperation and demo farms: accurate, but cost grows linearly. Human video capture: cheap and abundant, but no force data. Simulation and world models: scalable, but must carry over to real conditions. Deployed fleet data flywheels: compounding, but needs a live fleet."></picture></a>
<figcaption>Expert demonstrations record skilled work most directly but cost the most; video and simulation scale more cheaply but miss touch or realism; fleet data compounds only once something is deployed. From my physical AI trend brief. <a href="/theses/frontline-and-physical-ai/data-routes.svg">Open full size</a></figcaption>
</figure>

AR glasses are one way to deliver guidance, and the first-person data they capture might later help train robots. That is one possible path. Robotics could advance without it, and a phone may be good enough for many jobs.

## Adoption won't follow one pattern

Hiring difficulty might drive adoption in some industries and not others, and how workers and unions respond will differ by workplace. Synthetic data might help with training, but it can't replace real outcomes when checking whether guidance works.

The buyer is probably an operations or service leader who owns a task where errors are costly and hard to staff, such as field service, maintenance or quality inspection. This may turn out to be a feature of existing field service and training software, with the hard part being integration and getting crews to change habits.

I'd change my mind if guided workflows fail to measurably cut errors or time on a specific task in real deployments, or if workers stop using them once the novelty wears off.


