# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 07:51:59 2017

@author: aditya royal
"""
import IPyton.nbformat.current as nbf
nb=nbf.read(open('untitled53.py','r'),'py')
nbf.write(nb,open('test.ipynb','w'),'ipynb')
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from skearn.linear_model import LinearRegression
train_data=pd.read_csv('train_ysMSKmq.csv')
test_data=pd.read_Csv('test_uLBXQQR.csv')
train_data.head()
