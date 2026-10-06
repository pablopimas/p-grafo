# P-Grafo Project Management Guide

This document consolidates the project management practices from the original planning PDFs. It defines how to organise work, track progress and maintain quality in P-Grafo development.

---

## Overview

P-Grafo development follows a **Kanban methodology** with GitHub Projects (new), GitHub Issues as the primary work unit and Pull Requests for traceability. The approach emphasises:

- Visualising work.
- Limiting work in progress (WIP).
- Managing flow explicitly.
- Continuous improvement.

This guide complements the technical architecture documentation and ensures that development practices are as rigorous as the scientific design.

---

## Work organisation model

### Work item unit

- **GitHub Issues**: Use for all real work (features, bugs, tasks, spikes).
- **Draft items**: Use only for very early ideas or work not yet refined.
- **Pull Requests**: Always link to the corresponding Issue for traceability.

### Board structure

The main Kanban board is grouped by **Status**:

| Column | Meaning |
|---|---|
| **Backlog** | Work identified but not yet refined. |
| **Ready** | Work refined and ready to start. |
| **In Progress** | Active work. |
| **Review** | Work finished, pending technical or functional review. |
| **Done** | Work accepted and integrated. |
| **Blocked** | Work stopped due to dependency or incident. |

### WIP limits

To prevent overload and maintain focus:

- **In Progress**: maximum 2 items
- **Review**: maximum 2 items

Adjust these limits as the team grows or shrinks.

---

## Custom fields in GitHub Projects

Configure the following custom fields in your GitHub Project:

| Field | Type | Recommended values |
|---|---|---|
| `Status` | Single select | Backlog, Ready, In Progress, Review, Done, Blocked |
| `Priority` | Single select | P0, P1, P2, P3 |
| `Type` | Single select | Epic, Feature, Task, Spike, Bug, Tech Debt |
| `Area` | Single select | Architecture, Domain, Application, Infrastructure, CLI, Science, Testing, Docs, DevEx |
| `Estimate` | Number | 1, 2, 3, 5, 8 |
| `Risk` | Single select | Low, Medium, High |
| `Target` | Single select | Foundation, MVP, Post-MVP |

These fields enable filtering, grouping and reporting across the project.

---

## Recommended views

Configure these views in GitHub Projects:

1. **Board — Status**: Main Kanban view grouped by Status.
2. **Table — All work**: Full table view for bulk editing of fields.
3. **Board — Priority**: Grouped by Priority to focus on P0 and P1.
4. **Blocked**: Filter `Status = Blocked` to identify impediments.
5. **MVP**: Filter `Target = MVP` to focus on MVP scope.
6. **Science**: Filter `Area = Science` to track scientific tasks.

---

## Issue template

Use this template for all Issues to ensure clarity and traceability:

```markdown
## Context

Brief explanation of why this task exists.

## Objective

Concrete result that must be delivered.

## Scope

- Item 1
- Item 2
- Item 3

## Acceptance criteria

- [ ] Verifiable criterion 1
- [ ] Verifiable criterion 2
- [ ] Verifiable criterion 3

## Dependencies

- #123
- None

## Technical notes

Implementation observations, constraints or decisions.
```

This format ensures that every task has context, clear completion criteria and explicit dependencies.

---

## Naming convention

Use consistent prefixes for quick filtering and readability:

```text
ARCH-001 Create C4 context
ARCH-002 Create C4 containers
DEVX-001 Create pyproject.toml
DOM-001 Implement ProteinSequence
APP-001 Create RunPredictionUseCase
CLI-001 Create predict command
SCI-001 Implement DCA baseline
TEST-001 Add domain fixtures
```

Prefixes help identify the nature of work at a glance.

---

## Operational policies

### When a task enters Ready

A task can move to **Ready** when:

- It has a clear description.
- It has verifiable acceptance criteria.
- Dependencies are identified.
- It is small enough to complete in approximately one day or less.
- No pending decisions block execution.

### When a task enters In Progress

- Work has started.
- A branch is created and linked to the Issue.
- WIP limit is respected (max 2).

### When a task enters Review

A task can move to **Review** when:

- Code or documentation is pushed.
- Relevant tests pass.
- Minimum documentation is updated.
- The Issue references its Pull Request.
- WIP limit is respected (max 2).

### When a task enters Done

A task can move to **Done** when:

- It has been reviewed and approved.
- All acceptance criteria are met.
- No open blockers remain.
- It is integrated into `main` or the equivalent primary branch.

### When a task enters Blocked

- An external dependency or incident prevents progress.
- The blocking factor is clearly documented.
- Next steps or required actions are identified.

---

## Automations

Configure these minimal automations in GitHub Projects:

- **When an item is added to the project**: Set `Status = Backlog`.
- **When an Issue is closed**: Move to `Done`.
- **When an Issue is reopened**: Move to `Backlog` or `Ready`, according to team policy.

These automations reduce manual overhead and keep the board up to date.

---

## Metrics

Track the following metrics over time to monitor flow and identify bottlenecks:

- **Lead time**: Time from Backlog to Done.
- **Cycle time**: Time from In Progress to Done.
- **Throughput**: Number of items completed per unit time.

Review these metrics in retrospectives to continuously improve the workflow.

---

## Getting started

To set up P-Grafo project management:

1. **Create repository labels** matching the `Area` and `Type` fields.
2. **Create a GitHub Project** and configure custom fields.
3. **Create the first 10–20 Issues** manually or via importer.
4. **Add Issues to the Project**.
5. **Group the main view by Status**.
6. **Start with few cards in Ready** to avoid saturating In Progress.

This approach aligns with Kanban principles: start with visible flow, limit WIP and adjust policies as real bottlenecks emerge.

---

## Relationship to other documentation

This guide complements:

- **Architecture documentation** (`docs/architecture/`): Defines the technical structure.
- **Backlog** (`docs/scrum/backlog.md`): Lists planned work.
- **Roadmap** (`docs/scrum/roadmap.md`): Defines sprint objectives.
- **Definition of Done** (`docs/scrum/definition-of-done.md`): Defines quality criteria.

Together, these documents form the complete development framework for P-Grafo.

---

## References

- GitHub Projects documentation: [https://docs.github.com/en/issues/planning-and-tracking-with-projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- Kanban methodology: Visualise work, limit WIP, manage flow.
- P-Grafo architecture plan (original PDF): Source of initial practices.
- P-Grafo GitHub Projects Kanban guide (original PDF): Source of workflow details.
