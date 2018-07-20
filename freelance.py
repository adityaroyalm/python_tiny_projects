# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:16:50 2018

@author: aditya royal
"""
import pandas as pd
import xlsxwriter
df=pd.read_excel('C:/Users/aditya royal/Downloads/Firm List_sample.xlsx')
k=pd.read_csv('C:/Users/aditya royal/Downloads/filename.csv')
j=k.T
a='www.facebook.com'
for x in range(len(df.index)):
  if not(j.index[x].startswith(' None')):
      df.loc[x,'answ']=a+'/'+str(j.index[x][4:-2])
writer=pd.ExcelWriter('facebook_scrap.xlsx',engine='xlsxwriter')
df.to_excel(writer,'sheet1')
