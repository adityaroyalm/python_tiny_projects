# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:06:49 2017

@author: aditya royal
"""
A=[1,2,3,-3,-3,-5,40,-3]
max_ending_here = 0
start_ending_here = 0
end_ending_here = 0
max_so_far = 0
start_so_far = 0
end_so_far = 0
allNegative = True
n = len(A)
if n == 0:
    print []
for i in range(n):
    if A[i] >= 0:
        allNegative = False
    if max_ending_here + A[i] >= max_ending_here:
        max_ending_here += A[i]
        end_ending_here = i
    else:
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start_so_far = start_ending_here
            end_so_far = end_ending_here
        elif max_so_far <= max_ending_here:
            if end_ending_here - start_ending_here > end_so_far - start_so_far:
                max_so_far = max_ending_here
                start_so_far = start_ending_here
                end_so_far = end_ending_here
        max_ending_here = 0
        start_ending_here = i+1
        
    
if max_so_far < max_ending_here:
    max_so_far = max_ending_here
    start_so_far = start_ending_here
    end_so_far = end_ending_here
elif max_so_far <= max_ending_here:
    if end_ending_here - start_ending_here > end_so_far - start_so_far:
        max_so_far = max_ending_here
        start_so_far = start_ending_here
        end_so_far = end_ending_here
if allNegative:
    print []
else:
    print A[start_so_far:end_so_far+1]

