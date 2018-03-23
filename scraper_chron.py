# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:07:22 2018

@author: aditya royal
"""
import pandas as pd
li=[6,6,4,8,44,867,9907]
df=pd.DataFrame(li,columns=['p'])
k=df[['p']].apply(lambda x:df)