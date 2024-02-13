#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:28:53 2022

@author: bixbypeterson
"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner' : 'bixby',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)}

with DAG( dag_id = 'my_first_dag_v3',
         description = 'This is the first DAG I ever wrote',
         default_args = default_args,
         start_date = datetime(2022, 7, 20, 2),
         schedule_interval = '@daily'
         ) as dag:
    task1 = BashOperator(
        task_id = 'task_1',
        bash_command = 'echo hello world')
    
    task2 = BashOperator(
        task_id = 'task_2',
        bash_command = 'echo Task 2 running after Task 1')
    
    task3 = BashOperator(
        task_id = 'task_3',
        bash_command = 'echo Task 3 running after Task 1 and at the same time as Task2')
    
    task4 = BashOperator(
        task_id = 'task_4',
        bash_command = 'echo Task 4 running after Task 2 and Task 3 complete')
    
    task1 >> [task2,task3] >> task4