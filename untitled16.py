# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 09:39:04 2017

@author: aditya royal
"""

import csv
with open(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects\titanic\train.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    for ro in reader:
        print(ro['Survived'])