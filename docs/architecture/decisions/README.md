# Architectural Decisions

Relevant decisions are recorded here as lightweight ADRs. Do not split a decision into its
own file until the record is long enough to justify it. Each decision describes the context,
the choice, the consequences and the discarded alternatives.

## Format

```markdown
## ADR-NNN: Title

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Superseded

### Context

### Decision

### Consequences

### Alternatives considered
```

## Index

- [ADR-001: Hexagonal architecture with C4 documentation](#adr-001-hexagonal-architecture-with-c4-documentation)
- [ADR-002: CPU-first, no deep learning in the core](#adr-002-cpu-first-no-deep-learning-in-the-core)
- [ADR-003: Python 3.12+ with `src/` layout](#adr-003-python-312-with-src-layout)
- [ADR-004: Filesystem as initial persistence adapter](#adr-004-filesystem-as-initial-persistence-adapter)

## ADR-001: Hexagonal architecture with C4 documentation

**Date:** 2026-10-06  
**Status:** Accepted

### Context

P-Grafo must remain interpretable, testable and evolvable as scientific methods change. The
system needs clear boundaries between domain science, orchestration and technical
implementations. Documentation must scale with the codebase.

### Decision

Use hexagonal (ports-and-adapters) architecture combined with C4 documentation:

- Domain and application form the core, free of external dependencies.
- Infrastructure and adapters implement ports at the boundary.
- C4 models document context, containers, components and code.

### Consequences

**Positive:**

- Domain science remains testable without infrastructure.
- Adapters can be swapped (CLI vs API, filesystem vs database) without changing core logic.
- New prediction methods enter as new adapters behind existing ports.
- Documentation evolves with the system through versioned diagrams.

**Negative:**

- Initial setup requires more discipline than a script-oriented approach.
- Developers must understand ports, adapters and dependency inversion.

### Alternatives considered

- **Script-first pipeline:** rejected due to tight coupling and poor testability.
- **Layered architecture:** rejected because it allows domain to depend on infrastructure.
- **Event-driven core:** deferred; may be added later if async workflows become necessary.

---

## ADR-002: CPU-first, no deep learning in the core

**Date:** 2026-10-06  
**Status:** Accepted

### Context

The project targets researchers and students without GPU access. Deep learning models are
often opaque and require specialised hardware. The goal is interpretability and accessibility.

### Decision

The core execution line (P-Grafo Classic and Hybrid) runs on CPU and uses classical methods:

- Homology modelling, MSA, DCA, fragment assembly.
- Statistical potentials and physical optimisation.
- Classical ML (regression, random forest, gradient boosting) as optional adapters.

Deep learning (P-Grafo Neural) remains outside the core execution and may enter later as
pluggable adapters.

### Consequences

**Positive:**

- Accessible to users without GPUs.
- Methods are interpretable and auditable.
- Easier to debug and validate scientifically.

**Negative:**

- Accuracy may be lower than state-of-the-art deep learning methods.
- Some tasks (e.g., contact prediction) may require more feature engineering.

### Alternatives considered

- **GPU-dependent deep learning core:** rejected due to accessibility and interpretability goals.
- **Hybrid core with optional neural adapters:** accepted for future evolution, but not in MVP.

---

## ADR-003: Python 3.12+ with `src/` layout

**Date:** 2026-10-06  
**Status:** Accepted

### Context

The project needs a modern Python baseline with clear packaging, testing and dependency
management. The team values type safety and clean imports.

### Decision

- Minimum Python version: 3.12.
- Package layout: `src/p_grafo/` to avoid accidental imports and support clean packaging.
- Dependency management: `pyproject.toml` with `uv` or `poetry`.

### Consequences

**Positive:**

- Modern syntax and standard library features available.
- Clear separation between source and tests.
- Better IDE support and fewer import pitfalls.

**Negative:**

- Excludes users on older Python versions (mitigated by virtual environments).

### Alternatives considered

- **Flat layout (`p_grafo/` at root):** rejected due to import ambiguity.
- **Python 3.10 minimum:** rejected; 3.12 provides better type hints and performance.

---

## ADR-004: Filesystem as initial persistence adapter

**Date:** 2026-10-06  
**Status:** Accepted

### Context

The MVP needs simple, reproducible persistence without database complexity. Experiments must
be traceable and portable.

### Decision

Use local filesystem as the initial persistence adapter:

- FASTA inputs stored in `data/inputs/`.
- Results stored in `data/outputs/<experiment-id>/`.
- Metadata in JSON alongside structures.

A database-backed repository may replace this adapter later without changing domain or use
cases.

### Consequences

**Positive:**

- Simple setup and debugging.
- Easy to version and share experiment artefacts.
- No database dependencies in MVP.

**Negative:**

- Less efficient for large-scale experiment tracking.
- No built-in query interface for experiments.

### Alternatives considered

- **Database from the start:** rejected for the MVP because it adds operational complexity before the experiment contract is stable.
- **In-memory only:** rejected because experiments must remain traceable and portable.

See the [architecture overview](../README.md).
