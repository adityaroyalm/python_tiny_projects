# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:47:09 2017

@author: aditya royal
"""

import numpy as np
A=[[1,2,3],[2,3,82],[732,4,0],[25,0,2]]
j=0
j=0
m=len(A)
n=len(A[0])
if m>n:
    z=n/2
else:
    z=m/2
k=z +1- (z)%1
p=[]
for i in range(k/2):
    p.append(A[i][j:(n-j)])
    p.append(A[(1+i):(m-i)][n-1-j])
    p.append(A[m-1-i][j:(n-1-j)][::-1])
    p.append(A[(i+1):(m-1-i)][j][::-1])
    j=j+1
print [element for array in p for element in array ]
