# C4: componentes

## Aplicación

Los casos de uso previstos son `RunPredictionUseCase`, `BuildMsaUseCase`,
`ComputeCouplingsUseCase`, `BuildGraphUseCase`, `PredictDistancesUseCase`,
`OptimizeStructureUseCase`, `ExportStructureUseCase` y `ExperimentQueryService`.

Los puertos de entrada expresan ejecutar una predicción y consultar experimentos. Los puertos
de salida aíslan MSA, cálculo de acoplamientos, predicción de distancias, optimización,
repositorios, exportadores, configuración y observabilidad.

## Dominio

El dominio contendrá `ProteinSequence`, `Residue`, `MultipleSequenceAlignment`,
`CouplingMatrix`, `ProteinGraph`, `DistanceConstraintSet`, `StructureModel`, `PredictionJob`
y `StructureQualityService`.

## Adaptadores iniciales

La primera iteración del pipeline conectará la CLI con dobles de prueba para MSA, DCA,
predicción y optimización. Las implementaciones reales previstas incluyen wrappers de
subprocesos, repositorios de ficheros y exportadores PDB/JSON.
