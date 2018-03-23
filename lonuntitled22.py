# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 07:19:43 2017

@author: aditya royal
"""

import pandas as pd
import numpy as np
df=pd.DataFrame({'B':[1,2,2,3,4,5,5,5,6,7,7],'A':[1,2,3,4,5,6,7,8,9,10,11]})
b=df.loc[df['A'].shift()!=df['A']]
suu= df.sub(df.mean(axis=0),axis=1)
katr= df.sum(axis=1).idxmax()
#print (df.isnull().cumsum(axis=1)==3).idxmax(axis=1)
df.groupby('grp')['vals'].nlargest(3).sum
#print pd.groupby(pd.cut(pd.DataFrame({'A':[1,2,2,3,4,5,5,5,6,7,7]}),2))['A'].mean()
#pd.groupby(pd.cut(df['A'], 3))['B'].sum()
#df.unstack.sort_values()[-3:].index.tolist()
dti=pd.date_range(start='2015-01-1',end='2015-12-31',freq='B')
s=pd.Series(np.random.rand(len(dti)),index=dti)
s[s.index.weekday==2].sum()
print s.resample('M').mean()
print s.groupby(pd.TimeGrouper('4M')).idxmax()
print pd.date_range('2015-01-01','2016-12-31',freq='WOM-3THU')
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
                               '12. Air France', '"Swiss Air"']})
df['FlightNumber']=df['FlightNumber'].interpolate().astype(int)
temp=df.From_To.str.split('_',expand=True)
temp.columns=['From','To']
temp['From']=temp['From'].str.capitalize()
temp['To']=temp['To'].str.capitalize()
df=df.drop('From_To',axis=1)
df=df.join(temp)
df['Airline']=df['Airline'].str.extract('([a-zA-Z\s]+)',expand=False).str.strip()
df['Airline']=df['Airline'].str.extract('([a-zA-Z\s]+)',expand=False).str.strip()
temp2=[x for x in df.RecentDelays]
#delays=df['RecentDelays'].apply(pd.Series)
g=pd.Series(df.ix[2,'RecentDelays'])
g2=df['RecentDelays'].apply(pd.Series)
letters=['A','B','C']
numbers=list(range(10))
mi=pd.MultiIndex.from_product([letters,numbers])
s=pd.Series(np.random.rand(30),index=mi)
print s.index.is_lexsorted()
print s.loc[:,[1,3,6]]
print s.loc[:'B',5:]
new_s=s.swaplevel(0,1)
x=5
y=4
p=pd.tools.util.cartesian_product([np.arange(x),np.arange(y)])
df=pd.DataFrame(np.asarray(p).T,columns=['x','y'])
df['mine']=np.random.binomial(1,0.4,size=x*y)
df['adjacent'] = \
    df.merge(df + [ 1,  1, 0], on=['x', 'y'], how='left')\
      .merge(df + [ 1, -1, 0], on=['x', 'y'], how='left')\
      .merge(df + [-1,  1, 0], on=['x', 'y'], how='left')\
      .merge(df + [-1, -1, 0], on=['x', 'y'], how='left')\
      .merge(df + [ 1,  0, 0], on=['x', 'y'], how='left')\
      .merge(df + [-1,  0, 0], on=['x', 'y'], how='left')\
      .merge(df + [ 0,  1, 0], on=['x', 'y'], how='left')\
      .merge(df + [ 0, -1, 0], on=['x', 'y'], how='left')\
       .iloc[:, 3:]\
        .sum(axis=1)
