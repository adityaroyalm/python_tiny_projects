# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:40:44 2018

@author: aditya royal
"""

import pandas as pd
df=pd.read_excel('C:/Users/aditya royal/Downloads/MortgageDefaulters.xlsx',sheetname=1)
df=pd.get_dummies(df,columns=['OUTCOME'],drop_first=True)
#df.drop('OUTCOME',inplace=True,axis=1)
df.loc[:,'OUTCOME_non-default']=[0 if x==1 else 1 for x in df.loc[:,'OUTCOME_non-default']]
df.drop('State',axis=1,inplace=True)
tyeper=df.dtypes
df=pd.get_dummies(df,columns=df.loc[:,df.dtypes==object],drop_first=True)
df_train=df.sample(int(0.6*len(df.index)),axis=0)
import statsmodels.api as sm
model=sm.Logit(df_train.loc[:,'OUTCOME_non-default'],df_train.loc[:,df.columns!='OUTCOME_non-default'])
from sklearn.feature_selection import chi2
