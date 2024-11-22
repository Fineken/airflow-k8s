from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

dag = DAG(
    'test_dag',
    default_args=default_args,
    description='Тестируем git-sync',
    schedule_interval=None,
    start_date=datetime(2023, 11, 15),
    catchup=False
)

hello_world_task = BashOperator(
    task_id='hello_world_task',
    bash_command='echo Hello world!',
    dag=dag
)

hello_world_task