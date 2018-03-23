# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:12:58 2017

@author: aditya royal
"""
import pandas as pd
import numpy as np
a=np.arange(-30,30)
df=pd.DataFrame()
df['s']=np.exp(a)
np.random.seed(2)
df['ss']=a*a
print df['ss'].corr(df['s'])