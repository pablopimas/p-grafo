# C4: Context

P-Grafo receives a protein sequence and, when available, structural or evolutionary evidence.
It builds alignments, couplings and geometric constraints, and produces candidate 3D structures
with confidence metrics and exportable artefacts.

The outcome of an execution is a computational structural hypothesis. It is not an
experimental determination of the protein structure.

| External element | Relationship with P-Grafo |
| --- | --- |
| Bioinformatics researcher | Initiates predictions, queries executions, compares results and analyses structures. |
| Developer | Incorporates adapters and algorithms. |
| MSA and alignment tools | Provide homologs and alignments through infrastructure adapters. |
| Biological repositories | Provide sequences, structures and fragment libraries for training or validation. |
| Experiment storage | Preserves inputs, metadata, models and reports. |

The researcher initially interacts through a CLI. The system may consult external engines,
saves metadata and results, and exports PDB, JSON and reports.

See the [architecture overview](README.md).
