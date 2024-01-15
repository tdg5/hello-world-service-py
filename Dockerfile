FROM python:3.12.1-bullseye

ARG HELLO_WORLD_API_PY_GIT_REF
ARG HELLO_WORLD_API_PY_VERSION

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m venv /venv && source /venv/bin/activate

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./hello_world_api_py /app/hello_world_api_py

ENV PYTHONPATH=/app

ENTRYPOINT ["python"]

CMD ["-m", "hello_world_api_py.entry"]
