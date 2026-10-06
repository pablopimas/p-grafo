# Definition of Done

A story is considered done when it meets the following criteria:

## Code quality

- [ ] Code passes linting (ruff, mypy or equivalent).
- [ ] Code is formatted consistently.
- [ ] No TODOs or FIXMEs left in the changed files (or they are tracked as separate issues).

## Testing

- [ ] Unit tests cover domain logic and use cases.
- [ ] Contract tests verify port/adapter boundaries (if applicable).
- [ ] All tests pass locally and in CI.
- [ ] Test coverage does not decrease for critical modules.

## Architecture

- [ ] Changes respect hexagonal architecture (domain and application do not import infrastructure).
- [ ] No new dependencies added to the core without justification.
- [ ] C4 diagrams are updated if the change affects context, containers or components.
- [ ] ADRs are created or updated for significant architectural decisions.

## Documentation

- [ ] README or relevant docs are updated if behaviour changes.
- [ ] Public functions and classes have docstrings.
- [ ] Usage examples are updated if CLI or API changes.

## Scientific validity (for pipeline changes)

- [ ] The change includes a verifiable scientific criterion (e.g., energy decreases, constraints are satisfied, RMSD improves).
- [ ] Results are reproducible with a fixed seed.
- [ ] Limitations are documented if the change introduces approximations.

## Integration

- [ ] The change integrates without breaking existing functionality.
- [ ] CI pipeline passes on the pull request.
- [ ] The feature can be demonstrated end-to-end (CLI invocation produces expected artefacts).

## Review

- [ ] Code review is completed and approved.
- [ ] The pull request references the relevant issue or epic.
- [ ] Changelog or release notes are updated if the change is user-facing.
