# Intersection Over Union Wed Service

## Description

Web service provides API to calculate Intersection Over Union https://johfischer.com/2021/11/04/intersection-over-union-iou/

## Usage

**Requirements:**
Application requires docker, docker-compose, python 3.9 to be installed.

To prepare local development and install dev requirements run for the first time:

```bash
make prepare-local-dev
```

Then you could run linters, tests and prettify code:

```bash
make pretty
make lint
make run-test
```

To run server locally run:

```bash
make run
```

To build/run tests in docker you could run:

```bash
make docker-build-test
make docker-lint
make docker-run-test
```

To build/run service in docker you could run:

```bash
make docker-build
make docker-run
```

**API:**

The application has single endpoint `/intersection-over-union`, you could use swagger 
at `http://0.0.0.0:8000/` or curl:

```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/intersection-over-union' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "predicted": {
    "left": 4.5,
    "top": 3,
    "right": 11.5,
    "bottom": 10
  },
  "ground_truth": {
    "left": 8.5,
    "top": 7,
    "right": 14.5,
    "bottom": 13
  }
}'
```
Response:
```json
{
  "iou": 0.118
}
```

In case of incorrect values will be provided in the content(incorrect field names of left > right) `422` error will be returned

You could configure number of decimal digits in `DECIMAL_DIGITS` env in `docker-compose.yaml`. 
Also you could configure some gunicorn options from `gunicorn_config.py`

## TODOs

#### 1. Probably use poetry instead of pip

#### 2. To set up CI/CD you should:

1. add docker pushing and tagging functionality to `Makefile`
2. then you could write CI pipeline to execute sequentially(for example in Gitlab CI you could use docker-in-docker) the following steps:

```bash
make docker-build-test
make docker-lint
make docker-run-test
```

If previous steps are successful, you should execute:
```bash
make docker-build
and tag using something like commit id or version number
make docker-push
```

Then if you deploy to kubernetes, then you could write pipelines to deploy to staging/prod environments. 
These pipelines should create all needed resources in kubernetes(or update docker tag in deployment which you get in previous step):
deployments, ingresses, secrets, etc.

