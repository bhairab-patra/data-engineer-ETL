 
import sys
sys.path.insert(0, r'C:\JAVA_MS_2027\DATA_ENG\COMP_ETL')
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator
from etl.extract import extract_employees
from etl.tranform import transform_employees
from etl.load import load_to_warehouse



def run_extract(**context):
    df = extract_employees()
    # XCom se agle task ko data pass karo
    context['ti'].xcom_push(key='raw_data', value=df.to_json())

def run_transform(**context):
    import pandas as pd
    raw_json = context['ti'].xcom_pull(key='raw_data')
    df_raw   = pd.read_json(raw_json)
    df_clean = transform_employees(df_raw)
    context['ti'].xcom_push(key='clean_data', value=df_clean.to_json())

def run_load(**context):
    import pandas as pd
    clean_json = context['ti'].xcom_pull(key='clean_data')
    df_clean   = pd.read_json(clean_json)
    load_to_warehouse(df_clean)

default_args = {
    "owner": "data_team",
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}


with DAG(
    dag_id ="employee_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule ="0 1 * * *",  # ← raat 1AM daily
    catchup=False,  # purane missed runs skip karo
    tags=["etl", "employees"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_employees",
        python_callable=run_extract,
    )
    transform_task = PythonOperator(
        task_id         = 'transform_employees',
        python_callable = run_transform,
    )
    load_task = PythonOperator(
        task_id         = 'load_to_warehouse',
        python_callable = run_load,
    )
    
    extract_task >> transform_task >> load_task
    
