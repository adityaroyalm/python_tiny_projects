# -*- coding: utf-8 -*-
"""
Created on Tue May 02 07:57:36 2017

@author: aditya royal
"""

import numpy as np
import pandas as pd
data=pd.read_csv(r'C:/Users/aditya royal/Desktop/winequality.csv')
from sklearn.linear_model import LogisticRegression
logReg=LogisticRegression()

X = data.drop(['ID', 'quality'], axis=1)
X.fillna(X.mean(),inplace=True)
y = data.quality
y[y==2]=0
logReg.fit(X, y)
pred=logReg.predict(X)
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import log_loss
y=y.reshape((4898,1))
k2=accuracy_score(y,pred)
k3=f1_score(y,pred)
pred_prob = logReg.predict_proba(X)
k4=log_loss(y,pred_prob[:,0])