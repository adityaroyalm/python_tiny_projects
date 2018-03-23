# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:22:53 2018

@author: aditya royal
"""
#import os
#import numpy as np
#import re
#import pandas as pd
#df=pd.DataFrame(0,index=np.arange(100000),columns=['column'])
#directory = os.fsencode('C:/Users/aditya royal/Downloads/facebook')
#k=list()
#for file in os.listdir(directory):
#    filename = os.fsdecode(file)
#    if filename.endswith(".txt"): 
#        k.append(re.search('(filename.txt)',filename))
#        obj=pd.read_csv('C:/Users/aditya royal/Downloads/facebook/'+str(filename))
#        obj=obj.T
#        r=re.search(r'(.*)(?:first)+',filename).group(1)
#        r=int(r)
#        i=-1
#        l=r-np.shape(obj)[0]
#        for x in obj.index:
#            i=i+1
#            if not str(x).startswith(' None'):
#                df.iloc[l+i,0]=obj.index[i]
#            else:
#                continue
#    else:
#        continue
i=-1
for x in obj_final.loc[:,'column']:
    i=i+1
    try:
        obj_final.loc[i,'column']='https://www.facebook.com/'+x
    except:
        continue
#obj_csv=obj_final.to_csv('test.csv',index=False)
#df_new=pd.read_csv('test.csv')
#writer=pd.ExcelWriter('test.xlsx')
#df_new.to_excel(writer,index=True)
#writer.save()

