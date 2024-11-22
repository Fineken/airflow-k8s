# Start Generation Here
FROM apache/airflow:2.5.0

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./dags /usr/local/airflow/dags

RUN chown -R airflow:airflow /usr/local/airflow/dags

USER airflow

CMD ["airflow", "webserver"]
