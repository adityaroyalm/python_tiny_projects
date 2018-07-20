# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:40:44 2018

@author: aditya royal
"""

import pandas as pd
#reading excel files
df=pd.read_excel('C:/Users/aditya royal/Downloads/MortgageDefaulters.xlsx',sheetname=1)
df=df.drop(['First_home','OUTCOME','State'],axis=1)
maxk=df-pd.DataFrame(df.max())