from airflow import DAG
from airflow.decorators import task
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta

from docker.types import Mount
from airflow.providers.docker.operators.docker import DockerOperator


default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2024, 1, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="parse_games", start_date=datetime(2022, 1, 1), schedule=None) as dag:
    
    task_a = DockerOperator (
        task_id="parse_slippi_files",
        image="/containers/slippi_parser/Dockerfile",
        command='python3 slippi_parser.py',
        docker_url='tcp://docker-proxy:2375',
        network_mode='host',
        mounts=[
            Mount(
                source='/tmp/keys/keys.json',
                target='/tmp/keys/keys.json',
                type='bind'
            )
        ]
    )