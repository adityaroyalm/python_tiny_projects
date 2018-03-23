# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 20:12:11 2017

@author: aditya royal
"""
import pandas as pd
from collections import Counter
#import xgboost as xgb
read_csv=pd.read_csv(r'D:\MLsoftaware_projects\zillow\properties_2016.csv\properties_2016.csv',dtype=object)
#plot histogram on first column using and importing collections#
train_csv=pd.read_csv(r'D:\MLsoftaware_projects\zillow\train_2016.csv\train_2016.csv',dtype=object)

frq=Counter(read_csv.loc[:,'airconditioningtypeid'])

#print frq
ser_frq=pd.Series(list(dict(frq).values()))
ser_frq.plot(kind='bar')

#see if there are any duplicate rows in any csv's
#if len(read_csv.loc[:,'parcelid'])==len(set(read_csv.loc[:,'parcelid'])):
   # print 'aditya'
#use xgboost
set_len=len(set(train_csv.loc[:,'parcelid']))
common=set(read_csv.loc[:,'parcelid']) & set(train_csv.loc[:,'parcelid'])
common1=[x for x in read_csv.loc[:,'parcelid'] if x in common]
key_list={}

for key,value in Counter(train_csv.loc[:,'parcelid']).iteritems():
   if value>1:
      key_list[key]=value
without_duplicates=[x for x in train_csv.loc[:,'parcelid'] if x not in key_list.keys()]
without_duplicates_csv=train_csv.loc[train_csv.loc[:,'parcelid'].isin(without_duplicates).tolist(),:]
merged_dfright=pd.merge(read_csv,without_duplicates_csv,how='right',on='parcelid')
#a=[3,5,10,6,3]
#b=[5,6,3,3]
#sam=list(set(a)&set(b))
#dtrain=xgb.DMatrix('merged_dfright')
test_test=[x for x in read_csv.loc[:,'parcelid'] if x not in without_duplicates]
#test_test_csv=read_csv.loc[read_csv.loc[:,'parcelid'].isin(test_test).tolist(),:]
import cProfile
cProfile.run('foo()')
