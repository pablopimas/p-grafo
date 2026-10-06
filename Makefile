SHELL := /bin/bash

PYTHON ?= python
PYTEST ?= $(PYTHON) -m pytest
RUFF ?= $(PYTHON) -m ruff
PIP ?= $(PYTHON) -m pip
BUILD ?= $(PYTHON) -m build
PRE_COMMIT ?= $(PYTHON) -m pre_commit

SRC := src
TESTS := tests
PACKAGE := p_grafo

.PHONY: help install install-dev format format-check lint test test-unit test-contract test-integration test-e2e check build clean pre-commit

help:
	@echo "P-Grafo development commands"
	@echo ""
	@echo "  make install           Install the package in editable mode"
	@echo "  make install-dev       Install package with development dependencies"
	@echo "  make format            Format source code and tests with Ruff"
	@echo "  make format-check      Check formatting without modifying files"
	@echo "  make lint              Run Ruff lint checks"
	@echo "  make test              Run the complete test suite"
	@echo "  make test-unit         Run unit tests"
	@echo "  make test-contract     Run contract tests"
	@echo "  make test-integration  Run integration tests"
	@echo "  make test-e2e          Run end-to-end tests"
	@echo "  make check             Run formatting, linting, tests and package build"
	@echo "  make build             Build source and wheel distributions"
	@echo "  make pre-commit        Run all pre-commit hooks"
	@echo "  make clean             Remove generated local artefacts"

install:
	$(PIP) install -e .

install-dev:
	$(PIP) install -e ".[dev]"

format:
	$(RUFF) format $(SRC) $(TESTS)
	$(RUFF) check --fix $(SRC) $(TESTS)

format-check:
	$(RUFF) format --check $(SRC) $(TESTS)

lint:
	$(RUFF) check $(SRC) $(TESTS)

test:
	$(PYTEST) $(TESTS) -q

test-unit:
	$(PYTEST) $(TESTS)/unit -q

test-contract:
	$(PYTEST) $(TESTS)/contract -q

test-integration:
	$(PYTEST) $(TESTS)/integration -q

test-e2e:
	$(PYTEST) $(TESTS)/e2e -q

check: format-check lint test build

build:
	rm -rf dist build
	$(BUILD)

pre-commit:
	$(PRE_COMMIT) run --all-files

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache
	rm -rf build dist
	rm -rf .coverage coverage.xml htmlcov
	rm -rf ./**/__pycache__
	rm -rf $(SRC)/*.egg-info
	rm -rf $(SRC)/$(PACKAGE).egg-info
	rm -rf $(PACKAGE).egg-info
