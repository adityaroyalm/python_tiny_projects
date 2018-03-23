# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:40:44 2018

@author: aditya royal
"""

import pandas as pd
import seaborn.apionly as sns
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
obj=pd.read_csv('C:/Users/aditya royal/Downloads/MPG.csv')
mpg_year=obj.groupby(['model year'])['mpg'].mean()
mpg_year.plot()
plt.scatter(x=obj['mpg'],y=obj['horsepower'])
plt.show()
plt.bar(obj['mpg'],obj['origin'])
#plt.bar(obj['car manufacturer'],obj['origin'])
origin_group=obj.groupby(['cylinders'])
plt.hist(obj['mpg'])
for name,group in origin_group:
    plt.boxplot(origin_group['mpg'].get_group(name).values)
    plt.show()
#sns.heatmap(obj[['mpg','cylinders']].T)
plt.scatter(x=obj['weight'],y=obj['mpg'],c=list(obj['origin'].values),cmap=matplotlib.colors.ListedColormap(['red','green','blue']))
sns.pairplot(obj[['mpg','displacement','horsepower','weight','acceleration']].dropna())
