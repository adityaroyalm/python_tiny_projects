# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 07:55:00 2017

@author: aditya royal
"""
import mysql.connector
from mysql.connector import errorcode
db_name='products'
tables={}
tables['products']= (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")
cnx=mysql.connector.connect(user='root',password='Root1@#')
cursor=cnx.cursor()
def create_database(cursor):
    try:
        cursor.execute(
                "create database {} default character set 'utf-8'".format(DB_NAME))
        