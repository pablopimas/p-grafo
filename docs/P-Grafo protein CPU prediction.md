# P-Grafo: predicción estructural de proteínas en CPU

## Declaración fundacional

P-Grafo es un sistema de predicción estructural de proteínas orientado a CPU. Genera modelos
tridimensionales candidatos a partir de una secuencia proteica y de evidencia evolutiva,
estructural y geométrica. El sistema produce estructuras, métricas de calidad, trazas de
optimización y artefactos científicos exportables.

P-Grafo opera sin redes neuronales ni dependencias de GPU. Su base científica integra
modelado por homología, alineamientos múltiples, acoplamientos evolutivos, ensamblaje de
fragmentos, potenciales estadísticos, restricciones geométricas y optimización física.

P-Grafo constituye una plataforma interpretable, reproducible y accesible para investigación,
docencia y experimentación bioinformática.

## Principios constitutivos

- **CPU-first**: el pipeline se ejecuta en CPU y utiliza memoria convencional.
- **Métodos clásicos**: el sistema utiliza algoritmos bioinformáticos, potenciales estadísticos
  y optimización física; no utiliza redes neuronales.
- **Núcleo independiente**: el dominio científico no depende de interfaces, almacenamiento,
  herramientas externas ni librerías concretas.
- **Arquitectura hexagonal**: los puertos definen las dependencias externas y los adaptadores
  materializan sus implementaciones.
- **Documentación C4**: el contexto, los contenedores, los componentes y las decisiones de
  arquitectura se mantienen versionados.
- **Reproducibilidad**: las ejecuciones registran semillas, configuración, entradas, métricas
  y artefactos de salida.
- **Trazabilidad científica**: cada predicción conserva la evidencia y las restricciones que
  intervienen en la generación del modelo.

## Alcance científico

La primera línea funcional de P-Grafo cubre proteínas monoméricas de una sola cadena, con
longitudes entre 50 y 250 aminoácidos, sin ligandos ni modificaciones postraduccionales. El
dominio inicial comprende proteínas globulares y genera estructuras en formato PDB junto con
metadatos en JSON.

P-Grafo opera en tres modos:

| Modo | Evidencia estructural |
| --- | --- |
| `homology` | Molde estructural disponible en PDB. |
| `hybrid` | Molde parcial combinado con contactos evolutivos. |
| `de_novo` | Fragmentos y restricciones sin un molde suficiente. |

Los complejos proteína-proteína, los ligandos, las proteínas de membrana y las regiones
intrínsecamente desordenadas quedan fuera de este alcance. Las regiones desordenadas se
representan como regiones de confianza estructural limitada, no como una estructura única
forzada.

## Proceso científico

```text
FASTA
  ↓
validación de secuencia
  ↓
búsqueda de homólogos
  ↓
alineamiento múltiple (MSA)
  ↓
contactos y acoplamientos evolutivos
  ↓
restricciones geométricas
  ↓
búsqueda de conformaciones
  ↓
optimización física
  ↓
modelo 3D + confianza
```

### Modelado por homología

El modo `homology` usa búsqueda de homólogos, alineamiento secuencia-estructura, selección de
moldes, construcción de esqueleto, modelado de regiones variables, optimización de cadenas
laterales y evaluación estereoquímica.

### Ensamblaje de fragmentos

El modo `de_novo` compone conformaciones mediante fragmentos de 3, 5 y 9 residuos procedentes
de una biblioteca estructural. Las trayectorias aplican movimientos de Monte Carlo,
aceptación energética y minimización física.

La energía estructural integra los siguientes términos:

