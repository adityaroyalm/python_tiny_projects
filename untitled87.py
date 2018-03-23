# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 11:30:42 2017

@author: aditya royal
"""
import pandas as pd
import numpy as np
a=np.arange(-30,30)
df=pd.read_csv('C:/Users/aditya royal/Downloads/boston.marathon.wtimes.txt',sep='\t')
#df=pd.DataFrame()
#df.loc[:,'s']=a
#df.loc[:,'sss']=a*a
#df.loc[:,'IMPORTS']=np.log(df.loc[:,'IMPORTS'])
#df.loc[:,'GDP']=np.log(df.loc[:,'GDP'])
np.random.seed(2)
#import scipy.stats
#slope, intercept, r_value, p_value, std_err=scipy.stats.linregress(df.loc[:,'MONTHS'],df.loc[:,'CALLS'])
import untitled88
untitled88.looper(df,'year','minutes',intox=1,intoy=1)
#df.loc[:,'IMPORTS'].hist()
#df.loc[:,'GDP'].hist()
