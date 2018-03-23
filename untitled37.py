# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:30:20 2017

@author: aditya royal
"""
A=[100,105,183,499]
#minimum=[0]*len(A)
#maximum=[0]*len(A)
total=[0]*len(A)
#minindex=[0]*len(A)
#maxindex=[0]*len(A)
minimumm=float('inf')
#maxindexx=
#minindexx=0
import numpy as np
maximumm=float('-inf')
#for l in range(len(A)):
maximum=sorted(A,reverse=True)
maxindex=sorted(range(len(A)),reverse=True,key=lambda x: A[x])
    #maximum[l]=maximumm
    #maxindex[l]=maxindexx
    
    
#for m in range(len(A)):    
#    for j in range(len(A)):
   #     if A[j]<minimumm:
minimum=sorted(A)
minindex=sorted(range(len(A)),key=lambda x: A[x])
            #minindexx=j
    #minindex[m]=minindexx
    #minimum[m]=minimumm
    
    
l=0
m=0
#total[0]=(maximum[0]-minimum[0])+abs(maxindex[0]-minindex[0])
for i in range(len(A)):
    total[i]=abs(maximum[l]-minimum[m])+abs(maxindex[l]-minindex[m])
    l=l+1
    m=m+1
print max(total)
    #if total[i]-total[i+1]>len(A)-1:
    #   break
    
 #return total[i]
            