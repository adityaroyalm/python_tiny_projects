# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:24:50 2017

@author: aditya royal
"""
import numpy as np
import pandas as pd
csv_obj=pd.read_table("C:/Users/aditya royal/Downloads/fsz.txt")
print csv_obj.describe()
print csv_obj.dtypes
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
k=pd.DataFrame()
for x in csv_obj:
    if csv_obj.loc[:,x].dtype!=np.int64:
        k.loc[:,x]=le.fit_transform(csv_obj.loc[:,x])       
print np.dtype(csv_obj.loc[:,'Date'])
from datetime import date
#import datetime
today=date.today()
print today
#print datetime.datetime.strptime(csv_obj.ix[2,'Date'],'%y')
w=''
a=np.zeros(10)
b=np.zeros(10)
i=0
for x in csv_obj.loc[:,'Date']:
    for y in x:
        w=w+y
        if len(w)==4:
            a[i]=w
            i=i+1
            w=''
            break;
del csv_obj['Date']
csv_obj['Date']=pd.Series([str(int(x)) for x in a])
csv_obj['Date']=pd.to_datetime(csv_obj['Date'],format='%Y')
csv_obj['Date']= pd.DatetimeIndex(csv_obj['Date']).year
csv_obj['DateAcquired']=pd.to_datetime(csv_obj['DateAcquired'],format='%Y-%m-%d')
csv_obj['DateAcquired']=pd.DatetimeIndex(csv_obj['DateAcquired']).date
#for i in range(len(a)):
 #   csv_obj.ix[i,'Date']=datetime.datetime.strptime(str(int(a[i])),'%Y')
        
        
            