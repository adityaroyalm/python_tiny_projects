# -*- coding: utf-8 -*-
"""
Created on Wed May 03 20:08:50 2017

@author: aditya royal
"""
from pandas import DataFrame as DF 
dct = {'a':3, 'b':3,'c':5,'d':3}
lst = ['c', 'd', 'a', 'b', 'd']
k=DF(lst)
ko=k[0].map(dct)