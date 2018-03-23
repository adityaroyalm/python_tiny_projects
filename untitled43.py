# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:26:19 2017

@author: aditya royal
"""
A=[1,2,3]
present=0
high=0
endpresent=0
startpresent=0
starthigh=0
endhigh=0

for num in range(len(A)):
    if num >0:
        present=present+A[num]
        
        endpresent=num
        
    else:
                
                
        if present>high:
            high=present
            
            endhigh=endpresent
            starthigh=startpresent
                
        startpresent=num+1
        present=0
if present>high:
    high=present
    
    endhigh=endpresent
    starthigh=startpresent
        
print A[starthigh:endhigh+1]