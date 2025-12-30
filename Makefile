# Makefile for fastapi_tut
# Usage: make <target> [VARIABLE=value]

PYTHON ?= python3
VENV_DIR ?= .venv
DATABASE_URL ?= sqlite:///./dev.db
ALEMBIC ?= alembic
UVICORN ?= uvicorn
PIP ?= pip

.PHONY: help venv install setup run run-prod makemigration migrate test docs-serve docs-build lint format clean

help:
	@echo "Available targets:" \
		"\n  venv         Create virtualenv and upgrade pip" \
		"\n  install      Install Python deps (from requirements.txt)" \
		"\n  setup        Create venv and install deps" \
		"\n  run          Run dev server (uvicorn, reload)" \
		"\n  run-prod     Run production server (uvicorn)" \
		"\n  makemigration m=MSG   Create alembic migration (autogenerate)" \
		"\n  migrate      Apply alembic migrations (upgrade head)" \
		"\n  test         Run tests with pytest" \
		"\n  docs-serve   Serve docs locally with mkdocs" \
		"\n  docs-build   Build static docs with mkdocs" \
		"\n  lint         Run linter (ruff) if available" \
		"\n  format       Format code (ruff format)" \
		"\n  clean        Remove common temporary files"

venv:
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtualenv created at $(VENV_DIR); activate with: source $(VENV_DIR)/bin/activate"
	$(VENV_DIR)/bin/$(PIP) install -U pip setuptools wheel

install:
	$(PIP) install -r requirements.txt

setup: venv install
	@echo "Setup complete. Activate the venv with: source $(VENV_DIR)/bin/activate"

run:
	DATABASE_URL=$(DATABASE_URL) $(UVICORN) app.main:app --reload

run-prod:
	DATABASE_URL=$(DATABASE_URL) $(UVICORN) app.main:app --host 0.0.0.0 --port 8000

makemigration:
ifndef m
	$(error Please provide a message via m="create users")
endif
	DATABASE_URL=$(DATABASE_URL) $(ALEMBIC) revision --autogenerate -m "$(m)"

migrate:
	DATABASE_URL=$(DATABASE_URL) $(ALEMBIC) upgrade head

test:
	pytest -q

docs-serve:
	mkdocs serve

docs-build:
	mkdocs build

lint:
	ruff check . || echo "ruff not installed"

format:
	ruff format . || echo "ruff not installed"

clean:
	rm -rf $(VENV_DIR) .pytest_cache .mypy_cache .ruff_cache site
	find . -name "__pycache__" -type d -exec rm -rf {} + || true
	find . -name "*.db" -maxdepth 1 -type f -exec rm -f {} + || true
