FROM python:3.12.1-bullseye

ARG HELLO_WORLD_SERVICE_GIT_REF
ARG HELLO_WORLD_SERVICE_VERSION

ENV SETUPTOOLS_SCM_PRETEND_VERSION_FOR_HELLO_WORLD_SERVICE="$HELLO_WORLD_SERVICE_VERSION"

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m venv /venv && source /venv/bin/activate

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./hello_world_service /app/hello_world_service

ENV PYTHONPATH=/app

ENTRYPOINT ["python"]

CMD ["-m", "hello_world_service.main"]
