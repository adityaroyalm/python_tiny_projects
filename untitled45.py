# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 09:22:46 2017

@author: aditya royal
"""
A=5
def slopedownmatrix(x,a):
    for i in range(1,x+1):
        a[i-1]=[0]*i
        return a
slopedownmatrix(A,a)
k=0
a[-1][0]=0
a[-1][-1]=0
a[0][-1]=0
for i in range(5):
    for j in range(i+1):
        a[i][0]=1
        if j<k:
            a[i][j]=a[i-1][j]+a[i-1][j-1]
        a[i][k]=1
    k=k+1
print a