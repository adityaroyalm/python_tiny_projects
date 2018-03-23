# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:29:13 2017

@author: aditya royal
"""
import pandas as pd
df_train=pd.read_csv(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects\quora\train.csv')
print df_train.head()
print('Total number of questions in the training data: {}'.format(len(df_train)))
#print('Duplicate pairs: {}%'.format(round(df_train['is_duplicate'].mean()*100,2)))
print('Duplicate pairs={}'.format(round(df_train['is_duplicate'].mean()*100,2)))
qids=pd.Series(df_train['qid1'].tolist()+df_train['qid2'].tolist())
print('ttal no of equestions multiple times: {}'.format(sum(qids.value_counts()>1)))
from collections import Counter
