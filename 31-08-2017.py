# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:05:12 2017

@author: aditya royal
"""
import pandas as pd
csv_obj=pd.read_csv("C:/Users/aditya royal/Desktop/abalone.csv",header=None)
#from metrics import rsquare
from sklearn.metrics import r2_score
from sklearn import linear_model
lr=linear_model.LinearRegression()
#creating dummy variables for female and male
csv_obj.ix[csv_obj.iloc[:,0]=='M',0]=1
csv_obj.ix[csv_obj.iloc[:,0]=='F',0]=0
import numpy as np
#summary like in r
ded=csv_obj.describe()
#replacing unusual values with nan
csv_obj.ix[csv_obj.iloc[:,0]=='I',0]=np.nan
# can fill whole dataframe with forward or backward fill
csv_obj.iloc[:,0].fillna(method='ffill',inplace=True)
#summary like r
ded=csv_obj.iloc[:,0].describe()
#train_test_split will be a lot easier
train,validate,test=np.split(csv_obj.sample(frac=1),[int(0.4*len(csv_obj)),int(0.7*len(csv_obj))])
#fit the model
lr.fit(train.iloc[:,:8],train.iloc[:,8])
#predict the model
result1=lr.predict(validate.iloc[:,:8]).astype(int)
print(r2_score(validate.iloc[:,8].as_matrix(),result1))
#k=validate[:,8]
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#csv_obj.iloc[0].mean
#plotting histogram
import matplotlib.pyplot as plt 
#histogram has only one axis so its wrong
#plt.hist(csv_obj.ix[csv_obj.iloc[:,0]==1,:],csv_obj.ix[csv_obj.iloc[:,0]==0,:],stacked=True,bins=1000)
k=0
csv_obj.ix[csv_obj.iloc[:,0]==1,1:8].hist()
csv_obj.ix[csv_obj.iloc[:,0]==0,1:8].hist()       
csv_obj.iloc[:,1:8].hist()
