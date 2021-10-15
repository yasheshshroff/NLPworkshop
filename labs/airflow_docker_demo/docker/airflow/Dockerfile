# Base Image
FROM puckel/docker-airflow

# install the needed packages including java and a perl library which we
# need for fastqc

ENV AIRFLOW_HOME=/usr/local/airflow
WORKDIR $AIRFLOW_HOME
COPY ./start-airflow.sh $AIRFLOW_HOME/start-airflow.sh
COPY ./airflow.cfg $AIRFLOW_HOME/airflow.cfg
USER root
RUN apt-get update -y && apt-get install -y\
 wget \
 unzip \
 python3-pip
RUN pip3 install sklearn
RUN chmod +x $AIRFLOW_HOME/start-airflow.sh
RUN chown -R airflow:airflow $AIRFLOW_HOME
USER airflow
CMD [ "./start-airflow.sh" ]
