# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:16:05 2018

@author: aditya royal
"""
import pandas as pd
import numpy as np
index = pd.date_range('10/1/1999', periods=1100)
ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
ts = ts.rolling(window=100,min_periods=100).mean().dropna()
grouped=ts.groupby(lambda x:x.month).transform(lambda x: ( x.mean()) / x.std()
)
df = pd.read_csv(
   "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
   )
#df.groupby('day').filter(lambda x : print(type(x)))
#k=df.groupby('day').transform(lambda x: (type(x)))
#df=df.drop(df.columns[[1,3,4,5]],axis=1)
#k=df.groupby('sex').filter(lambda x: x.mean()>20)
