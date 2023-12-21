# creating the import Blocs 
from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Creating the DAG Arguments block
default_args = {
    'owner': 'yassine ouazzani',
    'start_date': days_ago(0),
    'email': ['yassineouazzanii@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# creating the DAG definition block. The DAG will run daily.
ETL_server_dag = DAG(
    dag_id='ETL_Server_Access_Log_Processing',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1),
)
#Creating the download task
Download = BashOperator(
    task_id = 'Download_Task',
    bash_command = 'wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt "',
    dag = ETL_server_dag,

)

#Creating the extract task : Extract the fields timestamp and visitorid to a new file named extracted.txt.

Extract = BashOperator(
    task_id = 'Extract_Task',
    bash_command ='cut -d "#" -f1,4 web-server-access-log.txt > /home/project/airflow/dags/extracted.txt',
    dag = ETL_server_dag,

)

#Creating the Transform task : this task capitalize all charachters of vsitorId Fields
Transfom = BashOperator(
    task_id = "Transfom_Task",
    bash_command ='tr "[a-z]" "[A-Z]" < /home/project/airflow/dags/extracted.txt > /home/project/airflow/dags/capitalized.txt',
    dag = ETL_server_dag,

)

 #Creating the Load task : this task compress the extracted and transformed data
Load = BashOperator(
    task_id = "Load_Task",
    bash_command ='zip log.zip capitalized.txt',
    dag = ETL_server_dag,

)

Download >> Extract >> Transfom >> Load



