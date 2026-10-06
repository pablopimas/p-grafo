# P-Grafo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/pablopimas/p-grafo/actions/workflows/ci.yml/badge.svg)](https://github.com/pablopimas/p-grafo/actions/workflows/ci.yml)

P-Grafo is a bioinformatics research system for estimating a candidate 3D structure of a
protein from its sequence and evolutionary and structural evidence. The initial scope covers
monomeric proteins of 50–250 amino acids, without ligands or post-translational modifications,
in three modes: `homology`, `hybrid` and `de_novo`.

It is designed to run on CPU and evolve from a Python MVP to an extensible platform.

## Architecture

The project combines C4 documentation with hexagonal architecture:

- The **domain** expresses the scientific language and rules without depending on frameworks.
- The **application** orchestrates use cases through explicit ports.
- The **infrastructure** implements the ports for MSA, DCA, prediction, optimisation,
  persistence and export.
- The **adapters** expose the system's entry points, starting with the CLI.

Dependencies point inwards: domain and application do not import CLI, filesystem, external
tools or concrete scientific libraries.

## Repository map

```text
src/p_grafo/
  domain/          Pure scientific entities, value objects and services
  application/     Use cases, DTOs and ports
  infrastructure/  Implementations of outbound ports
  adapters/        CLI, API and batch entry points
  bootstrap/       Dependency composition
tests/
  unit/ integration/ contract/ e2e/
docs/
  README.md        Documentation index
  research/        Foundational scientific statement
  architecture/    C4 model and architectural decisions
  scrum/           Backlog, roadmap and project management
```

## Local development

Python 3.12 or higher is required.

```bash
python -m venv .venv
. .venv/bin/activate
make install
make check
```

## Usage

```bash
p-grafo predict \
  --fasta examples/1ubq.fasta \
  --mode de_novo \
  --models 20 \
  --output results/1ubq/
```

The CLI will be available in Sprint 2. The planned command contract is in
[C4: Containers](docs/architecture/c4-container.md).

## Roadmap

1. **Sprint 0:** architectural foundation, documentation and CI.
2. **Sprint 1:** domain model, ports and DTOs.
3. **Sprint 2:** end-to-end prediction pipeline with simulated adapters.
4. **Sprint 3:** first scientific pipeline with MSA, couplings and baseline predictor.
5. **Sprint 4-5:** quality, observability and MVP hardening.

See the [documentation index](docs/README.md), the
[architecture overview](docs/architecture/README.md) and the
[initial backlog](docs/scrum/backlog.md) for more detail.

## Contributing

Follow the [Definition of Done](docs/scrum/definition-of-done.md) and the
[project workflow](docs/scrum/project-management.md).
