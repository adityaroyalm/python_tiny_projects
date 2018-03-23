# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 17:16:47 2017

@author: aditya royal
"""
import pandas as pd

df=pd.DataFrame({'A':[1,2,2,3,4,5,5,5,0,6,7,7]})
for x in range(len(df.loc[:,'A'])-1):
    if df.loc[x,'A']==df.loc[x+1,'A']:
        print x
k=[]
for element in df.loc[:,'A']:
    kk=element-(df.loc[:,'A']).mean()
    k.append(kk)
print df.loc[:,'A'].mean()
print df.idxmin()
(df.isnull().cumsum(axis=1)==3).idxmax(axis=1)