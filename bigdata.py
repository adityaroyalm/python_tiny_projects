# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:02:32 2018

@author: aditya royal
"""

import pandas as pd
import numpy as np
import sklearn.linear_model as lm
import seaborn as sns
from sklearn.metrics import r2_score
df=pd.read_csv('C:/Users/aditya royal/task2output2.txt',sep='\t')
#My column names are in 3rd row .Remove this part if you are having them at perfect location 
df.columns=df.iloc[2,:]
df=df.drop(df.index[2])
######  max vs year
#converting to float
df=df.astype(float)
lrg=lm.LinearRegression()
x_train=np.array(df[['YEAR']],dtype=float)
y_train=np.array(df[['MAX']],dtype=float)
#fitting a linear regression
lrg.fit(x_train,y_train)
#predicting 
y_pred=lrg.predict(x_train)
print(r2_score(y_train,y_pred))
#coefficient of linear regression
coeff1=lrg.coef_
#intercept of linear regression
intercept1=lrg.intercept_
#plot
sns.lmplot(x='YEAR',y='MAX',data=df)
########  min vs year
lrg=lm.LinearRegression()
x_train=np.array(df[['YEAR']],dtype=float)
y_train=np.array(df[['MIN']],dtype=float)
#fitting linear regression
lrg.fit(x_train,y_train)
#predicting linear regression
y_pred=lrg.predict(x_train)
print(r2_score(y_train,y_pred))
#coefficient of linear regression
coeff2=lrg.coef_
#intercept
intercept2=lrg.intercept_
#plot
sns.lmplot(x='YEAR',y='MIN',data=df)
########## mean vs year
lrg=lm.LinearRegression()
x_train=np.array(df[['YEAR']],dtype=float)
y_train=np.array(df[['MEAN']],dtype=float)
lrg.fit(x_train,y_train)
y_pred=lrg.predict(x_train)
print(r2_score(y_train,y_pred))
coeff3=lrg.coef_
intercept3=lrg.intercept_
sns.lmplot(x='YEAR',y='MEAN',data=df)
########## meadian vs year
lrg=lm.LinearRegression()
x_train=np.array(df[['YEAR']],dtype=float)
y_train=np.array(df[['MEDIAN']],dtype=float)
lrg.fit(x_train,y_train)
y_pred=lrg.predict(x_train)
print(r2_score(y_train,y_pred))
coeff4=lrg.coef_
intercept4=lrg.intercept_
sns.lmplot(x='YEAR',y='MEDIAN',data=df)
