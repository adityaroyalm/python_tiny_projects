# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:28:22 2017

@author: aditya royal
"""
iris=datasets.load_iris()
X=iris.data
y=iris.target
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm
from sklearn.preprocessing import label_binarize
from sklearn.model_selection import train_test_split
y = label_binarize(y, classes=[0, 1, 2])
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
classifier=OneVsRestClassifier(svm.SVC(kernel='linear',probability=True,random_state=random_state))
scoe=classifier.fit(X_train,y_train).decision_function(X_test)
