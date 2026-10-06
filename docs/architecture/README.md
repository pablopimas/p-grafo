# P-Grafo Architecture

P-Grafo is a CPU-oriented protein structure prediction system. The architecture separates the
scientific language, pipeline orchestration and technical implementations. The documentation
model is C4. The implementation model is hexagonal.

The [foundational statement](../research/p-grafo-foundation.md) defines the scientific scope.
This document defines the software structure, its boundaries and its contracts.

## Documents

- [C4: Context](c4-context.md)
- [C4: Containers](c4-container.md)
- [C4: Components](c4-component.md)
- [Architectural decisions](decisions/README.md)

## Architectural model

The architecture combines four C4 levels with a hexagonal core:

| Level | Content |
| --- | --- |
| Context | Actors, external systems and the outcome of a prediction. |
| Containers | Entry point, application, domain, infrastructure and storage. |
| Components | Entities, use cases, ports and adapters. |
| Code | Python modules under `src/p_grafo`. |

Dependencies point inwards. The domain knows nothing about use cases, interfaces, storage or
scientific libraries. The application knows the domain and the ports; it knows nothing about
concrete adapters. Infrastructure and adapters implement the ports. `bootstrap` composes those
implementations at the system boundary.

```text
input adapters
        ↓
input ports
        ↓
use cases
        ↓
domain
        ↑
output ports
        ↑
infrastructure adapters
```

Context, containers and components are specified in the C4 documents linked above.

## Modules

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
    └── container.py
```

| Module | Content |
| --- | --- |
| `domain` | Scientific entities, value objects, services and exceptions. |
| `application` | Use cases, DTOs, policies and ports. |
| `infrastructure` | Implementations of output ports. |
| `adapters` | CLI, HTTP API and batch. |
| `bootstrap` | Composition of use cases and adapters. |

DTOs cross the application boundary. Domain entities are not directly serialised by the CLI
or exporters.

## Composition

`bootstrap/container.py` instantiates adapters, assigns them to ports and constructs the use
cases. No use case constructs its concrete dependencies. The CLI obtains the use case from
the composition container.

An execution produces:

```text
best_model.pdb
models.json
contacts.csv
energy_trace.csv
report.html
```

The report includes the candidate structure, energy score, satisfied constraints, geometric
violations, model diversity, confidence, prediction mode, configuration and seed. The output
schema is in [C4: Containers](c4-container.md).

## Testing

| Type | Scope |
| --- | --- |
| Unit | Domain and use cases with port doubles. |
| Contract | Each port and its adapter. |
| Integration | Pipeline with reference data. |
| End-to-end | Complete invocation from an input adapter. |

Domain tests do not import infrastructure. Contract tests verify that an adapter fulfils the
port without exposing its library or external process to the core.

## Product levels

| Level | Architectural capabilities |
| --- | --- |
| P-Grafo Classic | Homology, MSA, DCA, fragments, statistical potentials and physical optimisation. |
| P-Grafo Hybrid | Regression, random forest, gradient boosting and statistical fragment selection behind the same ports. |
| P-Grafo Neural | Language models, equivariant networks and direct coordinate prediction behind the same ports. |

The current scientific scope is P-Grafo Classic and the classical machine learning of P-Grafo
Hybrid. P-Grafo Neural stays outside that execution. When a neural method exists, it enters as
an adapter of `DistancePredictorPort`, `CouplingComputerPort` or `StructureOptimizerPort`, not
as a change to the core.

## Current constraints

- Python 3.12 and the `src/` layout form the packaging base.
- The scientific core remains free of CLI, FastAPI, NumPy, SciPy, XGBoost, subprocess and
  direct file access.
- The filesystem is the persistence adapter of the current functional line.
- PDB and JSON are the interchange formats for structures and metadata.
- Each prediction preserves evidence, constraints, seed and configuration.

The accepted decisions, including discarded alternatives, are recorded as
[lightweight ADRs](decisions/README.md).

## Related documents

- [Foundational statement](../research/p-grafo-foundation.md)
- [Documentation index](../README.md)
- [C4: Context](c4-context.md)
- [C4: Containers](c4-container.md)
- [C4: Components](c4-component.md)
- [Architectural decisions](decisions/README.md)
