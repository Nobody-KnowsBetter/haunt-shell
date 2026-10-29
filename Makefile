.PHONY: help install test test-cov run seance ofrenda autopsy whisper clean

help:
	@echo "HauntShell 👻 - Developer Commands"
	@echo "  make install    - Install package in editable mode with requirements"
	@echo "  make test       - Run all 39 unit & integration tests"
	@echo "  make test-cov   - Run tests with code coverage report"
	@echo "  make seance     - Start interactive séance chamber with Clippy"
	@echo "  make ofrenda    - Display the Grand Altar of Ancestors"
	@echo "  make whisper    - Hear a whisper from unallocated space"
	@echo "  make clean      - Clean cache and build artifacts"

install:
	bash setup.sh

test:
	pytest -v

test-cov:
	pytest -v --cov=hauntshell --cov-report=term-missing

seance:
	haunt chamber clippy

ofrenda:
	haunt ofrenda

whisper:
	haunt whisper

clean:
	rm -rf .pytest_cache .coverage htmlcov build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
