# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 09:04:36 2017

@author: aditya royal
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
data=pd.read_csv(r'C:/Users/aditya royal/desktop/winequality.csv')
logreg=LogisticRegression()
print data.head()
data.loc[(data.quality==2),'quality']=0
X=data[['fixed acidity','volatile acidity']]
y=data.quality
logreg.fit(X,y)
pred=logreg.predict(X)
from sklearn.metrics import confusion_matrix
C=confusion_matrix(y,pred)
pd.DataFrame(C,index=['Predicted:0','Predicted:1']  ,columns=['Actual:0','Actual:1'])
#from plot_matrix import show_confusion_matrix
#show_confusion_matrix(C)
from sklearn.metrics import roc_auc_score
pre=logreg.predict_proba(X)
roc_auc_score(y,pred[:,1],)

