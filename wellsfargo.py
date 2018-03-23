# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:12:12 2017

@author: aditya royal
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
obj=pd.read_excel("C:/Users/aditya royal/Downloads/Book12.xlsx")
a=['age','tenure_altered','check_bal_altered','sav_bal_altered','branch_visit_cnt','phone_banker_cnt','mobile_bank_cnt','online_bank_cnt','direct_mail_cnt','direct_email_cnt','direct_phone_cnt']
obj2=obj.pivot_table(index=['masked_id'],columns=['asof_yyyymm'],values=a)
col=[x for x in obj.columns if x not in a and x not in ['asof_yyyymm']]
obj4=obj.loc[:,col]
k=np.arange(1,300,6).tolist()
obj4=obj4.loc[k,:]
obj2.reset_index(inplace=True,drop=True)
obj4.reset_index(inplace=True,drop=True)
obj5=pd.concat([obj4,obj2],axis=1)
print obj5.columns
i=0
j=0
fig,axis=plt.subplots(nrows=6,ncols=6,figsize=(16,16))
for x in range(13,49):
    axis[j,i].plot(obj5.iloc[:,x])
    i=i+1
    if (i==6):
        j=j+1
        i=0
plt.show()
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
dropped=obj5.drop(obj5.columns[np.arange(25,37)],axis=1)
train_x=dropped.sample(40,random_state=2)
train_y=obj5.iloc[:,25:36].sample(40,random_state=2)
test_x=dropped.iloc[[int(x) for x in obj5.index if x not in train_x.index],:]
test_y=obj5.iloc[:,25:36].iloc[[int(x) for x in obj5.index if x not in train_y.index],:]
lr.fit(train_x,train_y)
ans=pd.DataFrame(lr.predict(test_x))
ans.reset_index(inplace=True,drop=True)
test_y.reset_index(drop=True,inplace=True)
from sklearn.metrics import explained_variance_score
acc=list()
i=0
from matplotlib import pyplot as plt
fig,axis=plt.subplots(nrows=10,ncols=2,figsize=(30,30))
j=0
k=0
for i in range(0,10):
    axis[j,k].plot(test_y.iloc[:,i])
    k=k+1
    axis[j,k].plot(ans.iloc[:,i])
    k=0
    j=j+1