from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
from pendulum import datetime
from scripts import logs

default_args = {
    "retries": 2,
    "retry_delay": timedelta(seconds=300),
}

with DAG(
    dag_id="api_to_kafka",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    start_date=datetime(2026, 4, 15, tz="UTC"),
    schedule_interval="@daily",
) as dag:

    task_generator = PythonOperator(
        task_id="log_generator",
        python_callable=logs.generate_log,
    )

    task_ingestion = PythonOperator(
        task_id="log_ingestion",
        python_callable=logs.ingestion,
    )

    task_features = PythonOperator(
        task_id="log_features",
        python_callable=logs.features,
    )

    task_generator >> task_ingestion >> task_features