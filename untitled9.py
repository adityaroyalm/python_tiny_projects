# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:24:50 2017

@author: aditya royal
"""
import numpy as np
import pandas as pd
csv_obj=pd.read_table("C:/Users/aditya royal/Downloads/fsz.txt")
print csv_obj.describe()
print csv_obj.dtypes
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
k=pd.DataFrame()
for x in csv_obj:
    if csv_obj.loc[:,x].dtype!=np.int64:
        k.loc[:,x]=le.fit_transform(csv_obj.loc[:,x])       
