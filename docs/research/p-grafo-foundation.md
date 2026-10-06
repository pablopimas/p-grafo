# P-Grafo: CPU-based protein structure prediction

## Foundational statement

P-Grafo is a CPU-oriented protein structure prediction system. It generates candidate 3D
models from a protein sequence and from evolutionary, structural and geometric evidence. The
system produces structures, quality metrics, optimisation traces and exportable scientific
artefacts.

P-Grafo runs on CPU, without GPU dependencies and without deep learning. Its scientific basis
integrates homology modelling, multiple sequence alignments, evolutionary couplings, fragment
assembly, statistical potentials, classical machine learning, geometric constraints and
physical optimisation.

P-Grafo constitutes an interpretable, reproducible and accessible platform for bioinformatics
research, teaching and experimentation.

## Constitutive principles

- **CPU-first**: the pipeline executes on CPU and uses conventional memory.
- **Classical methods and machine learning**: the system uses bioinformatics algorithms,
  statistical potentials, physical optimisation and classical machine learning (regression,
  random forest, gradient boosting, k-nearest neighbors). It does not use deep learning.
- **Independent core**: the scientific domain does not depend on interfaces, storage, external
  tools or concrete libraries.
- **Hexagonal architecture**: ports define external dependencies and adapters materialise
  their implementations.
- **C4 documentation**: context, containers, components and architectural decisions are
  versioned.
- **Reproducibility**: executions record seeds, configuration, inputs, metrics and output
  artefacts.
- **Scientific traceability**: each prediction preserves the evidence and constraints
  involved in model generation.

## Scientific scope

The first functional line of P-Grafo covers monomeric single-chain proteins, with lengths
between 50 and 250 amino acids, without ligands or post-translational modifications. The
initial domain comprises globular proteins and generates structures in PDB format together
with JSON metadata.

P-Grafo operates in three modes:

| Mode | Structural evidence |
| --- | --- |
| `homology` | Structural template available in PDB. |
| `hybrid` | Partial template combined with evolutionary contacts. |
| `de_novo` | Fragments and constraints without a sufficient template. |

Protein-protein complexes, ligands, membrane proteins and intrinsically disordered regions
are outside this scope. Disordered regions are represented as regions of limited structural
confidence, not as a single forced structure.

## Scientific process

```text
FASTA
  ↓
sequence validation
  ↓
homolog search
  ↓
multiple sequence alignment (MSA)
  ↓
evolutionary contacts and couplings
  ↓
geometric constraints
  ↓
conformational search
  ↓
physical optimisation
  ↓
3D model + confidence
```

### Homology modelling

The `homology` mode uses homolog search, sequence-structure alignment, template selection,
backbone construction, variable region modelling, side-chain optimisation and
stereochemical evaluation.

### Fragment assembly

The `de_novo` mode assembles conformations using 3-, 5- and 9-residue fragments from a
structural library. Trajectories apply Monte Carlo moves, energetic acceptance and physical
minimisation.

The structural energy integrates the following terms:

\[
E =
w_{\text{backbone}}E_{\text{backbone}}
+
w_{\text{contact}}E_{\text{contact}}
+
w_{\text{torsion}}E_{\text{torsion}}
+
w_{\text{hydro}}E_{\text{hydrophobic}}
+
w_{\text{vdw}}E_{\text{van der Waals}}
+
w_{\text{elec}}E_{\text{electrostatic}}
+
w_{\text{solv}}E_{\text{solvation}}
\]

### Evolutionary contacts

P-Grafo derives contact evidence from multiple sequence alignments using amino acid
frequencies, joint frequencies, entropy and phylogeny corrections, covariance matrix,
regularised inversion and direct coupling analysis.

\[
J = \left(C + \lambda I\right)^{-1}
\]

In this formulation, \(C\) represents the covariance matrix, \(\lambda\) represents the
regularisation and \(J\) represents approximate direct interactions. Interactions are
transformed into distance and contact constraints between residues.

### Geometry and optimisation

Geometric constraints come from amino acid-type-dependent distributions, statistical
potentials from the PDB, linear or ridge regression, random forest, gradient boosting,
k-nearest neighbors, Markov models, frequency tables and template-based classification.

Optimisation uses Monte Carlo, simulated annealing, numerical gradient descent, L-BFGS,
conjugate gradient, basin hopping, differential evolution, local search, distance geometry,
multidimensional scaling and optimisation of angles \(\phi\), \(\psi\) and \(\chi\).

