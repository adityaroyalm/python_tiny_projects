# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:24:39 2017

@author: aditya royal
"""

import pandas as pd
import numpy as np
#load data
automobile=pd.read_csv('C:/Users/aditya royal/Desktop/Automobile_data.csv')
# see a sample of data
print automobile.head()
# find the type of data
print automobile.dtypes
#counting number of '?'
total=automobile.isin(['?']).apply(sum)
# Removing unsopported data type
for column in (automobile):
    automobile.loc[automobile.loc[:,column].isin(['?']),column]=np.nan
#replacing nan values with average values of the coulmn
int_columns=automobile.dtypes.isin([int,float])
#column names
cols=automobile.columns
#changing dtype of columns
try:
    automobile.apply(lambda x:x.to_numeric(errors='coerce'))
except ValueError:
    pass
#finding only integer,float columns
int_cols=cols[int_columns]
for column in (int_cols):
    automobile.loc[automobile.loc[:,column].isnull(),column]=0

#automobile['stroke'] = pd.to_numeric(automobile['stroke'], errors='coerce')