\[
E =
w_{\text{rama}}E_{\text{backbone}}
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

### Contactos evolutivos

P-Grafo deriva evidencia de contacto de alineamientos múltiples mediante frecuencias de
aminoácidos, frecuencias conjuntas, correcciones de entropía y filogenia, matriz de
covarianza, inversión regularizada y análisis de acoplamiento directo.

\[
J = \left(C + \lambda I\right)^{-1}
\]

En esta formulación, \(C\) representa la matriz de covarianza, \(\lambda\) representa la
regularización y \(J\) representa interacciones directas aproximadas. Las interacciones se
transforman en restricciones de distancia y contacto entre residuos.

### Geometría y optimización

Las restricciones geométricas proceden de distribuciones dependientes del tipo de aminoácido,
potenciales estadísticos del PDB, regresión lineal o ridge, random forest, gradient boosting,
k-nearest neighbors, modelos de Markov, tablas de frecuencia y clasificación basada en
plantillas.

La optimización utiliza Monte Carlo, simulated annealing, descenso de gradiente numérico,
L-BFGS, gradiente conjugado, basin hopping, differential evolution, búsqueda local,
geometría de distancias, multidimensional scaling y optimización de ángulos
\(\phi\), \(\psi\) y \(\chi\).

```text
contactos → matriz de distancias
matriz de distancias → coordenadas aproximadas
coordenadas aproximadas → reconstrucción del backbone
backbone → cadenas laterales
modelo completo → minimización energética
```

## Modelo estructural

La representación inicial del backbone contiene los átomos `N`, `Cα`, `C`, `O` y `Cβ`. El
modelo registra residuos, átomos, coordenadas cartesianas, ángulos torsionales, enlaces
covalentes, distancias, contactos y validaciones geométricas.

La función de energía inicial se expresa como:

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

Cada trayectoria parte de una conformación inicial y registra los cambios de torsiones,
inserciones de fragmentos, rotaciones de dominios, modificaciones de loops, recolocaciones
entre contactos y cambios de cadenas laterales. Las ejecuciones conservan los modelos con
mejor energía y calidad geométrica.

## Arquitectura de software

P-Grafo utiliza arquitectura hexagonal. El dominio y la aplicación no importan NumPy, SciPy,
interfaces de línea de comandos, almacenamiento, subprocesos ni programas externos. Estas
dependencias se expresan mediante puertos y se implementan mediante adaptadores.

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

### Dominio

El dominio contiene `ProteinSequence`, `Residue`, `MultipleSequenceAlignment`,
`CouplingMatrix`, `ProteinGraph`, `DistanceConstraintSet`, `StructureModel`, `PredictionJob`
y `StructureQualityService`.

### Casos de uso

| Caso de uso | Responsabilidad |
| --- | --- |
| `RunPredictionUseCase` | Ejecuta el pipeline completo de predicción. |
| `BuildMsaUseCase` | Construye o recupera un MSA. |
| `ComputeCouplingsUseCase` | Genera la matriz de coevolución y restricciones. |
| `BuildGraphUseCase` | Construye el grafo proteico desde secuencia y evidencia. |
| `PredictDistancesUseCase` | Estima distancias y ángulos. |
| `OptimizeStructureUseCase` | Convierte restricciones en coordenadas 3D. |
| `ExportStructureUseCase` | Genera PDB, JSON y resumen del experimento. |
| `ExperimentQueryService` | Consulta ejecuciones y metadatos. |

### Puertos

Los puertos de entrada son `PredictionInputPort`, `ExperimentQueryInputPort` y
`ModelTrainingInputPort`.

Los puertos de salida son `MsaProviderPort`, `CouplingComputerPort`, `DistancePredictorPort`,
`StructureOptimizerPort`, `StructureRepositoryPort`, `ExperimentRepositoryPort`,
`StructureExporterPort`, `LoggerPort` y `ConfigPort`.

Los adaptadores de entrada son la CLI, la API HTTP y el ejecutor batch. Los adaptadores de
salida incluyen proveedores de MSA, cálculo DCA, predictores de distancia, optimizadores,
repositorios de ficheros y exportadores PDB y JSON.

## Contrato de ejecución

Una ejecución de predicción recibe una secuencia FASTA y, de forma opcional, un mapa de
contactos. Genera un conjunto de modelos estructurales, selecciona el modelo mejor puntuado y
produce los siguientes artefactos:

```text
best_model.pdb
models.json
contacts.csv
energy_trace.csv
report.html
```

Cada resultado incluye:

```text
estructura candidata
score energético
restricciones satisfechas
violaciones geométricas
diversidad entre modelos
nivel de confianza
modo de predicción
configuración y semilla
```

Los resultados son hipótesis estructurales computacionales. No constituyen una determinación
experimental de la estructura proteica.

## Niveles del producto

| Nivel | Capacidades |
| --- | --- |
| P-Grafo Classic | Homología, MSA, DCA, fragmentos, potenciales estadísticos, Monte Carlo y optimización geométrica. |
| P-Grafo Hybrid | Regresión, random forest, XGBoost, clasificación de contactos y selección estadística de fragmentos. |
| P-Grafo Neural | Modelos de lenguaje proteico, redes equivariantes, transformers, difusión y predicción directa de coordenadas. |

El alcance fundacional actual corresponde a **P-Grafo Classic**. P-Grafo Hybrid y P-Grafo
Neural son niveles arquitectónicamente compatibles y permanecen fuera de la ejecución actual.

## Criterios de calidad

La calidad de una ejecución se evalúa mediante validación de secuencia, consistencia de las
restricciones, reducción de energía, violaciones de contactos, estereoquímica, diversidad del
conjunto de modelos y repetibilidad con la misma semilla y configuración.

| Escenario | Caracterización |
| --- | --- |
| Proteína con homólogo cercano | Evidencia estructural directa. |
| Proteína con plantilla parcial | Evidencia combinada de plantilla y restricciones. |
| MSA profundo y contactos claros | Evidencia evolutiva informativa. |
| Proteína corta sin homólogos | Incertidumbre estructural elevada. |
| Proteína larga sin evidencia evolutiva | Espacio conformacional amplio y coste computacional elevado. |

## Referencias

- Rosetta: suite de modelado proteico basada en fragmentos y energía física.
  [Rosetta Commons](https://www.rosettacommons.org/)
- FoldX: herramienta de estabilidad y afinidad basada en campo de fuerzas empírico.
  [FoldX Suite](https://foldxsuite.crg.eu/)
- trRosetta: sistema de predicción de restricciones geométricas.
  [Nature Protocols 2021](https://www.nature.com/articles/s41596-021-00628-9)
