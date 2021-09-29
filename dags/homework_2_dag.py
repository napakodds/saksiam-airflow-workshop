import logging

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


def _say_hello():
    logging.info("Hello, SAKSIAM!")

def print_log_messages():
    logging.info("Hello, NANNAN!")

default_args = {
    "owner": "Napak Paweechainapa",
    "start_date": timezone.datetime(2021, 9, 29)
}
with DAG(
    "homework_2_dag",
    schedule_interval="*/30 * * * *",
    default_args=default_args,
    catchup=False,
    tags=["saksiam"],
)as dag:

    start = DummyOperator(task_id="start")

    echo_hello = BashOperator(
        task_id="echo_hello",
        bash_command="echo 'hello'",
    )

    say_hello = PythonOperator(
        task_id="say_hello",
        python_callable=_say_hello,
    )

    print_log_messages = PythonOperator(
        task_id="print_log_messages",
        python_callable=print_log_messages,
    )

    end = DummyOperator(task_id="end")

   
    [start >> echo_hello >> say_hello >> print_log_messages >> end]