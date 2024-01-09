FROM python:3.10-slim

RUN pip install \
    dagster==1.5.14 \
    dagster-postgres \
    dagster-k8s \
    dagster-celery[flower,redis,kubernetes] \
    dagster-celery-k8s

# Get example pipelines
COPY dagster_project/ /