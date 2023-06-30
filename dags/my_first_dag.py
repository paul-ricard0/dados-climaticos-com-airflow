from airflow.models import DAG
from airflow.utils.dates import days_ago # Para usar dias anteriores 


# Operators, são classes no Airflow com várias funções já pronto
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator

with DAG(
    'my_first_dag',
    start_date=days_ago(2), # Iniciou 2 dia atrás 
    schedule_interval='@daily' # Executa todo dia 00:00
) as dag:
    
    tarefa_01 = EmptyOperator(task_id = 'task_01')
    tarefa_02 = EmptyOperator(task_id = 'task_02')
    tarefa_03 = EmptyOperator(task_id = 'task_03')

    tarefa_04 = BashOperator(task_id = 'cria_pasta',         
                    bash_command='mkdir -p "/mnt/c/Users/paulo/Documents/Cursos/Alura/Airflow/test={{data_interval_end.strftime("%Y-%m-%d")}}" ')
    
    tarefa_01 >> [tarefa_02, tarefa_03]
    tarefa_03 >> tarefa_04