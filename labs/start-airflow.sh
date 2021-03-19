#!/usr/bin/env bash

# Move to the AIRFLOW HOME directory
cd $AIRFLOW_HOME

# Initiliase the metadatabase
airflow db init
exec airflow webserver  &> /dev/null &

exec airflow scheduler
