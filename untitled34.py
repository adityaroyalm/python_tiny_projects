# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:15:53 2017

@author: aditya royal
"""

ret = 0
X=[-7 -13]
Y=[1,-5]
curr = (X[0], Y[0])
for i in range(0,len(X)):
    stepsX = abs(curr[0] - X[i])
    stepsY = abs(curr[1] - Y[i])
    ret += max(stepsX, stepsY)
    curr = (X[i], Y[i])
print ret
