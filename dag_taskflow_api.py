#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:46:52 2022

@author: bixbypeterson
"""

from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner' : 'bixby',
    'retries' : 0,
    'retry_delay' : timedelta(minutes=2)}

@dag(dag_id='dag_with_taskflow_api', default_args=default_args, 
     start_date=datetime(2022,7,20), 
     schedule_interval='@daily')

def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {'firstname':'Dumb', 'lastname':'Ass'}
    
    @task()
    def get_age():
        return 100
    
    @task()
    def greet(firstname,lastname,age):
        print(f"Hello {firstname} {lastname} for {age}th Time!")
        
    name_dict = get_name()
    age = get_age()
    greet(firstname=name_dict['firstname'], lastname=name_dict['lastname'], age=age)
    
greet_dag = hello_world_etl()