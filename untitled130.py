# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:40:58 2018

@author: aditya royal
"""


import pandas as pd
obj=pd.ExcelFile('data_random.xlsx')
df=obj.parse('Sheet1')
df
