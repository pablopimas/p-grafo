# Initial Backlog

## Architectural foundation

- [ ] Create and version C4 diagrams (context, containers, components).
- [ ] Write initial ADRs (hexagonal architecture, CPU-first, Python 3.12+, filesystem persistence).
- [ ] Set up CI pipeline for lint, tests and packaging.
- [ ] Configure repository structure with `src/` layout.
- [ ] Add README, LICENSE, CODEOWNERS and `.editorconfig`.

## Protein domain

- [x] Implement `ProteinSequence` entity with validation.
- [ ] Implement `Residue` value object.
- [ ] Implement `ProteinGraph` entity (nodes, edges, weights).
- [ ] Implement `StructureModel` entity (coordinates, energy, metadata).
- [ ] Implement `DistanceConstraintSet` and `CouplingMatrix`.
- [ ] Add unit tests for domain entities and validation rules.
- [ ] Define DTOs for prediction input/output.

## Minimum pipeline

- [ ] Implement `RunPredictionUseCase` with simulated adapters.
- [ ] Create CLI entry point (`p-grafo predict`).
- [ ] Implement fake MSA provider for testing.
- [ ] Implement fake DCA/coupling computer for testing.
- [ ] Implement baseline structure generator (extended backbone).
- [ ] Implement simple energy function (bonds, angles, clashes).
- [ ] Implement Monte Carlo optimizer with simulated annealing.
- [ ] Implement PDB and JSON exporters.
- [ ] Add end-to-end test with synthetic sequence.

## Quality and reproducibility

- [ ] Add reproducible fixtures (short test sequences).
- [ ] Implement fixed seed support for all random operations.
- [ ] Write contract tests for each port/adapter pair.
- [ ] Add integration tests for pipeline with reference data.
- [ ] Document execution contract (inputs, outputs, artefacts).
- [ ] Add logging and basic telemetry.
- [ ] Create experiment output directory structure.

## Future epics (post-MVP)

- [ ] Real MSA adapter (HHblits, MMseqs2 or JackHMMER wrapper).
- [ ] Real DCA adapter (plmDCA or similar).
- [ ] Fragment library and assembly.
- [ ] Homology modelling mode.
- [ ] Classical ML predictors (Random Forest, XGBoost) for distances/contacts.
- [ ] HTTP API adapter.
- [ ] Database-backed experiment repository.
- [ ] Enhanced energy function (solvation, electrostatics).
- [ ] Per-residue confidence scoring.
