# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 20:16:28 2017

@author: aditya royal
"""
import numpy as np
arr=np.zeros((7,7))
#arr = [[0 for y in xrange(5)] for x in xrange(2)]   
for n in range(7): 
    arr[n:7-n,[n,-n-1]]=7-n
    arr[[n,-n-1],n:7-n]=7-n
    