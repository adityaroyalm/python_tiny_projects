# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:24:43 2017

@author: aditya royal
"""
import pandas as pd
import numpy as np
obj=pd.read_csv("C:/Users/aditya royal/Desktop/New folder (2)/CompleteDataset.csv")
grouped=obj.loc[:,'Overall'].groupby(obj.loc[:,'Nationality'])
grp_mean=grouped.mean()
grp_mean.sort_values(inplace=True,ascending=False)
count=dict()
for x in (np.arange(15,48)):
    if(obj.iloc[:,x].dtype==str):
        count[x]=count[x]+1
    #obj.iloc[:,x].dtype==int
    #obj.iloc[:,x].hist()
#for x in obj.iloc[:,15:48].columns:
 #   print type(x)