# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 09:26:17 2017

@author: aditya royal
"""
import numpy as np
import pandas as pd
df=pd.DataFrame({'vals':[7,2,0,-3,-4,-2,-5,0,3,4],'grps':['a','s','d','a','s','s','d','d','a','s']})
dd=df[df['vals']==0]
izero=np.r_[-1,(df[df['vals']==0]).index]
idx=np.arange(len(df))
print izero[np.searchsorted(izero-1,idx)-1]
df['y']=idx-izero[np.searchsorted(izero-1,idx)-1]
def replace(group):
    mask=group<0
    group[mask]=group[mask]*-1
    print group
    return group
print df.groupby(['grps'])['vals'].transform(replace)
