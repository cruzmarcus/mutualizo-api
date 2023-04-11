SHELL := /bin/bash


POETRY_VERSION = $$(cat $$PWD/Dockerfile | grep POETRY_VERSION= | grep -o -P '(?<==).*')
SERVICE_NAME = mutualizo-api


poetry-install-config:
	curl -sSL https://install.python-poetry.org | python3.10 - --version $(POETRY_VERSION)	&& \
		export PATH="$$HOME/.local/bin:$$PATH"  && \
		poetry config virtualenvs.in-project true


poetry-uninstall:
	curl -sSL https://install.python-poetry.org | python3.10 - --uninstall


create-dev-env:
	make poetry-install-config && \
		poetry env use 3.10 && poetry install


update-dev-dependencies:
	poetry update


run-tests:
	poetry run pytest -vv --durations=10 tests/


generate-tests-coverage-src: 
	poetry run pytest --cov src --cov-report xml:cov.xml


tests-coverage-average:
	poetry run pytest --cov src


build-image:
	docker image build -t $(SERVICE_NAME) .


run-container-api:
	docker compose up -d


cleanup-container:
	docker compose down


run-api:
	poetry run uvicorn src.api.main:app --host 0.0.0.0 --reload


kill-api:
	ps axjf | grep 'make run-api' | awk '{print -$$3}' | xargs kill -9


setup:
	make run-api


cleanup:
	make kill-api
