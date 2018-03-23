# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 15:28:58 2017

@author: aditya royal
"""

import pandas as pd
dataset=pd.read_csv("C:/Users/aditya royal/Desktop/MLsoftaware_projects/allstate claim seveirity/train.csv")
dataset_test=pd.read_csv("C:/Users/aditya royal/Desktop/MLsoftaware_projects/allstate claim seveirity/train.csv")
ID=dataset_test['id']
dataset_test.drop('id',axis=1,inplace=True)
#midinh vslurd
