# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 20:29:23 2017

@author: aditya royal
"""
a=3

T=0
B=a
R1=a
L=0
r=0
R=a
C=a
n=a
c=0
A=[[0]*a for i in range(a)]
while T<=B and R1>=L:
    A[0][0]=1
    for i in range(c,C):
       
        A[r][i]=num
        r=r+1
        num+=1
        T+=1
        
    
            
    for j in range(r,R):
        A[j][C]=num
        C=C-1
        num+=1
        R1-=1
      
    for k in range(C,c-1,-1):
        A[R][k]=num
        R=R-1
        num+=1
        B-=1
               
    for l in range(R,r-2,-1):
        A[l][c+m]=num
        c=c+1
        num+=1
        R+=1