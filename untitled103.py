# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 23:10:30 2017

@author: aditya royal
"""
from __future__ import print_function
import mysql.connector
from datetime import date
cnx=mysql.connector.connect(user='root',password='Root1@#',database='test')
cursor=cnx.cursor()
add_employee=("INSERT INTO EMPLOYEES "
              "(first_name,last_name,hire_date,gender,birth_date,death_date)"
              "VALUES(%s,%s,%s,%s,%s)")
add_salary=("INSERT INTO salaries" 
            "(emp_no,salary,from_Date,to_date))"
            "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
data_employee=('geert','vanderkelen','tomorrow','M',date(1977,6,14))
cursor.execute(add_employee,data_employee)

    
