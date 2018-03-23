# -*- coding: utf-8 -*-
"""
Created on Fri May 05 13:33:57 2017

@author: aditya royal
"""
import pandas as pd
train  = pd.DataFrame({'id':[1,2,4],'features':[["A","B","C"],["A","D","E"],["C","D","F"]]})
train["features"].apply(lambda x: " ".join([i.split(" ") for i in x]))
train['features_t'] =train["features"].map(lambda x: "_".join(["_".join(i.split(" ")) for i in x ]))
