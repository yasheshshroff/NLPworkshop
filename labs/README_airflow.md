# Setting up Airflow on AWS

```shell
# 1. set the environment (portability) in ~/.bashrc
export AIRFLOW_HOME=/home/ubuntu/airflow

# 2. activate the ML environment
source activate pytorch_p36

# 3. install airflow
pip install apache-airflow

# 4. initialize the database
airflow db init

# 5. create a new user
airflow users create --username admin --firstname Warren --lastname Buffet --role Admin --email nowhere@here.com

# password: a1rfl0w

# 6. get the config file
wget https://raw.githubusercontent.com/yasheshshroff/NLPworkshop/main/labs/airflow.cfg

# 7. create the dags folder
mkdir dags

wget https://raw.githubusercontent.com/yasheshshroff/NLPworkshop/main/labs/ml_pipeline.py -O dags/ml_pipeline.py

# 8. Start the scheduler
airflow scheduler

# 9. Start the webserver in a different terminal
source activate pytorch_p36
airflow webserver
```



## Running Airflow

* Go to the ec2 public IP address <ec2.compute>:8080
* Start the DAG tasks





