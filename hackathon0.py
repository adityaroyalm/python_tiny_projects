# -*- coding: utf-8 -*-
"""
Created on Mon May 01 11:31:27 2017

@author: aditya royal
"""
import pandas as pd
data=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\Day7\student.csv')
data=data[['age','studytime']]
X=data['age']
import numpy as np
random_state = np.random.RandomState(0)
from sklearn.model_selection import train_test_split
y=data['studytime']
X_train,y_train,X_test,y_test=train_test_split(X,y,random_state=0)
from sklearn import svm
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
classifier=OneVsRestClassifier(svm.SVC(kernel='linear',probability=True,random_state=random_state))
y_test=label_binarize(y_test,classes=[1,2,3,4])
X_test=label_binarize(X_test,classes=[1,2,3,4])
X_train=X_train.reshape((296,1))
X=X.reshape((395,1))
y_train=y_train.reshape((99,1))
Y=classifier.fit(X_train,X_test).decision_function(y_train)
Y=classifier.predict_proba(X_train)
pred = classifier.predict_proba(X)
from sklearn.linear_model import LinearRegression
