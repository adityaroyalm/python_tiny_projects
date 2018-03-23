# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:46:12 2017

@author: aditya royal
"""

import pandas as pd
import numpy as np
#load data
automobile=pd.read_csv('C:/Users/aditya royal/Desktop/Automobile_data.csv')
#create a series
series_obj=automobile.loc[:,'symboling']
#printing its values
print series_obj.values
#printing it's index
print series_obj.index
#changing the index
series_obj.index=np.arange(1,410,2)
print series_obj.index
#boolean indexing
print series_obj[series_obj<2]
#checking indexes
print 51 in series_obj
#pandassssssssssssssss
#retrieving columns
automobile['make']
# del dataframe columns
del automobile['make']
#values of a dataframe
automobile.values
#checking column names in df
'symboling' in automobile.columns
#drop columns in adataframe
automobile.drop(['symboling','fuel-type'],axis=1)
#selecting indexing 
#automobile.loc[]#for label based indexing
#automobile.iloc[]#for integer based indexing
#automobile.ix[]#for mixed indexing
#filtering
automobile.loc[automobile['fuel-type']=='gas',:]
#function application and mapping
automobile['city-mpg'] =automobile['city-mpg'].apply(lambda x: x+1)
automobile['city-mpg']=automobile['city-mpg'].map(lambda x: x+1)
#sorting index either by row or column
print automobile.sort_index()
#sort indx by values
#descriptive statistics on df
automobile.loc[:,['symboling','width']].sum()
automobile.loc[:,['symboling','width']].mean()
automobile.loc[:,['symboling','width']].max()
automobile.loc[:,['symboling','width']].idxmin()
automobile.loc[:,['symboling','width']].idxmax()
#handling missing data
print automobile.isnull()
#dropping rows having null values 
print automobile.dropna(how='any')
# filling na values
automobile.fillna(0,inplace=True)
