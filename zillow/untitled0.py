# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:16:48 2017

@author: aditya royal
"""

import pandas as pd
read_csv=pd.read_csv(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects\zillow\properties_2016.csv\properties_2016.csv',dtype=object)
#plot histogram on first column using and importing collections#
train_csv=pd.read_csv(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects\zillow\train_2016.csv\train_2016.csv',dtype=object)
from collections import Counter
frq=Counter(read_csv.loc[:,'airconditioningtypeid'])

print frq
ser_frq=pd.Series(list(dict(frq).values()))
ser_frq.plot(kind='bar')
merged_df=pd.merge(read_csv,train_csv,how='left',on='parcelid')
#see if there are any duplicate rows in any csv's
if len(read_csv.loc[:,'parcelid'])==len(set(read_csv.loc[:,'parcelid'])):
    print 'aditya'
print merged_df.head()