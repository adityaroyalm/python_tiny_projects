# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:37:21 2017

@author: aditya royal
"""
import pandas as pd
contracts_end=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Train_BG1IL20\Train\Contracts_End.csv')
contracts_start=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Train_BG1IL20\Train\Contracts_New.csv')
import collections
import matplotlib.pyplot as plt
K=collections.Counter(contracts_end['MUNICIPALITY'])
df=pd.DataFrame.from_dict(K,orient='index')
#print contracts_end['YEAR_END_CONTRACT'].hist()
sensus=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\indicadores_seccion_censal_csv_en\C2011_ccaa09_Indicadores.csv')
sensus['cpro']=[str(x).zfill(1) for x in sensus['cpro'].tolist()]
sensus['cmun']=[str(x).zfill(3) for x in sensus['cmun'].tolist()]
sensus['dist']=[str(x).zfill(2) for x in sensus['dist'].tolist()]
sensus['secc']=[str(x).zfill(3) for x in sensus['secc'].tolist()]
sensus['CENSUS_SECTION']=sensus[['cpro','cmun','dist','secc']].apply(lambda x: ''.join(x),axis=1)
sensus['CENSUS_SECTION']=sensus[['cpro','cmun','dist','secc']].apply(lambda x: ''.join(x),axis=1)
contracts_end_merged=contracts_end.merge(sensus,how='inner',left_on='CENSUS_SECTION',right_on='CENSUS_SECTION')

contracts_new_merged=contracts_start.merge(sensus,left_on='CENSUS SECTION',right_on='CENSUS_SECTION',how='inner')
#print len(contracts_start['YEAR_CONTRACT'].unique())
#print len(contracts_end['YEAR_END_CONTRACT'].unique())
contracts_start['YEAR_CONTRACT'].hist(bins=12)
#contracts_end['YEAR_END_CONTRACT'].hist(bins=11)
#contracts_end['YEAR_CONTRACT']=contracts_end['YEAR_END_CONTRACT']
#contracts_end.drop('YEAR_CONTRACT',axis=1,inplace=True)
#start_year=contracts_start['YEAR_CONTRACT'].value_counts()
#contracts_start['CENSUS_SECTION']=contracts_start['CENSUS SECTION']
#contracts_start.drop('CENSUS SECTION',axis=1,inplace=True)

#contracts=pd.merge(contracts_start,contracts_end,how='inner',on=['MUNICIPALITY','WATER_USAGE','TYPE_OF_HOUSEHOLD','CENSUS_SECTION'])
#contracts.drop_duplicates(subset=['MUNICIPALITY','WATER_USAGE','TYPE_OF_HOUSEHOLD','CENSUS_SECTION'],keep=False)
#end_year=contracts_end['YEAR_END_CONTRACT'].value_counts()
#compare=pd.concat([start_year,end_year],axis=1)
#compare['diff']=compare['YEAR_CONTRACT']-compare['YEAR_END_CONTRACT']
#
#month={'jan.':1,'feb.':2,'mar.':3,'apr.':4,'may.':5,'jun.':6,'jul.':7,'aug.':8,'sep.':9,'oct.':10,'nov.':11,'dec.':12,'ago.':8}
import numpy as np
#contracts['month_number']=contracts['MONTH_CONTRACT'].map(lambda x: month[x])
#contracts['month_end_number']=contracts['MONTH_END_CONTRACT'].map(lambda x: month[x])
#contracts['month_number'].hist(bins=12)
#contracts['month_end_number'].hist(bins=12)
#contracts['day']=contracts['DAY_ALTA_CONTR']
#contracts['end_day']=contracts['DAY_END_CONTRACT']
#contracts.drop(contracts[contracts['YEAR_CONTRACT']+30*contracts['month_number']+contracts['day']>30*contracts['month_end_number']+contracts['end_day']+contracts['YEAR_END_CONTRACT']].index,inplace=True)
#contracts['timeline']=(30*contracts['month_end_number']+contracts['end_day'])-(30*contracts['month_number']+contracts['day'])
#contacts_pre_2007['END.DATE']
#contacts=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Train_BG1IL20\Train\Contacts_Pre_2017.csv')
#contacts['start']=pd.DatetimeIndex(contacts['START.DATE']).day
#contacts['end']=pd.DatetimeIndex(contacts['END.DATE']).day
#resolution=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Train_BG1IL20\Train\Resolution_Pre_2017.csv')
#resolution['date']=pd.DatetimeIndex(resolution['Date']).day
#resolution['date'].hist()
#contacts['start'].hist(bins=30)
#contacts['end'].hist(bins=30)
#avg=contracts['timeline'].mean()
#resolution_2010=resolution.loc[resolution['Year']==2010]
#contacts['START.DATE']=contacts['START.DATE'].astype('datetime64[ns]')
#contacts['Year']=[x.year for x in contacts['START.DATE']]
#contacts_2010=contacts.loc[contacts['Year']==2010]
#contracts_2008=contracts_start.loc[contracts_start['YEAR_CONTRACT']<2008]
#sorted(contracts_2008['YEAR_CONTRACT'])
#contracts_end_2008=contracts_end.loc[contracts_end['YEAR_END_CONTRACT']<2008]
#sorted(contracts_end_2008['YEAR_END_CONTRACT'])
#month={'jan.':1,'feb.':2,'mar.':3,'apr.':4,'may.':5,'jun.':6,'jul.':7,'aug.':8,'sep.':9,'oct.':10,'nov.':11,'dec.':12,'ago.':8}
#contracts_2008['month_number']=contracts_2008['MONTH_CONTRACT'].map(lambda x: month[x])
#contracts_end_2008['month_end_number']=contracts_end_2008['MONTH_END_CONTRACT'].map(lambda x: month[x])
#contracts_2008['DAY_ALTA_CONTR'].fillna(0,inplace=True)
#contracts_end_2008['DAY_END_CONTRACT'].fillna(0,inplace=True)
#contracts_2008['DAY_ALTA_CONTR']=contracts_2008['DAY_ALTA_CONTR'].astype(np.int64)
#contracts_end_2008['DAY_END_CONTRACT']=contracts_end_2008['DAY_END_CONTRACT'].astype(np.int64)
#contracts_2008['DAY_ALTA_CONTR']=[format(x,'02') for x in contracts_2008['DAY_ALTA_CONTR']]
#contracts_end_2008['DAY_END_CONTRACT']=[format(x,'02') for x in contracts_end_2008['DAY_END_CONTRACT']]
#contracts_2008.DAY_ALTA_CONTR=contracts_2008.DAY_ALTA_CONTR.astype(str)
#contracts_end_2008.DAY_END_CONTRACT=contracts_end_2008.DAY_END_CONTRACT.astype(str)

#contracts_2008['month_number'].fillna(0,inplace=True)
#contracts_end_2008['month_end_number'].fillna(0,inplace=True)
#contracts_2008['month_number']=contracts_2008['month_number'].astype(np.int64)
#contracts_end_2008['month_number']=contracts_end_2008['month_end_number'].astype(np.int64)
#contracts_2008['month_number']=[format(x,'02') for x in contracts_2008['month_number']]
#contracts_end_2008['month_end_number']=[format(x,'02') for x in contracts_end_2008['month_end_number']]
#contracts_2008.month_number=contracts_2008.month_number.astype(str)
#contracts_end_2008.month_number=contracts_end_2008.month_end_number.astype(str)
#contracts_2008.YEAR_CONTRACT=contracts_2008.YEAR_CONTRACT.astype(str)
#contracts_end_2008.YEAR_END_CONTRACT=contracts_end_2008.YEAR_END_CONTRACT.astype(str)
#contracts_2008['MONTH_CONTRACT'].fillna(0,inplace=True)
#contracts_end_2008['MONTH_END_CONTRACT'].fillna(0,inplace=True)
#contracts_2008.MONTH_CONTRACT=contracts_2008.MONTH_CONTRACT.astype(str)
#contracts_end_2008.MONTH_END_CONTRACT=contracts_end_2008.MONTH_END_CONTRACT.astype(str)
#contracts_2008.loc[contracts_2008['MONTH_CONTRACT']=='ago.','MONTH_CONTRACT']='aug.'
#contracts_end_2008.loc[contracts_end_2008['MONTH_END_CONTRACT']=='ago.','MONTH_END_CONTRACT']='aug.'
#contracts_2008['MONTH_CONTRACT']=contracts_2008['MONTH_CONTRACT'].map(lambda x: x.rstrip('.'))
#contracts_end_2008['MONTH_END_CONTRACT']=contracts_end_2008['MONTH_END_CONTRACT'].map(lambda x: x.rstrip('.'))
#contracts_2008['DAY_ALTA_CONTR'].fillna(round(contracts_2008['DAY_ALTA_CONTR'].mean(),0),inplace=True)
#contracts_end_2008['DAY_END_CONTRACT'].fillna(round(contracts_end_2008['DAY_END_CONTRACT'].mean(),0),inplace=True)
#contracts_2008['YEAR_CONTRACT'].fillna(round(contracts_2008['YEAR_CONTRACT'].mean(),0),inplace=True)
#contracts_end_2008['YEAR_END_CONTRACT'].fillna(round(contracts_end_2008['YEAR_END_CONTRACT'].mean(),0),inplace=True)
#contracts_2008['YEAR_CONTRACT'].replace('0',round(contracts_2008['YEAR_CONTRACT'].mean(),0)).astype(str)
#contracts_end_2008['YEAR_END_CONTRACT'].replace('0',round(contracts_end_2008['YEAR_END_CONTRACT'].mean(),0)).astype(str)
#contracts_2008['DAY_ALTA_CONTR'].replace('0',round(contracts_2008['DAY_ALTA_CONTR'].mean(),0)).astype(str)
#contracts_end_2008['DAY_END_CONTRACT'].replace('0',round(contracts_end_2008['DAY_END_CONTRACT'].mean(),0)).astype(str)
#contracts_2008['date']=contracts_2008['DAY_ALTA_CONTR']+' '+contracts_2008['MONTH_CONTRACT']+' '+contracts_2008['YEAR_CONTRACT']
#contracts_end_2008['date']=contracts_end_2008['DAY_END_CONTRACT']+' '+contracts_end_2008['MONTH_END_CONTRACT']+' '+contracts_end_2008['YEAR_END_CONTRACT']
#from datetime import datetime
#contracts_2008=contracts_2008.reset_index(drop=True)
#contracts_end_2008=contracts_end_2008.reset_index(drop=True)
#contracts_2008['dated']=[0]*len(contracts_2008['date'])
#contracts_end_2008['dated']=[0]*len(contracts_end_2008['date'])
#i=0
#for d in contracts_2008['date']:
 #   contracts_2008.loc[i,'dated']=datetime.strptime(d,'%d %b %Y').date()
  #  i=i+1
#i=0
#for d in contracts_end_2008['date']:
    #contracts_end_2008.loc[i,'dated']=datetime.strptime(d,'%d %b %Y').date()
    #i=i+1
### creating model only on contracts
#import matplotlib.pyplot as plt
#import sklearn
#from datetime import datetime
#contacts['START.DATE']=contacts['START.DATE'].astype(np.datetime64)
#resolution['Date']=resolution['Date'].astype(np.datetime64)
#los=contacts.dtypes
#contacts['START.DATEE']=contacts['START.DATE'].day()
#contacts['month']=[int(x.strftime('%m'))*30 for x in contacts['START.DATE']]
#resolution['month']=[int(x.strftime('%m'))*30 for x in resolution['Date']]
#contacts['day']=[int(x.strftime('%d'))for x in contacts['START.DATE']]
#resolution['day']=[int(x.strftime('%d')) for x in resolution['Date']]
#contacts['year']=[int(x.strftime('%Y')) for x in contacts['START.DATE']]
#resolution['year']=[int(x.strftime('%Y')) for x in resolution['Date']]
#contacts['END.DATE']=contacts['END.DATE'].astype(str)
#contacts['CONTACT.TYPE']=contacts['CONTACT.TYPE'].astype(str)
#contacts['sum']=contacts['month']+contacts['day']+contacts['year']
#resolution['sum']=resolution['day']+resolution['month']+resolution['year']
#b=[]
#contacts['sum'].fillna(0,inplace=True)
#resolution['sum'].fillna(0,inplace=True)
#from collections import Counter
#lee=range(len(Counter(contacts['CONTACT.TYPE']).keys()))
#dictio=Counter(contacts['CONTACT.TYPE']).keys()
#dictio2=Counter(resolution['Category']).keys()
#dictio3=Counter(resolution['Subject']).keys()
#dicti=dict(zip(dictio,range(len(dictio))))
#dicti2=dict(zip(dictio2,range(len(dictio2))))
#dicti3=dict(zip(dictio3,range(len(dictio3))))
#contacts['contact']=[dicti[x] for x in contacts['CONTACT.TYPE']]
#resolution['category']=[dicti2[x] for x in resolution['Category']]
#resolution['subject']=[dicti3[x] for x in resolution['Subject']]
#contacts['contact'].fillna(0,inplace=True)
#X=contacts.as_matrix(columns=['sum','contact'])
#X1=resolution.as_matrix(columns=['sum','category','subject'])
#contacts.loc[Counter(X[X[0]==None or X[1]==None]).keys(),['month','year','day']]=0
#Y=contacts.as_matrix(columns=['Contacts'])
#Y1=resolution.as_matrix(columns=['Resolution'])
#Test=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Test_74k7qT9\Test\Contacts2017.csv')
#Test1=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Test_74k7qT9\Test\Resolution2017.csv')
#Test['Date']=Test['Date'].astype(np.datetime64)
#Test1['Date']=Test1['Date'].astype(np.datetime64)
#Test['month']=[int(x.strftime('%m'))*30 for x in Test['Date']]
#Test1['month']=[int(x.strftime('%m'))*30 for x in Test1['Date']]
#Test['day']=[int(x.strftime('%d')) for x in Test['Date']]
#Test1['day']=[int(x.strftime('%d')) for x in Test1['Date']]
#Test['year']=[int(x.strftime('%Y')) for x in Test['Date']]
#Test1['year']=[int(x.strftime('%Y')) for x in Test1['Date']]
#Test['sum']=Test['day']+Test['year']+Test['month']
#Test1['sum']=Test1['day']+Test1['year']+Test1['month']
#c=[]
#Test['contact']=[dicti[x] for x in Test['CONTACT.TYPE']]
#Test1['category']=[dicti2[x] for x in Test1['Category']]
#Test1['subject']=[dicti3[x] for x in Test1['Subject']]
#t=Test.as_matrix(columns=['sum','contact'])
#t1=Test1.as_matrix(columns=['sum','category','subject'])
#n_neighbors=5 
from sklearn import neighbors
import scipy.sparse

#for i, weights in enumerate(['uniform', 'distance']):
 #   knn=neighbors.KNeighborsRegressor(n_neighbors,weights=weights)
  #  y_=knn.fit(X,Y).predict(t)
   # plt.scatter(X, y, c='k', label='data')
    #plt.plot(T, y_, c='g', label='prediction')
#plt.show()
#from sklearn.ensemble import RandomForestClassifier
#rf=RandomForestClassifier(n_estimators=100)
#rf.fit(X1,Y1)
#results1=rf.predict(t1)

results=pd.DataFrame(results)
results.to_csv(r'C:\Users\aditya royal\Desktop\amma\results.csv')