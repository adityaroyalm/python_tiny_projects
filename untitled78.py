# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:33:20 2017

@author: aditya royal
"""
import pandas as pd
a=pd.Series([5,5,8,1,2,32,1,5,8,9,8,9])
#a.apply(len)
print a.value_counts()
dist_train=train_qs.apply(lambda x:len(x.split(' ')))
from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
def word_match_share():
    for word in str(row['question1']).lower().split():
        if word not in stops:
            q1words[word]=1
