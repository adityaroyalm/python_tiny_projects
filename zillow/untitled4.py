# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 16:14:36 2017

@author: aditya royal
"""
from numpy import nan
from pandas import *
dicti={'num':Series([1,2,np.nan,4],index=[1,2,3,4]),'alph':Series(['a','b','c','d'],index=[1,2,3,4])}
##different way to create dictionaries #
df=DataFrame(dicti)
#for c in  df.dtypes[df.dtypes=='object'].index.values:
 #   df[c]=True
#print df.columns[0,1]
import numpy as np
pri= np.ndarray((3,3),dtype=int)
print pri[[1,1]]
