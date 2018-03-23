# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:43:49 2017

@author: aditya royal
"""
a=[[1,2,3],[3,2,4],[3,5,2]]
C=len(a[0])
R=len(a)
c=0
A=[[0]*(C) for i in range(C+1)]
r=0
c=0
if c!=C:
    
    for i in range(1,C+1):
        r=0
        c=c+1
        for j in range(i):
            A[i-1][j]=a[r+j-1][c-j]
#else:
    
 #   for i in range(C+1,2*C):
  #      r=r+1
   #     c=0
    #    w=range(R-1)
     #   for j in w[::-1]:
      #      A[i][j]=a[r+j][C-j]