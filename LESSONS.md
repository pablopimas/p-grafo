# Lessons Learned

This file records concise, practical lessons discovered while building P-Grafo.

It is not an architecture specification, roadmap or scientific reference. Architectural decisions
belong in `docs/architecture/decisions/`; planned work belongs in `docs/scrum/`.

## Format

Each entry should include:

- Date
- Context
- Lesson
- Consequence or action

## Entries

### 2026-10-06 — Architecture before scientific complexity

**Context:** The project started with a broad scientific goal: CPU-only protein structure
modelling without deep learning.

**Lesson:** A full scientific pipeline should not be implemented before its domain concepts,
ports, reproducibility rules and test boundaries are explicit.

**Action:** Build a vertical technical slice with fake adapters before integrating MSA, DCA,
fragment assembly, physical optimisation or classical ML.

### 2026-10-06 — Generated structures are not validated predictions

**Context:** The MVP will initially generate placeholder or geometrically constrained
structures.

**Lesson:** Producing a PDB file does not demonstrate structural prediction accuracy.

**Action:** Label early outputs as synthetic baselines or candidate models. Make scientific
claims only after comparison with experimental reference structures and explicit metrics.
