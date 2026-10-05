# C4: contexto

P-Grafo recibe una secuencia de proteína, construye evidencia evolutiva y estructural, estima
restricciones geométricas y produce una estructura 3D candidata con métricas de confianza y
artefactos exportables.

| Elemento externo | Relación con P-Grafo |
| --- | --- |
| Investigador bioinformático | Inicia predicciones, compara resultados y analiza estructuras. |
| Desarrollador | Incorpora adaptadores y algoritmos. |
| Herramientas de MSA | Proporcionan alineamientos mediante adaptadores de infraestructura. |
| Repositorios biológicos | Aportan datos para entrenamiento o validación. |

El investigador interactúa inicialmente mediante una CLI. El sistema puede consultar motores
externos, guarda metadatos y resultados, y exporta PDB, JSON y reportes.
