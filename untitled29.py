# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:53:47 2017

@author: aditya royal
"""
a=[1]
b=1
ret=[]
if len(a)==1:
    return a

for i in xrange(len(a)):
    ret.append(a[i + b])
    if i+b+1==len(a):
        break
for i in range(b):
    ret.append(a[i])