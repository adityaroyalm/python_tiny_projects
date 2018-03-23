# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:11:16 2018

@author: aditya royal
"""

#looper(df,a,b,intox=1,intoy=1):
import sys
piu=0
kiu=0
multiplier_x=1.0000
multiplier_y=1.0000
import untitled90
least=sys.float_info.max
from sklearn import linear_model
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/aditya royal/Downloads/boston.marathon.wtimes.txt',sep='\t')
a=df.iloc[:,0]
b=df.iloc[:,1]
import numpy as np
from sklearn.metrics import mean_squared_error
regr=linear_model.LinearRegression()
#dfx=df.sort_values(by='year')
#dfx.reset_index(drop=True)
#dfy=df.sort_values(by='minutes')
#dfy.reset_index(drop=True)
plt.scatter(dfx.loc[:,'year'],dfx.loc[:,'minutes'])
lines_x=1
lines_y=1
kse=dict()
for alpha in range(0,360,5):
    abline(a,b)
# while (lines_x<=200):
#     temp=0
#     for p in range(lines_x):
#         df_x=dfx.iloc[p*len(dfx)/lines_x:(p+1)*len(dfx)/lines_x,:]
#         decider_x=np.absolute(np.absolute(df_x.loc[:,a].corr(df_x.loc[:,b]))/np.absolute(dfx.loc[:,a].corr(dfx.loc[:,b])))
#         if (decider_x>=multiplier_x or decider_x<=1/multiplier_x):
#             fitt=regr.fit(df_x.loc[:,a].to_frame(),df_x.loc[:,b].to_frame())
#             pred=fitt.predict(df_x.loc[:,a].to_frame())
#             temp=int(mean_squared_error(df_x.loc[:,b].to_frame(),pred)+temp)
#             kse[temp]=lines_x
#             piu=99
    
#     if (piu!=99):
#         print 'decrease multiplier'
        
            
#     if (intox*temp<least):
        
#         least=temp  
#         least_x=least   
#     if(temp==0):
#         break
#     lines_x=lines_x+1

# lines_x=1
# lines_y=1

# least=sys.float_info.max
# while (lines_y<=20):
#     temp=0
#     for k in range(lines_y):
#         df_y=dfy.iloc[k*len(dfy)/lines_y:(k+1)*len(dfy)/lines_y,:] 
#         decider_y=np.absolute(np.absolute(df_y.loc[:,a].corr(df_y.loc[:,b]))/np.absolute(dfy.loc[:,a].corr(dfy.loc[:,b])))
#         if (decider_y>=multiplier_y or decider_y<=1/multiplier_y):
#             fitt=regr.fit(df_y.loc[:,a].to_frame(),df_y.loc[:,b].to_frame())
#             pred=fitt.predict(df_y.loc[:,a].to_frame())
#             temp=int(mean_squared_error(df_y.loc[:,b].to_frame(),pred)+temp)
#             kse[temp]=lines_y
#             kiu=99
            
#     if (kiu!=99):
#         print 'decrease multiplier'
#     if (intoy*temp<least):
#         least=temp
#         least_y=least 
#     if(temp==0):
#         break
#     lines_y=lines_y+1
# if (piu==99 and kiu==99):
#     if (least_x<least_y):
#         kse[least_y]=0
#         untitled90.otherfunc(df,a,b,multiplier_x,multiplier_y,lines_x=kse[least_x],lines_y=kse[least_y])
# if (piu==99 and kiu==99):
#     if (least_x>least_y):
#         kse[least_x]=0   
#         untitled90.otherfunc(df,a,b,multiplier_x,multiplier_y,lines_x=kse[least_x],lines_y=kse[least_y])
#     if (least_x==least_y):
#         untitled90.otherfunc(df,a,b,multiplier_x,multiplier_y,lines_x=kse[least_x],lines_y=0)



#original regression line
#fitt=regr.fit(dfx.loc[:,a].to_frame(),dfx.loc[:,b].to_frame())
#pred=fitt.predict(dfx.loc[:,a].to_frame())
#print(plt.plot(dfx.loc[:,a],pred))
    
    