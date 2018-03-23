# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:15:33 2017

@author: aditya royal
"""

af=0
a=[0]*(A+1)
def summ(A,a):
    a=[0]*(A+1)
    
    a[0][0]=1
    for i in range(1,A):
        a[A-i+1][0]=a[A-i+1][A-i+1]=1
        if A-i>=2:
            a[A][i]=a[A-1][i-1]+a[A-1][i]+summ(A-i,a)
            a[1][0]=a[1][1]=1
            return a[A][i]
        af=af+1
    return a
summ(6,a)