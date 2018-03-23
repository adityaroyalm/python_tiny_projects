# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:08:59 2017

@author: aditya royal
"""
A=7
A += 1
ret = []
if A == 0:
    print ret
ret = [[1]]
for i in range(2,A+1):
    ret.append([0]*i)
    ret[i-1][0] = 1
    ret[i-1][-1] = 1
    for j in range(1,i-1):
        ret[i-1][j] = ret[i-2][j-1]+ret[i-2][j]
print ret[-1]