```text
contacts → distance matrix
distance matrix → approximate coordinates
approximate coordinates → backbone reconstruction
backbone → side chains
full model → energy minimisation
```

## Structural model

The initial backbone representation contains atoms `N`, `Cα`, `C`, `O` and `Cβ`. The model
records residues, atoms, Cartesian coordinates, torsion angles, covalent bonds, distances,
contacts and geometric validations.

The initial energy function is expressed as:

```text
E_total =
E_bond
+ E_angle
+ E_torsion
+ E_clash
+ E_contact
+ E_compactness
+ E_hydrophobic
```

Each trajectory starts from an initial conformation and records torsion changes, fragment
insertions, domain rotations, loop modifications, relocations between contacts and side-chain
changes. Executions retain models with better energy and geometric quality.

## Software architecture

P-Grafo uses hexagonal architecture. The domain and application do not import NumPy, SciPy,
command-line interfaces, storage, subprocesses or external programs. These dependencies are
expressed via ports and implemented via adapters.

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

### Domain

The domain contains `ProteinSequence`, `Residue`, `MultipleSequenceAlignment`,
`CouplingMatrix`, `ProteinGraph`, `DistanceConstraintSet`, `StructureModel`, `PredictionJob`
and `StructureQualityService`.

### Use cases

| Use case | Responsibility |
| --- | --- |
| `RunPredictionUseCase` | Executes the complete prediction pipeline. |
| `BuildMsaUseCase` | Builds or retrieves an MSA. |
| `ComputeCouplingsUseCase` | Generates the coevolution matrix and constraints. |
| `BuildGraphUseCase` | Builds the protein graph from sequence and evidence. |
| `PredictDistancesUseCase` | Estimates distances and angles. |
| `OptimizeStructureUseCase` | Converts constraints into 3D coordinates. |
| `ExportStructureUseCase` | Generates PDB, JSON and experiment summary. |
| `ExperimentQueryService` | Queries executions and metadata. |

### Ports

Input ports are `PredictionInputPort`, `ExperimentQueryInputPort` and
`ModelTrainingInputPort`.

Output ports are `MsaProviderPort`, `CouplingComputerPort`, `DistancePredictorPort`,
`StructureOptimizerPort`, `StructureRepositoryPort`, `ExperimentRepositoryPort`,
`StructureExporterPort`, `LoggerPort` and `ConfigPort`.

Input adapters are the CLI, HTTP API and batch executor. Output adapters include MSA
providers, DCA computation, distance predictors, optimisers, file repositories and PDB and
JSON exporters.

## Execution contract

A prediction execution receives a FASTA sequence and, optionally, a contact map. It generates
a set of structural models, selects the best-scored model and produces the following
artefacts:

```text
best_model.pdb
models.json
contacts.csv
energy_trace.csv
report.html
```

Each result includes:

```text
candidate structure
energy score
satisfied constraints
geometric violations
model diversity
confidence level
prediction mode
configuration and seed
```

Results are computational structural hypotheses. They do not constitute an experimental
determination of the protein structure.

## Product levels

| Level | Capabilities |
| --- | --- |
| P-Grafo Classic | Homology, MSA, DCA, fragments, statistical potentials, Monte Carlo and geometric optimisation. |
| P-Grafo Hybrid | Regression, random forest, XGBoost, contact classification and statistical fragment selection. |
| P-Grafo Neural | Protein language models, equivariant networks, transformers, diffusion and direct coordinate prediction. |

The current scope comprises **P-Grafo Classic** and the classical machine learning of
**P-Grafo Hybrid**. P-Grafo Neural, based on deep learning, remains outside the execution.

## Quality criteria

Execution quality is evaluated through sequence validation, constraint consistency, energy
reduction, contact violations, stereochemistry, model set diversity and repeatability with
the same seed and configuration.

| Scenario | Characterisation |
| --- | --- |
| Protein with close homolog | Direct structural evidence. |
| Protein with partial template | Combined template and constraint evidence. |
| Deep MSA and clear contacts | Informative evolutionary evidence. |
| Short protein without homologs | High structural uncertainty. |
| Long protein without evolutionary evidence | Broad conformational space and high computational cost. |

## References

- Rosetta: protein modelling suite based on fragments and physical energy.
  [Rosetta Commons](https://www.rosettacommons.org/)
- FoldX: stability and affinity tool based on empirical force field.
  [FoldX Suite](https://foldxsuite.crg.eu/)
- trRosetta: geometric constraint prediction system.
  [Nature Protocols 2021](https://www.nature.com/articles/s41596-021-00628-9)
