FROM python:3.10-slim as requirements-stage

ARG POETRY_VERSION=1.4.2

COPY pyproject.toml poetry.lock /

RUN pip install "poetry==$POETRY_VERSION" 
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.10-slim

COPY --from=requirements-stage /requirements.txt /

RUN pip install -r requirements.txt

COPY src /src