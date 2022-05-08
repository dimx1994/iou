FROM python:3.9 as base

FROM base as prod

COPY requirements.txt /iou/
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r /iou/requirements.txt

COPY app /iou/app

WORKDIR /iou
ENV PYTHONPATH="${PYTHONPATH}:/iou"

CMD ["gunicorn", "--config", "app/gunicorn_config.py", "app.server:app"]


FROM base as test

COPY requirements-dev.txt /iou/
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r /iou/requirements-dev.txt

COPY app /iou/app

COPY Makefile /iou/
COPY setup.cfg /iou/
COPY tests /iou/tests

WORKDIR /iou
ENV PYTHONPATH="${PYTHONPATH}:/iou"

CMD [""]