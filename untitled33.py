# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:13:26 2017

@author: aditya royal
"""
X=[-7,-13]
Y=[1,-5]
a=0
ret=0
b=0
for i in range(len(X)-1):
    a=abs(X[i]-X[i+1])
    b=abs(Y[i]-Y[i+1])
    ret=ret+ max(a,b)
print ret
            