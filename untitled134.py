# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:22:53 2018

@author: aditya royal
"""
import numpy as np
a=np.array(([1,1,2,3],[2,4,1,4]))
costs=np.column_stack(a)
s=np.mean(costs[:,1],axis=0)
print(s)