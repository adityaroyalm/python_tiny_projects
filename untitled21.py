# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 13:02:51 2017

@author: aditya royal
"""

import pandas as pd
pd.__version__
pd.show_versions()
data={'animal':['cat','dog','snake','dog','dog','cat','snake','cat','dog'],
      'age':[2.5,3,0.5,np.nan,5,2,4.5,np.nan,7,3],
      'visits':[1,3,2,3,2,3,1,1,2,1],
      'priority':['yes','yes','no','yes',no','no','no','yes','no','no']
      }
labels=['a','b','c','d','e','f','g','g','h','i','j']
df=pd.DataFrame(data,index=labels)
df.groupby('visitors')['priority'].mean()
df.sort_values(by=['age','visits'],ascending=[False,True])
#df.loc('k')=[5.5,'dog',]
df=pd.DataFrame({'A':[1,2,2,3,4,5,5,5,6,7,7]})
for x in range(len(df.loc[:,'A'])):
    if df.loc[x,'A']==df.loc[x+1,'A']:
        print x