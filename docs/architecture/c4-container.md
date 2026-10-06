# C4: Containers

| Container | Responsibility | Allowed dependencies |
| --- | --- | --- |
| CLI / API | Validates input, translates boundary data, invokes use cases and presents results. | Application and boundary DTOs. |
| Application core | Orchestrates the pipeline, DTOs, execution policies and ports. | Domain and ports. |
| Domain | Contains entities and scientific rules without infrastructure dependencies. | No technical dependencies. |
| Scientific infrastructure | Implements MSA, DCA, geometric prediction, optimisation, persistence, serialisation, export and external computation. | Output ports and external libraries or processes. |
| Storage and artefacts | Preserves FASTA, configurations, models, traces, reports and exported structures. | Filesystem in the current functional line. |

The current functional line exposes a CLI and persists to the local filesystem. The HTTP API
and the batch executor are input adapters over the same core; they are not core dependencies.
An experiment backend can replace the persistence adapter without altering the domain or the
use cases.

See the [architecture overview](README.md).

## Schemas (future)

Schemas will be added as the system evolves beyond the MVP. Planned additions:

### CLI interface schema

```yaml
command: predict
arguments:
  fasta:
    flag: "--fasta"
    type: path
    required: true
  contacts:
    flag: "--contacts"
    type: path
    required: false
  mode:
    flag: "--mode"
    type: enum
    values: [homology, hybrid, de_novo]
  models:
    flag: "--models"
    type: int
    default: 20
  iterations:
    flag: "--iterations"
    type: int
    default: 100000
  seed:
    flag: "--seed"
    type: int
    required: false
  output:
    flag: "--output"
    type: path
    required: true
```

### Output report schema (JSON)

```json
{
  "job_id": "job_001",
  "mode": "de_novo",
  "sequence_id": "seq_001",
  "best_model": {
    "path": "best_model.pdb",
    "energy": -1234.56,
    "constraints_satisfied": 145,
    "confidence": 0.72
  },
  "models": [
    {
      "path": "model_001.pdb",
      "energy": -1200.12,
      "constraints_satisfied": 140,
      "confidence": 0.68
    }
  ],
  "artefacts": {
    "contacts": "contacts.csv",
    "energy_trace": "energy_trace.csv",
    "report": "report.html"
  },
  "configuration": {
    "models": 20,
    "iterations": 100000
  },
  "seed": 42,
  "started_at": "2026-10-06T13:00:00Z",
  "completed_at": "2026-10-06T13:45:00Z"
}
```

### Domain entity schemas (future)

When Pydantic or similar is introduced for DTOs, domain entities such as `ProteinSequence`,
`StructureModel` and `PredictionJob` will have explicit type schemas documented here.

### Database schema (future)

If persistence migrates from filesystem to a database, the schema will be documented in a
separate ADR and linked from this document.
