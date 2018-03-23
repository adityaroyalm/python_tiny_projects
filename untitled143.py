# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 21:08:10 2018

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:55:35 2018

@author: aditya royal
"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import r2_score
from datetime import datetime
from sklearn import linear_model
from collections import Counter
df=pd.read_csv('C:/Users/aditya royal/final.txt',sep=' ')
a=df
#df.columns=['id','year-mm-day','windspeedgust','temp','alt_inches']
######find * in the column alt_inches
def preprocessing(c):
    mask=list()
    for x in df.iloc[:,c]:
        try:
            if '*' in str(x):
                mask.append(False)
            else:
               mask.append(True) 
        except:
            mask.append(True)
    digits=[y for x,y in zip(mask,df.iloc[:,c]) if x]
    meandigit=pd.DataFrame([float(x) for x in digits]).mean()
    df.iloc[:,c]=[y if x else meandigit[0] for x,y in zip(mask,df.iloc[:,c])]
    df.iloc[:,c].fillna(meandigit[0],inplace=True)
    return (mask,meandigit)
# ####preprocessing invidual columns
#df['year']=[x[0:4] for x in pd.Series(df.loc[:,'year-mm-day'],dtype=str)]
#df['month']=[x[4:6] for x in pd.Series(df.loc[:,'year-mm-day'],dtype=str)]
#del df['year-mm-day']
#preprocessing(1)
#preprocessing(2)
#preprocessing(3)
#preprocessing(4)
#######clustering
#train,test=train_test_split(df.iloc[:,:6],test_size=0.33,random_state=42)
#unique_id=np.unique(df['id'])
kmeans=KMeans(n_clusters=200).fit(np.array(train.iloc[:,1:6].values))
result_id=kmeans.predict(np.array(train.iloc[:,1:6].values))
labels=kmeans.labels_
fi=[NONE]*np.unique(kmeans.labels_).shape[0]
i=0
j=0
for y in result_id:
    for x in np.unique(labels):
        if y==x:
            fi[j].append(train.iloc[i,0])
        i=i+1
    j=j+1
#zero_id=Counter(zeroth)
#zero_id=sorted(zero_id.items(),key=lambda x:x[1],reverse=True)
#one_id=Counter(first)
#one_id=sorted(one_id.items(),key=lambda x:x[1],reverse=True)
#second_id=Counter(second)
#second_id=sorted(second_id.items(),key=lambda x:x[1],reverse=True)
#third_id=Counter(third)
#third_id=sorted(third_id.items(),key=lambda x:x[1],reverse=True)
#fourth_id=Counter(fourth) 
#fourth_id=sorted(fourth_id.items(),key=lambda x:x[1],reverse=True) 
########linear regressoin
i=0
#for x in train.loc[:,'month']:
#    if int(x) in [3,4,5,6]:
 #       train.loc[:,'month']=3
  #      i=i+1
   # if int(x) in [7,8,9,10]:
    #    train.loc[:,'month']=2
     #   i=i+1
    #if int(x) in [11,12,12]:
     #   train.loc[:,'month']=1
      #  i=i+1
#regr=linear_model.LinearRegression()
#regr.fit(train.iloc[:,[0,1,2]],train.iloc[:,3])
#result=regr.predict(test.iloc[:,[0,1,2]])
accuracy=r2_score(test.iloc[:,3],result)

