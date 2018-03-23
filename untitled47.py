# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:09:44 2017

@author: aditya royal
"""

A=9
c=[0]*A

k=0
for i in range(1,A+1):
    c[i-1]=[0]*i
      
            
      
            
#c[-1][0]=0
#c[-1][-1]=0
#c[0][-1]=0
   # a=[[0]*A for i in range(A)]
c[0][0]=1

for i in range(A):
    for j in range(i+1):
        c[i][0]=1
        if i>0 and j>0 and j<k:
            c[i][j]=c[i-1][j]+c[i-1][j-1]
        c[i][k]=1
    k=k+1
print c