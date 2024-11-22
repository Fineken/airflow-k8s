from airflow.plugins_manager import AirflowPlugin
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def my_custom_function():
    print("Hello from my custom function!")

class MyCustomOperator(DummyOperator):
    def execute(self, context):
        super().execute(context)
        my_custom_function()

class MyPlugin(AirflowPlugin):
    name = "my_custom_plugin"
    operators = [MyCustomOperator, PythonOperator]

