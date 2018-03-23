# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 20:07:01 2017

@author: aditya royal
"""
import sqlalchemy
import twisted
#import xgboost as xgb
from bs4 import BeautifulSoup
#read in data
dtrain=xgb.DMatrix('')
dtest=xgb.DMatrix('')
param={'max_depth':2,'eta':1,'silent':1,'objective':'binary:logistic'}
num_round=2
bst=xgb.train(param,dtrain,num_round)
preds=bst.predict(test)
