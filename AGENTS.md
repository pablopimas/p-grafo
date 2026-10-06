# P-Grafo Agent Instructions

## Project purpose

P-Grafo is a CPU-first bioinformatics research project for interpretable protein structure
modelling. It produces candidate 3D structures from protein sequences and evolutionary,
structural and geometric evidence.

The current scope excludes GPUs and deep learning. Classical bioinformatics methods, physical
optimisation and classical machine learning are allowed.

## Current development stage

The project is in the MVP foundation stage.

Current implementation priority:

1. Build a tested domain core.
2. Build an end-to-end pipeline using fake adapters.
3. Add reproducibility, artefact export and end-to-end tests.
4. Replace fake adapters incrementally with scientific implementations.

Do not implement DCA, XGBoost, fragment assembly, homology modelling, HTTP APIs, databases,
Docker, workflow orchestration or neural models unless the current Issue explicitly requires it.

## Architecture

P-Grafo uses hexagonal architecture.

```text
input adapter
  → input port
  → use case
  → domain
  → output port
  → infrastructure adapter
```

Dependencies must point inwards.

### Dependency rules

- `domain` must not import from `application`, `infrastructure`, `adapters` or `bootstrap`.
- `domain` must not import CLI libraries, filesystem APIs, subprocess, NumPy, SciPy, pandas,
  scikit-learn, XGBoost, Pydantic or external bioinformatics tools.
- `application` may import from `domain` and define ports and DTOs.
- `application` must not instantiate infrastructure adapters directly.
- `infrastructure` implements outbound ports and may depend on external libraries.
- `adapters` translate external input/output and invoke inbound ports.
- `bootstrap` is the only location that composes concrete implementations.
- Domain entities must not be directly serialised by CLI or exporters. Use DTOs at boundaries.

## Source layout

```text
src/p_grafo/
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── services/
│   └── exceptions/
├── application/
│   ├── use_cases/
│   ├── ports/
│   │   ├── inbound/
│   │   └── outbound/
│   ├── dto/
│   └── services/
├── infrastructure/
│   ├── msa/
│   ├── dca/
│   ├── predictors/
│   ├── optimizers/
│   ├── persistence/
│   ├── exporters/
│   ├── config/
│   └── logging/
├── adapters/
│   ├── cli/
│   ├── api/
│   └── batch/
└── bootstrap/
```

## Coding rules

- Target Python 3.12 or higher.
- Use type hints for public functions, methods and classes.
- Prefer `dataclass(frozen=True)` for immutable value objects and DTOs.
- Keep functions small and single-purpose.
- Prefer explicit names over abbreviations.
- Do not add dependencies unless required by the current Issue.
- Do not introduce a framework where standard library code is sufficient.
- Do not write scientific claims in code comments or documentation unless a test or reference
  supports them.
- Preserve deterministic behaviour where possible.
- Random behaviour must receive an explicit seed through configuration or input DTOs.
- Fail early with clear domain-specific exceptions.
- Keep comments focused on non-obvious scientific or architectural rationale.

## Domain rules

- `ProteinSequence` owns validation of an amino acid sequence.
- Domain code must not parse files or know about FASTA file paths.
- FASTA parsing belongs to an input adapter or infrastructure parser.
- Domain code must not write PDB, JSON, CSV or filesystem artefacts.
- Structural representations must clearly distinguish verified data from simulated placeholders.
- A generated PDB is not evidence of a validated protein prediction.
- Do not overstate scientific accuracy in output fields, logs or documentation.

## Testing rules

- Place domain tests under `tests/unit/domain/`.
- Place application use-case tests under `tests/unit/application/`.
- Place adapter contract tests under `tests/contract/`.
- Place multi-component tests under `tests/integration/`.
- Place CLI-to-output tests under `tests/e2e/`.
- Every bug fix should include a regression test.
- Add tests before or alongside implementation.
- Use fixtures that are small, deterministic and legally redistributable.
- Tests must not require network access, external databases, a GPU or large datasets.
- Use fake adapters for unit tests and early end-to-end tests.

## Scientific validation rules

For any change affecting the scientific pipeline:

- State a measurable expected behaviour.
- Add a deterministic fixture or reference case where possible.
- Record configuration and seed.
- Do not claim biological or structural accuracy without comparison against a reference.
- Document relevant assumptions and limitations.

Examples of valid scientific criteria:

- A valid sequence is accepted and invalid residues are rejected.
- A generated backbone satisfies defined bond-length tolerances.
- An optimiser reduces a defined objective function.
- A contact predictor improves Precision@L against a fixed benchmark.
- The same input, configuration and seed reproduce the same output.

## Documentation rules

- Write public documentation in English.
- Update the relevant document when behaviour, contracts or architecture changes.
- Update C4 documentation only when context, containers or components materially change.
- Create a lightweight ADR for significant architectural decisions.
- Keep `README.md` concise; put detailed scientific rationale in `docs/research/`.
- Do not create new documentation files unless they serve a specific current need.

## Required checks

Before considering work complete, run the commands available in this repository:

```bash
make check
```

If available, also run focused tests:

```bash
pytest tests/unit -q
pytest tests/contract -q
pytest tests/integration -q
pytest tests/e2e -q
```

Do not claim tests pass unless they were actually run and their result is known.

## Change workflow

For every requested change:

1. Inspect relevant existing code and tests first.
2. State the smallest viable implementation plan.
3. Implement only the requested scope.
4. Add or update tests.
5. Run the relevant checks.
6. Summarise changed files, test results and remaining limitations.
7. Do not make unrelated refactors.

## Current first implementation target

The next feature is `DOM-001: ProteinSequence`.

Expected responsibilities:

- Store a sequence identifier and amino acid sequence.
- Normalise lowercase amino acids to uppercase.
- Remove accidental whitespace.
- Reject empty sequences.
- Reject invalid residues.
- Expose sequence length.
- Remain independent of FASTA files, CLI, NumPy, PDB, JSON and filesystem access.

Expected test cases:

- Accepts a valid sequence.
- Normalises lowercase input.
- Removes whitespace.
- Rejects an empty sequence.
- Rejects invalid residues.
- Exposes correct sequence length.
