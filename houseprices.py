# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:47:29 2017

@author: aditya royal
"""
from ggplot import *
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/aditya royal/Desktop/MLsoftaware_projects/house prices/train (3).csv')
del df['Id']
df1=df[['MSSubClass','Street']]
grouped=df1.groupby(['Street'])
#print ggplot(df,aes('MSSubClass','SalePrice',color='SaleCondition'))+geom_line()+facet_wrap('OverallQual')
#for column in df.columns:
   # if type(df[[column]]) is int:
df[['MSSubClass']].astype(int)
print type(df[['MSSubClass']]) is int