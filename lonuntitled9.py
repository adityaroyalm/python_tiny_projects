# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 17:58:31 2017

@author: aditya royal
"""

from sklearn.svm import SVC
import numpy as np
import pandas as pd
from StringIO import StringIO
import csv
#train=pd.read_csv('C:/Users/aditya royal/Desktop/MLsoftaware_projects/titanic/train.csv')
#train = train.drop(['Survived'], axis=1)
#x_train = np.array(train)
#titanic=np.genfromtxt('C:/Users/aditya royal/Desktop/MLsoftaware_projects/titanic/train.csv',skip_header=1,delimiter=',',dtype=None)
csv_open=open('C:/Users/aditya royal/Desktop/MLsoftaware_projects/titanic/train.csv','rb')
csv_obj=csv.reader(csv_open)
csv_obj.next()
data=[]
for row in csv_obj:
    data.append(row)
data=np.array(data)   
survived=data[:,1].astype(int)
x=data[:,5:8].astype(int)
#from sklearn.svm import SVC
#svc=SVC(kernel='linear')
from sklearn.model_selection import cross_val_score
#svc= svc.fit(x,survived)
import xgboost as xgb
dtrain=xgb.DMatrix(csv_obj)
dtest=xgb.DMatrix(csv_obj)
params = {"max_depth":2, "eta":0.1}
model = xgb.cv(params, dtrain,  num_boost_round=500, early_stopping_rounds=100)
