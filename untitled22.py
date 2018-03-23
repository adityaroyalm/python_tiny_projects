# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:31:13 2017

@author: aditya royal
"""
import IPython.nbformat.current as nbf
nb = nbf.read(open('lonallstateclaim.py', 'r'), 'py')
nbf.write(nb, open('lonalstateclaimm.ipynb', 'w'), 'ipynb')