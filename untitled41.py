# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:28:37 2017

@author: aditya royal
"""
A=[1,3,4,9,8,2,5,6,1]
sumOfA = 0
sumOfA2 = 0
n = 0
for a in A:
    sumOfA2 += a*a
    sumOfA += a
    n += 1
    sumOfN = n*(n+1)/2
    retA = sumOfN - sumOfA
    retB = (sumOfN*(2*n+1)/3 - sumOfA2)/retA
    x = (retB-retA)/2
    print [x,x + retA]