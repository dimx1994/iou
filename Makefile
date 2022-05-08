JOBS ?= 4
VENV_DIR ?= venv

CODE = app tests

lint:
	black --target-version py39 --check --skip-string-normalization $(CODE)
	flake8 --jobs $(JOBS) --statistics $(CODE)
	pylint --jobs $(JOBS) --rcfile=setup.cfg $(CODE)
	mypy $(CODE)

pretty:
	black --target-version py39 --skip-string-normalization $(CODE)
	isort $(CODE)
	unify --in-place --recursive $(CODE)

prepare-local-dev:
	python3 -m venv $(VENV_DIR) && . $(VENV_DIR)/bin/activate
	pip install -r requirements-dev.txt
	@echo Virtualenv in $(VENV_DIR) is initialized

run:
	python3 -m app.server

run-test:
	coverage run --source= -m pytest tests
	coverage report --omit=tests/* -m

docker-build:
	docker-compose build iou

docker-run:
	docker compose up iou

docker-build-test:
	docker-compose build test-iou

docker-run-test:
	docker-compose run test-iou make run-test

docker-lint:
	docker-compose run test-iou make lint
