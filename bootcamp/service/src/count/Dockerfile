ARG APP_IMAGE=python:3
FROM $APP_IMAGE as base

FROM base as builder
WORKDIR /app
RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir -U pip setuptools
COPY requirements.txt .
RUN .venv/bin/pip install -r requirements.txt --no-cache-dir -r requirements.txt && .venv/bin/splunk-py-trace-bootstrap

FROM base
WORKDIR /app
COPY --from=builder /app /app
COPY app.py .

ENV PATH="/app/.venv/bin:$PATH"
CMD [ "splunk-py-trace", "flask", "run", "--host", "0.0.0.0"]
