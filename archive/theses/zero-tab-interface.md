---
title: The zero-tab interface
theme: New interfaces and buyers
order: 2
summary: Messaging-native agents may move software into conversations people already have, instead of more tabs and apps. iMessage is one possible distribution surface.
updated: 2026-11-13
status: First draft
related: [agents-are-customers]
sources:
  - {title: "Cloud Security Alliance, “Claw Chain: Four CVEs Enable Full AI Agent Compromise”, May 17, 2026", url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-openclaw-claw-chain-cve-20260517-csa-style/"}
---
## The claim

Agents that live in messaging could shift a lot of software use into conversations people already have, rather than into another tab or app. iMessage is one possible distribution surface.

## Reasoning

- People already spend much of their day in messaging. An agent there needs no download, new login or new habit.
- Many tasks fit a text thread well: quick requests, confirmations, reminders and simple choices.

<figure class="stat">
<p class="stat-number">214K+</p>
<figcaption>GitHub stars by February 2026 for <a href="https://github.com/openclaw/openclaw">OpenClaw</a>, an open-source personal agent that people talk to through messaging apps. Stars measure developer interest, not everyday use. Source: <a href="https://labs.cloudsecurityalliance.org/research/csa-research-note-openclaw-claw-chain-cve-20260517-csa-style/">Cloud Security Alliance</a>, May 17, 2026.</figcaption>
</figure>
- Some don't: detailed comparisons, dashboards and anything that needs a lot of visual detail.
- iMessage is interesting because it's where many people already talk. What platforms actually allow third-party agents to do is a question I want to check case by case rather than assume.

## Where value might accrue

- Whoever controls access to the messaging surface.
- Agents that do one job very well inside a thread.
- Tools that let businesses be reached from inside a conversation.

## What would change my mind

- People finding agents in their messages annoying or untrustworthy.
- Platforms restricting what third-party agents can do.
- The tasks people care about turning out to need visual interfaces.

Related project: my [event finder for iMessage](/building/#messaging-event-agent) is a prototype built around event discovery inside a message thread.
