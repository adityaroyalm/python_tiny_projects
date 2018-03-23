# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:46:09 2017

@author: aditya royal
"""

A=[1,3,-1]
minimumm=float('inf')
import numpy as np
maximumm=float('-inf')

maxindex=sorted(range(len(A)),reverse=True,key=lambda x: A[x])
maximum=sorted(A,reverse=True)

minindex=sorted(range(len(A)),key=lambda x: A[x])
minimum=sorted(A)
    
l=0
m=0
maxi=float('-inf')
for l in range(len(A)):
    for m in range(len(A)):
        total=abs(maximum[l]-minimum[m])+abs(maxindex[l]-minindex[m])
        if total>maxi:
            maxi=total
print maxi

