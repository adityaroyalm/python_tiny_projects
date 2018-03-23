# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 10:48:51 2017

@author: aditya royal
"""

from sklearn import LabelEncoder
from sklearn import OneHotEncoder
labelencoder=LabelEncoder()

for i in range(len()):
    features=labelencoder.fit(labels[i])
    features=features.predict[datset[i]]
    onehotencoder=OHE()
    onehotencoder.fit_transform(features)
    cats.append(features)
encoded_cats=numpy.column_stack(cats)