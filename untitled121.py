# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:57:09 2018

@author: aditya royal
"""
li=list()
di=dict()
li2=list()
tu=tuple()
for x in range(1,20):
    li.append(x)
    li2.append(x*2)
di=dict(zip(li,li2))
a='abcde'
for x in range(len(a),0,-1):
    print(a[:x])
    
    
    