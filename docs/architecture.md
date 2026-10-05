# Arquitectura de P-Grafo

P-Grafo es un sistema de predicción estructural de proteínas orientado a CPU. La arquitectura
separa el lenguaje científico, la orquestación del pipeline y las implementaciones técnicas.
El modelo de documentación es C4. El modelo de implementación es hexagonal.

El documento fundacional define el alcance científico. Este documento define la estructura del
software, sus límites y sus contratos.

## Modelo arquitectónico

La arquitectura combina cuatro niveles C4 con un núcleo hexagonal:

| Nivel | Contenido |
| --- | --- |
| Contexto | Actores, sistemas externos y resultado de una predicción. |
| Contenedores | Entrada, aplicación, dominio, infraestructura y almacenamiento. |
| Componentes | Entidades, casos de uso, puertos y adaptadores. |
| Código | Módulos Python bajo `src/p_grafo`. |

Las dependencias apuntan hacia el núcleo. El dominio no conoce casos de uso, interfaces,
almacenamiento ni librerías científicas. La aplicación conoce el dominio y los puertos; no
conoce adaptadores concretos. La infraestructura y los adaptadores implementan los puertos.
`bootstrap` compone esas implementaciones en el borde del sistema.

```text
adaptadores de entrada
        ↓
puertos de entrada
        ↓
casos de uso
        ↓
dominio
        ↑
puertos de salida
        ↑
adaptadores de infraestructura
```

## Contexto

P-Grafo recibe una secuencia proteica y, cuando existe, evidencia estructural o evolutiva.
Construye alineamientos, acoplamientos, restricciones geométricas y un conjunto de modelos 3D
candidatos. Devuelve estructuras, métricas de confianza y artefactos exportables.

| Elemento externo | Relación |
| --- | --- |
| Investigador | Inicia predicciones, consulta ejecuciones y analiza artefactos. |
| Desarrollador | Extiende el sistema mediante nuevos adaptadores y algoritmos. |
| Herramientas de secuencia y alineamiento | Aportan homólogos y MSA a través de adaptadores. |
| Repositorios biológicos | Aportan secuencias, estructuras y bibliotecas de fragmentos. |
| Almacenamiento de experimentos | Conserva entradas, metadatos, modelos y reportes. |

El resultado arquitectónico de una ejecución es una hipótesis estructural computacional. No es
una determinación experimental.

## Contenedores

| Contenedor | Responsabilidad | Dependencias permitidas |
| --- | --- | --- |
| Adaptadores de entrada | Validan la invocación, traducen datos de borde e invocan puertos de entrada. | Aplicación y DTOs de borde. |
| Aplicación | Orquesta el pipeline, aplica políticas de ejecución y define puertos. | Dominio y puertos. |
| Dominio | Representa secuencias, evidencia, restricciones, grafos y estructuras. | Ninguna dependencia técnica. |
| Infraestructura científica | Implementa MSA, DCA, predicción geométrica, optimización, exportación y observabilidad. | Puertos de salida y librerías o procesos externos. |
| Almacenamiento y artefactos | Conserva FASTA, configuraciones, modelos, trazas y reportes. | Sistema de ficheros en la línea funcional actual. |

La línea funcional actual expone una CLI y persiste en sistema de ficheros local. La API HTTP
y el ejecutor batch existen como adaptadores de entrada del mismo núcleo. Un backend de
experimentos sustituye el adaptador de persistencia sin alterar dominio ni casos de uso.

## Componentes

### Dominio

| Componente | Responsabilidad |
| --- | --- |
| `ProteinSequence` | Representa y valida la secuencia primaria. |
| `Residue` | Representa identidad y propiedades de un residuo. |
| `MultipleSequenceAlignment` | Representa el alineamiento múltiple. |
| `CouplingMatrix` | Representa evidencia de coevolución entre posiciones. |
| `ProteinGraph` | Representa nodos, aristas, pesos y anotaciones. |
| `DistanceConstraintSet` | Representa restricciones geométricas derivadas. |
| `StructureModel` | Representa coordenadas, energía, puntuación y metadatos. |
| `PredictionJob` | Agrega una ejecución y su evidencia. |
| `StructureQualityService` | Evalúa consistencia, estereoquímica y confianza. |

La representación estructural registra átomos `N`, `Cα`, `C`, `O` y `Cβ`, coordenadas,
ángulos torsionales, enlaces, distancias y contactos.

### Aplicación

| Caso de uso | Responsabilidad |
| --- | --- |
| `RunPredictionUseCase` | Ejecuta el pipeline completo. |
| `BuildMsaUseCase` | Construye o recupera un MSA. |
| `ComputeCouplingsUseCase` | Calcula acoplamientos y restricciones evolutivas. |
| `BuildGraphUseCase` | Construye el grafo desde secuencia y evidencia. |
| `PredictDistancesUseCase` | Estima distancias y ángulos. |
| `OptimizeStructureUseCase` | Transforma restricciones en coordenadas 3D. |
| `ExportStructureUseCase` | Genera PDB, JSON y resumen. |
| `ExperimentQueryService` | Consulta ejecuciones y metadatos. |

`RunPredictionUseCase` selecciona el modo `homology`, `hybrid` o `de_novo` según la evidencia
disponible y coordina los demás casos de uso. La política de ejecución registra semilla,
configuración, entradas y artefactos.

