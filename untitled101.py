# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 18:28:22 2017

@author: aditya royal
"""

from mysql.connector import errorcode
import mysql.connector
cnx=mysql.connector.connect(user='root',password='Root1@#')
cnx.close()
try:
    mysql.connector.connect(user='root',password='Root1@#')
except mysql.connector.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong with your username or password")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print ("databse doesn't exist")
    else:
        print(err)

        