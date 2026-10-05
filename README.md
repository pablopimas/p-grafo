# P-Grafo

P-Grafo es un sistema de investigación bioinformática para estimar una estructura 3D candidata
de una proteína a partir de su secuencia y evidencia evolutiva y estructural. Está diseñado para
ejecutarse inicialmente en CPU y evolucionar de un MVP en Python a una plataforma extensible.

## Arquitectura

El proyecto combina documentación C4 con arquitectura hexagonal:

- El **dominio** expresa el lenguaje y las reglas científicas sin depender de frameworks.
- La **aplicación** orquesta casos de uso mediante puertos explícitos.
- La **infraestructura** implementa los puertos para MSA, DCA, predicción, optimización,
  persistencia y exportación.
- Los **adaptadores** exponen las entradas del sistema, comenzando por la CLI.

Las dependencias apuntan hacia el núcleo: dominio y aplicación no importan CLI, sistema de
ficheros, herramientas externas ni librerías científicas concretas.

## Mapa del repositorio

```text
src/p_grafo/
  domain/          Entidades, value objects y servicios científicos puros
  application/     Casos de uso, DTOs y puertos
  infrastructure/  Implementaciones de puertos de salida
  adapters/        Entradas CLI, API y batch
  bootstrap/       Composición de dependencias
tests/
  unit/ integration/ contract/ e2e/
docs/
  architecture/    Diagramas y decisiones C4
  scrum/           Backlog, roadmap y definición de terminado
```

## Desarrollo local

Se requiere Python 3.12 o superior.

```bash
python -m venv .venv
. .venv/bin/activate
make install
make check
```

La CLI está reservada para el Sprint 2. Tras instalar el paquete, se podrá invocar como
`p-grafo`.

## Roadmap

1. **Sprint 0:** base arquitectónica, documentación y CI.
2. **Sprint 1:** modelo de dominio, puertos y DTOs.
3. **Sprint 2:** pipeline de predicción de punta a punta con adaptadores simulados.
4. **Sprint 3:** primer pipeline científico con MSA, acoplamientos y predictor base.
5. **Sprint 4-5:** calidad, observabilidad y endurecimiento del MVP.

Consulta [la arquitectura](docs/architecture.md) y el
[backlog inicial](docs/scrum/backlog.md) para más detalle.
