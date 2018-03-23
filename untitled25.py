# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 23:19:16 2017

@author: aditya royal
"""

import pandas as pd
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(data,index=labels)
k=df.loc[df['age'].isnull(),]
df[df['age'].between(2,4)]
df.loc['K']=[5.5,'dog','no',2]
df.drop('K')
df['animal'].value_counts()
df.sort_values(by=['age','visits'],ascending=[False,True])
df['priority']=df['priority'].map({'yes':True,'no':False})
df['animal']=df['animal'].replace('snake','python')
df2=df.pivot_table(index='animal',columns='visits',values='age',aggfunc='mean')
df=pd.DataFrame({'A':[1,2,2,3,4,5,5,5,6,7,7]})
ddf=df.loc[df['A']!=df['A'].shift()]
dfr=df.sub(df.mean(0),axis=1)
print df.sum(0).argmin()
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
print df.groupby('grps')['vals'].nlargest(3)
dff=pd.DataFrame()
dff['A']=np.arange(0,101)
dff['B']=np.random.uniform(1,3,101)
df.groupby(pd.cut(dff['A'], np.arange(0, 101, 10)))['B'].sum()
