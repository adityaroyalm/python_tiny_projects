# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:39:41 2017

@author: aditya royal
"""

import pandas as pd
df=pd.DataFrame([[1,2,3,4,5],[2,3,4,5,6]],columns=['a',',b','c','d','e'])
def some(x):
    print x['a']
df.apply(some,axis=1,raw=True)
from collections import Counter
def get_weight(count,eps=10000,min_count=2):
    if count<min_count:
        return 0
    else:
        return 1/(count+eps)
eps=5000
words=(" ".join(train_qs)).lower().split()
weights=[]
from collecions 