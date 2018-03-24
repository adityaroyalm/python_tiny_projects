# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 15:28:58 2017

@author: aditya royal
"""

import pandas as pd
dataset=pd.read_csv("D:/MLsoftaware_projects/allstate claim seveirity/train.csv")
dataset_test=pd.read_csv("D:/MLsoftaware_projects/allstate claim seveirity/test.csv")
ID=dataset_test['id']
dataset_test.drop('id',axis=1,inplace=True)
dataset_test.shape
dataset=dataset.iloc[:,1:]
print(dataset.describe())
dataset.skew()
import numpy
import seaborn as sns
import matplotlib.pyplot as plt
dataa=dataset.iloc[:,116:]
cols=dataa.columns
print(cols)
import matplotlib.pyplot as plt
import seaborn as sns
n_cols=2
#plotting multiple seaborn plots
for i in range(7):
    fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(6,6))
    for j in range(2):
        sns.violinplot(y=cols[i*n_cols+j],data=dataa)
plt.show()
import numpy as np
dataset['loss']=np.log1p(dataset['loss'])
sns.violinplot(data=dataset,y='loss')
#data_corr=data.corr()
x=29
for i in range(x):
    fig,ax=plt.subplots(figsize=(6,6),nrows=1,ncols=4)
    for j in range(4):
        sns.countplot(data=dataset,x=dataset.columns[i*4+j],ax=ax[j])
labels=[]
cols=dataset.columns
for i in range(0,116):
    train=dataset[cols[i]].unique()
    test=dataset_test[cols[i]].unique()
    labels.append(list(set(train)|set(test)))   
cats=[]
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
for i in range(0,116):
    #label encoder is useless
    label_encoder=LabelEncoder()
    label_encoder.fit(labels[i])
    feature=label_encoder.transform(dataset.iloc[:,i])
    feature=feature.reshape(dataset.shape[0],1)
    #pd.dummy is better than onehtencoder
    onehotencoder=OneHotEncoder(sparse=False,n_values=len(labels[i]))
    feature=onehotencoder.fit_transform(feature)
    cats.append(feature)
encoded_cats=np.column_stack(cats)
import numpy as np
print(encoded_cats.shape)
r,c=dataset_encoded.shape()
#for i in range(0,split):
    
    