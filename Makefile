.PHONY: help test check clean
VERSION=$(shell git rev-parse --short HEAD)
APP_NAME=pynguin
DOCKER_REPO=pynguin

.DEFAULT: help
help:
	@echo "make test"
	@echo "        run tests"
	@echo "make lint"
	@echo "        run pylint, and mypy"
	@echo "make check"
	@echo "        run black, mypy, pylint, and pytest"
	@echo "make black"
	@echo "        run black code formatter"
	@echo "make clean"
	@echo "        clean-up build artifacts"

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

clean: clean-build clean-pyc

test:
	pytest -p no:sugar -v --cov=pynguin --cov-branch --cov-report=term-missing --cov-report html:cov_html tests/

lint: pylint mypy

pylint:
	pylint pynguin

mypy:
	mypy pynguin

black:
	black .

isort:
	isort

build-docker:
	docker build -t $(APP_NAME) .
	docker tag $(APP_NAME) $(DOCKER_REPO)/$(APP_NAME):$(VERSION)

check: isort black mypy pylint test