### Puertos

Puertos de entrada:

| Puerto | Operación |
| --- | --- |
| `PredictionInputPort` | Ejecuta una predicción completa. |
| `ExperimentQueryInputPort` | Consulta una ejecución. |
| `ModelTrainingInputPort` | Recalibra el modelo base de distancias. |

Puertos de salida:

| Puerto | Operación |
| --- | --- |
| `MsaProviderPort` | Obtiene o aloja un MSA. |
| `CouplingComputerPort` | Calcula una matriz de acoplamientos. |
| `DistancePredictorPort` | Predice restricciones geométricas. |
| `StructureOptimizerPort` | Optimiza una estructura 3D. |
| `StructureRepositoryPort` | Persiste estructuras. |
| `ExperimentRepositoryPort` | Persiste metadatos de ejecución. |
| `StructureExporterPort` | Exporta formatos científicos. |
| `LoggerPort` | Registra eventos y telemetría. |
| `ConfigPort` | Expone la configuración efectiva. |

### Adaptadores

| Adaptador | Puerto |
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

Los dobles de prueba implementan los mismos puertos de salida. El caso de uso no distingue un
doble de una implementación científica.

## Pipeline y límites

```text
FASTA
  → PredictionInputPort
  → validación de ProteinSequence
  → MsaProviderPort
  → CouplingComputerPort
  → DistancePredictorPort
  → BuildGraphUseCase
  → StructureOptimizerPort
  → StructureRepositoryPort
  → StructureExporterPort
  → PDB, JSON, CSV y reporte
```

El modo `homology` incorpora búsqueda de moldes y alineamiento secuencia-estructura mediante
puertos de infraestructura. El modo `hybrid` combina molde parcial y contactos evolutivos. El
modo `de_novo` compone fragmentos y restricciones sin un molde suficiente. Esos modos cambian
la evidencia de entrada; no cambian el contrato del caso de uso principal.

El alcance estructural cubre proteínas monoméricas de una sola cadena, de 50 a 250
aminoácidos, sin ligandos ni modificaciones postraduccionales. Complejos, membranas y ligandos
quedan fuera del contrato actual.

## Módulos

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

| Módulo | Contenido |
| --- | --- |
| `domain` | Entidades, value objects, servicios y excepciones científicas. |
| `application` | Casos de uso, DTOs, políticas y puertos. |
| `infrastructure` | Implementaciones de puertos de salida. |
| `adapters` | CLI, API HTTP y batch. |
| `bootstrap` | Composición de casos de uso y adaptadores. |

Los DTOs cruzan el borde de la aplicación. Las entidades de dominio no salen serializadas
directamente por la CLI ni por los exportadores.

## Composición

`bootstrap/container.py` instancia adaptadores, los asigna a puertos y construye los casos de
uso. Ningún caso de uso construye sus dependencias concretas. La CLI obtiene el caso de uso
desde el contenedor de composición.

Una ejecución produce:

```text
best_model.pdb
models.json
contacts.csv
energy_trace.csv
report.html
```

El reporte incluye estructura candidata, score energético, restricciones satisfechas,
violaciones geométricas, diversidad entre modelos, confianza, modo de predicción,
configuración y semilla.

## Pruebas

| Tipo | Alcance |
| --- | --- |
| Unidad | Dominio y casos de uso con dobles de puertos. |
| Contrato | Cada puerto y su adaptador. |
| Integración | Pipeline con datos de referencia. |
| Extremo a extremo | Invocación completa desde un adaptador de entrada. |

Las pruebas de dominio no importan infraestructura. Las pruebas de contrato verifican que un
adaptador cumple el puerto sin exponer su librería o proceso externo al núcleo.

## Niveles de producto

| Nivel | Capacidades arquitectónicas |
| --- | --- |
| P-Grafo Classic | Homología, MSA, DCA, fragmentos, potenciales estadísticos y optimización física. |
| P-Grafo Hybrid | Regresión, random forest, gradient boosting y selección estadística de fragmentos detrás de los mismos puertos. |
| P-Grafo Neural | Modelos de lenguaje, redes equivariantes y predicción directa de coordenadas detrás de los mismos puertos. |

La línea de ejecución actual es P-Grafo Classic. Hybrid y Neural permanecen fuera de esa
ejecución y entran, cuando existen, como adaptadores de `DistancePredictorPort`,
`CouplingComputerPort` o `StructureOptimizerPort`.

## Decisiones vigentes

- Python 3.12 y layout `src/` constituyen la base de empaquetado.
- El núcleo científico permanece libre de CLI, FastAPI, NumPy, SciPy, XGBoost, subprocess y
  acceso directo a ficheros.
- El sistema de ficheros es el adaptador de persistencia de la línea funcional actual.
- PDB y JSON son los formatos de intercambio de estructuras y metadatos.
- Cada predicción conserva evidencia, restricciones, semilla y configuración.

## Documentos relacionados

- [Declaración fundacional](P-Grafo%20protein%20CPU%20prediction.md)
- [C4: contexto](architecture/c4-context.md)
- [C4: contenedores](architecture/c4-container.md)
- [C4: componentes](architecture/c4-component.md)
- [Decisiones](architecture/decisions/README.md)
