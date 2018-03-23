# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 15:50:04 2017

@author: aditya royal
"""

import numpy as np
import pandas as pd
menu=pd.read_csv("D:/MLsoftaware_projects/mcdonalds/menu.csv")
print menu.head(4)
print menu.isnull().any()
print menu.shape
menu.describe()
from matplotlib import pyplot as plt
#f,axes=plt.subplots(3,3,figsize=(10,10))
s=np.linspace(0,3,10)
import seaborn as sns
cols= menu.columns.tolist()
int_cols=[]
for i in range(len(cols)):
    if isinstance(menu.iloc[1,i],str)==False:
        int_cols.append(cols[i])
from matplotlib import pyplot as plt
import seaborn as sns
ncol=3
for i in range(7):
    fig,ax=plt.subplots(nrows=1,ncols=3)
    for j in range(ncol):
        cmap=sns.cubehelix_palette(start=0.0,light=1,as_cmap=True)
        sns.kdeplot(menu.loc[:,int_cols[j]],menu.loc[:,int_cols[i]],cmap=cmap,ax=ax[j])

#cmap=sns.cubehelix_palette(start=0.0,light=1,as_cmap=True)
#for i in range(7)
#x=menu['Cholesterol (% Daily Value)']
#y=menu['Sodium (% Daily Value)']
#sns.kdeplot(x,y,cmap=cmap,ax=axes[0,0])
import plotly.tools 
import plotly 
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
a = menu['Cholesterol (% Daily Value)'].values
b = menu['Item'].values         
trace1=go.Scatter(y=a,x=b,mode='markers',marker={'size':menu['Cholesterol (% Daily Value)'].values})
layout=go.Layout(title='random_title')
data=[trace1]
figure=go.Figure(data=data,layout=layout)
py.plot(figure)
