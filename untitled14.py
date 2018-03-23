# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 14:50:11 2017

@author: aditya royal
"""

import pandas as pd
import numpy as np
df_train=pd.read_csv(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects\quora\train.csv')
df_train.head()
from matplotlib import pyplot as plt
quids=pd.Series(df_train['qid1'].tolist()+df_train['qid2'].tolist(),index=range(len(df_train['qid1'])+len(df_train['qid2'])))
plt.hist(quids.value_counts(),bins=50)
plt.yscale('log')
plt.figure(figsize=(12,5))
print len(quids.unique())
quids=np.array(quids)
quest=pd.Series(df_train['question1'].tolist()+df_train['question2'].tolist())
ind=np.unique(quids,return_index=True)
inde=ind[1]
quads_unique=quids[inde.tolist()]