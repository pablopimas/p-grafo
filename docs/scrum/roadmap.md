# Roadmap

| Sprint | Objective | Deliverable |
| --- | --- | --- |
| 0 | Prepare architecture, documentation and CI. | Executable and documented repository. |
| 1 | Establish domain model, ports and DTOs. | Tested core. |
| 2 | Execute minimum pipeline with simulated adapters. | End-to-end CLI demo. |
| 3 | Incorporate first useful scientific computation. | Technically meaningful prediction. |
| 4 | Add quality, metrics and traceability. | Reproducible MVP. |
| 5 | Improve UX, error handling and packaging. | Usable v0.1.0 release. |

## Sprint 0: Foundation

**Duration:** 1-2 weeks

**Goals:**
- Set up repository with `src/` layout.
- Configure CI (lint, tests, packaging).
- Write C4 context, containers and components.
- Draft initial ADRs.
- Add README, LICENSE and contribution guidelines.

**Exit criteria:**
- Empty tests pass in CI.
- Documentation is versioned and linked.
- Team can clone and run `make check`.

---

## Sprint 1: Domain core

**Duration:** 2 weeks

**Goals:**
- Implement `ProteinSequence`, `Residue`, `ProteinGraph`, `StructureModel`.
- Define input/output DTOs.
- Create inbound and outbound ports.
- Add unit tests for domain entities.

**Exit criteria:**
- Domain entities are validated and tested.
- Ports are defined with contract tests.
- No infrastructure imports in domain or application.

---

## Sprint 2: MVP pipeline

**Duration:** 2 weeks

**Goals:**
- Implement `RunPredictionUseCase` with fake adapters.
- Create CLI entry point.
- Build baseline structure generator.
- Implement simple energy function and optimizer.
- Export PDB and JSON.

**Exit criteria:**
- `p-grafo predict --fasta <file>` produces a PDB.
- End-to-end test passes with synthetic sequence.
- Output artefacts match execution contract.

---

## Sprint 3: First scientific computation

**Duration:** 2-3 weeks

**Goals:**
- Integrate real or semi-real MSA adapter.
- Add DCA or coupling computation.
- Build graph from evidence.
- Implement baseline distance predictor.

**Exit criteria:**
- First technically meaningful prediction on a small protein.
- Contacts or distances are derived from evidence, not hardcoded.
- Metrics (energy, constraints) are recorded.

---

## Sprint 4: Quality and reproducibility

**Duration:** 2 weeks

**Goals:**
- Add fixed seed support.
- Implement logging and telemetry.
- Add contract tests for all adapters.
- Create experiment output structure.
- Document limitations and validation.

**Exit criteria:**
- Executions are reproducible with same seed.
- All adapters have contract tests.
- Report includes confidence and traceability info.

---

## Sprint 5: Hardening and release

**Duration:** 1-2 weeks

**Goals:**
- Improve CLI UX and error messages.
- Add installation instructions.
- Create release package (PyPI or installable).
- Write v0.1.0 release notes.
- Polish documentation.

**Exit criteria:**
- `pip install .` works cleanly.
- v0.1.0 is tagged and released.
- Users can follow README to run a prediction without help.

---

## Post-MVP (future sprints)

- Homology modelling mode.
- Fragment library and assembly.
- Classical ML predictors (Random Forest, XGBoost).
- HTTP API adapter.
- Database-backed experiment tracking.
- Enhanced energy function and confidence scoring.
