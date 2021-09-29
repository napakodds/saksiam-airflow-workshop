import logging

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator


def _say_hello():
    logging.info("Hello, SAKSIAM!")


default_args = {
    "owner": "Napak Paweechainapa",
    "start_date": timezone.datetime(2021, 9, 29)
}
with DAG(
    "homework_1_dag",
    schedule_interval="*/10 * * * *",
    default_args=default_args,
    catchup=False,
    tags=["saksiam"],
)as dag:

    one = DummyOperator(task_id="1")
    two = DummyOperator(task_id="2")
    three = DummyOperator(task_id="3")
    four = DummyOperator(task_id="4")
    five = DummyOperator(task_id="5")
    six = DummyOperator(task_id="6")
    seven = DummyOperator(task_id="7")
    eight = DummyOperator(task_id="8")
    end = DummyOperator(task_id="9")

    one >> [two, five] 
    two >> [three, six]
    five >> [six, seven]
    three >> four >> end
    six >> eight
    seven >> eight
    eight >> end