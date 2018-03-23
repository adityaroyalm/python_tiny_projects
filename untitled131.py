# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:34:45 2018

@author: aditya royal
"""

import openpyxl
import pandas as pd 
book=openpyxl.load_workbook('final_freelancer.xlsx')
sheet=book.active
#df=pd.DataFrame(sheet.values)
li=list()
for index,row in df.iloc[1:10,:].iterrows():
    print(row)