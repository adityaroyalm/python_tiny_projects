# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:37:26 2017

@author: aditya royal
"""

def pascal_row(n):
    row = [1]

    for col in range(1, n):
        row.append(row[-1] * (n - col) / col)

    return row
print pascal_row(6)