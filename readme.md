# Dados climaticos com Airflow 

Descrição do projeto e sua finalidade.

## Requisitos

- Python 3.9
- Chave da API do Visual Crossing: [https://www.visualcrossing.com/weather-api](https://www.visualcrossing.com/weather-api)

## Instalação

1. Clone este repositório.
2. Navegue até o diretório do projeto.
3. Execute o seguinte comando para instalar o Apache Airflow e suas dependências:

`pip install 'apache-airflow==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"`

4. Instale o pandas

`pip install pandas`

5. Defina a variável de ambiente `AIRFLOW_HOME` apontando para o diretório do Airflow. Por exemplo:

`export AIRFLOW_HOME=~/Documents/airflow`
ou
`export AIRFLOW_HOME=$(pwd)`

## Scripts

1. As dags/scripts desenvolvidas estão na pasta Dags
2. Adicione sua Key no arquivo dags\dados_climaticos.py dentro na função extrair dados
3. Altere o caminho que você quer que salve os arquivo nas variaveis file_path dentro da def extrai_dados
4. Altere o path no command dentro de tarefa_1
5. Em with DAG() altere o start_date para a data de inicio que deseja. A atual é 01/06/2023

## Uso

1. Inicie o Airflow executando o seguinte comando:

`airflow standalone`

2. O Airflow estará sendo executado na porta localhost:8080.
3. Acesse [http://localhost:8080](http://localhost:8080) para usar o Airflow e gerenciar suas tarefas.
4. Usuário será admin e a senha se encontra no arquivo `standalone_admin_password.txt`
5. Executar a Dag dados_climaticos