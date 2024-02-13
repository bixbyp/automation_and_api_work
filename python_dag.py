#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:46:29 2022

@author: bixbypeterson
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

"""
XCOM can only handle 43 kb of data
Schedule Interval
    Accepts:
        datetime.timedelta
        CRON Expression:crontab.guru
            String of 5 fields seperated by a space
            minute hour day_of_month month_number day_of_week
            * = any value
            , = value list seperator
            - = range of values
            / = step values
            OR
            Presets:
                preset:  cron equivalant:
                None     used for externally triggered DAGs
                @once
                @hourly  0 * * * *
                @daily   0 0 * * *
                @weekly  0 0 * * 0
                @monthly 0 0 1 * *
                @yearly  0 0 1 1 *
"""

default_args = {
    'owner' : 'bixby',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)}


def hello_world(age, ti):
    first_name = ti.xcom_pull(task_ids='Python_Get_Name', key='first_name')
    last_name = ti.xcom_pull(task_ids='Python_Get_Name', key='last_name')
    print(f'Hello World, I am {first_name} {last_name} and this is my first python DAG at {age}')

def get_name(ti):
    ti.xcom_push(key='first_name', value='Bixby')
    ti.xcom_push(key='last_name', value='Peterson')

with DAG(
        default_args = default_args,
        dag_id = 'DAG_using_Python_with_XCOM',
        description = 'First DAG using Python',
        start_date = datetime(2022,7,19),
        schedule_interval = '@daily'
        ) as dag:
    
    task1 = PythonOperator(
        task_id = 'Python_Hello',
        python_callable= hello_world,
        op_kwargs = {'age' : 100 }
        )
    
    task2 = PythonOperator(
        task_id = 'Python_Get_Name',
        python_callable = get_name
        )
    
    task2 >> task1