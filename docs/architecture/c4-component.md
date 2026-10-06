# C4: Components

## Domain

| Component | Responsibility |
| --- | --- |
| `ProteinSequence` | Represents and validates the primary sequence. |
| `Residue` | Represents the identity and properties of a residue. |
| `MultipleSequenceAlignment` | Represents the multiple sequence alignment. |
| `CouplingMatrix` | Represents coevolution evidence between positions. |
| `ProteinGraph` | Represents nodes, edges, weights and annotations. |
| `DistanceConstraintSet` | Represents derived geometric constraints. |
| `StructureModel` | Represents coordinates, energy, score and metadata. |
| `PredictionJob` | Aggregates an execution and its evidence. |
| `StructureQualityService` | Evaluates consistency, stereochemistry and confidence. |

The structural representation records atoms `N`, `Cα`, `C`, `O` and `Cβ`, together with
coordinates, torsion angles, bonds, distances and contacts.

## Application

| Use case | Responsibility |
| --- | --- |
| `RunPredictionUseCase` | Executes the complete pipeline. |
| `BuildMsaUseCase` | Builds or retrieves an MSA. |
| `ComputeCouplingsUseCase` | Computes couplings and evolutionary constraints. |
| `BuildGraphUseCase` | Builds the graph from sequence and evidence. |
| `PredictDistancesUseCase` | Estimates distances and angles. |
| `OptimizeStructureUseCase` | Transforms constraints into 3D coordinates. |
| `ExportStructureUseCase` | Generates PDB, JSON and a summary. |
| `ExperimentQueryService` | Queries executions and metadata. |

`RunPredictionUseCase` selects `homology`, `hybrid` or `de_novo` from the available evidence
and coordinates the other use cases. The execution policy records the seed, configuration,
inputs and artefacts. These modes change the input evidence; they do not change the main use
case contract.

Input ports express executing a prediction, querying experiments and recalibrating the
baseline distance model. Output ports isolate MSA, coupling computation, distance prediction,
optimisation, repositories, exporters, configuration and observability.

| Port | Direction | Operation |
| --- | --- | --- |
| `PredictionInputPort` | Input | Executes a complete prediction. |
| `ExperimentQueryInputPort` | Input | Queries an execution. |
| `ModelTrainingInputPort` | Input | Recalibrates the baseline distance model. |
| `MsaProviderPort` | Output | Obtains or hosts an MSA. |
| `CouplingComputerPort` | Output | Computes a coupling matrix. |
| `DistancePredictorPort` | Output | Predicts geometric constraints. |
| `StructureOptimizerPort` | Output | Optimises a 3D structure. |
| `StructureRepositoryPort` | Output | Persists structures. |
| `ExperimentRepositoryPort` | Output | Persists execution metadata. |
| `StructureExporterPort` | Output | Exports scientific formats. |
| `LoggerPort` | Output | Records events and telemetry. |
| `ConfigPort` | Output | Exposes the effective configuration. |

## Pipeline and boundaries

```text
FASTA
  → PredictionInputPort
  → ProteinSequence validation
  → MsaProviderPort
  → CouplingComputerPort
  → DistancePredictorPort
  → BuildGraphUseCase
  → StructureOptimizerPort
  → StructureRepositoryPort
  → StructureExporterPort
  → PDB, JSON, CSV and report
```

The `homology` mode incorporates template search and sequence-structure alignment through
infrastructure ports. The `hybrid` mode combines a partial template with evolutionary
contacts. The `de_novo` mode assembles fragments and constraints without a sufficient
template.

The structural scope covers monomeric single-chain proteins of 50 to 250 amino acids, without
ligands or post-translational modifications. Complexes, membrane proteins and ligands are
outside the current contract. The scientific statement of that scope is in the
[foundational document](../research/p-grafo-foundation.md).

## Initial adapters

The first pipeline iteration connects the CLI with test doubles for MSA, DCA, prediction and
optimisation. Planned real implementations include subprocess wrappers, file repositories and
PDB/JSON exporters. The use case does not distinguish a double from a scientific
implementation.

| Adapter | Port |
| --- | --- |
| `CliPredictionController` | `PredictionInputPort` |
| `FilesystemStructureRepository` | `StructureRepositoryPort` |
| `FilesystemExperimentRepository` | `ExperimentRepositoryPort` |
| `SubprocessMsaAdapter` | `MsaProviderPort` |
| `PlmDcaAdapter` | `CouplingComputerPort` |
| `StatisticalDistancePredictorAdapter` | `DistancePredictorPort` |
| `ScipyStructureOptimizerAdapter` | `StructureOptimizerPort` |
| `PdbExporterAdapter` | `StructureExporterPort` |
| `JsonReportExporterAdapter` | `StructureExporterPort` |

See the [architecture overview](README.md).
