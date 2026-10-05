# C4: contenedores

| Contenedor | Responsabilidad |
| --- | --- |
| CLI / API | Valida la entrada, invoca casos de uso y presenta resultados. |
| Núcleo de aplicación | Orquesta el pipeline, DTOs, políticas de ejecución y puertos. |
| Dominio | Contiene entidades y reglas científicas sin dependencias de infraestructura. |
| Infraestructura científica | Implementa MSA, DCA, persistencia, serialización y cómputo externo. |
| Almacenamiento y artefactos | Conserva entradas, resultados, configuraciones y estructuras exportadas. |

El MVP usa una CLI y sistema de ficheros local. La API HTTP y un backend de experimentos son
adaptadores futuros, no dependencias del núcleo.
