# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:15:56 2017

@author: aditya royal
"""
import numpy as np
x=np.arange(30)
y=np.arange(1,60,2)
result = 0
for i in range(len(x)):
    for j in range(len(y)):
        result += x[i] * y[j]
print result
f=sum(x)
g=sum(y)
print sum(x)*sum(y)