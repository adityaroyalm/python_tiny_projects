# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 19:31:54 2017

@author: aditya royal
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
dataset=pd.read_csv("D:/MLsoftaware_projects/allstate claim seveirity/train.csv")
import numpy as np
vals=np.zeros(dataset[:,116].shape)
le=LabelEncoder()
for i in range(116):
    vals[:,i]=le.fit_transform(dataset.iloc[:,i].as_matrix())
print np.unique(vals[:,131])
O=OneHotEncoder()
O.fit_transform(vals)