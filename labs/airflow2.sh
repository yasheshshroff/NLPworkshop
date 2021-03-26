echo "export AIRFLOW_HOME=/home/ubuntu/airflow" >> ~/.bashrc
echo "source activate pytorch_p36" >> ~/.bashrc

# 3. install airflow
pip install apache-airflow

# 4. initialize the database
airflow db init

# 5. create a new user
airflow users create --username admin --firstname Warren --lastname Buffet --role Admin --email nowhere@here.com

# password: a1rfl0w

# 6. get the config file
cd airflow
wget https://raw.githubusercontent.com/yasheshshroff/NLPworkshop/main/labs/airflow.cfg -O airflow.cfg

# 7. create the dags folder
mkdir dags

wget https://raw.githubusercontent.com/yasheshshroff/NLPworkshop/main/labs/ml_pipeline.py -O dags/ml_pipeline.py

airflow webserver &> /dev/null
airflow scheduler 

