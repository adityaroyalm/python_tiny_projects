# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:31:08 2017

@author: aditya royal
"""
A=[3,2,1,5,9,8,6,7,7]
A=sorted(A)
n=range(1,len(A)+1)
diff=[i-j for i,j in zip(A,n)]
for i in range(1,len(A)):
    if diff[i]-diff[i-1]<0:
        break
ones=sum(diff)      
a= A[i]
b= A[i]-ones
c=[0]*2
c=[a,b]
print c