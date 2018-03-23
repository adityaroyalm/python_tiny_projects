# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:01:13 2017

@author: aditya royal
"""
A=[9,9,4,5,3,3,6,7,4,2,5,6,6,3,5,3]
n=len(A)


nums=0
for i in range(n):
    nums=nums+(A[n-1-i]*(10**i))
nums=nums+1
nums=long(nums)
for i in range(1,20):
    if (long(nums)/(10**i))==0:
        break

count=i
vec=[0]*count
for i in range(1,count+1):
    vec[count-i]=(nums%(10**i))/(10**(i-1))
print vec