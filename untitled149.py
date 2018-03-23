# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:04:08 2018

@author: aditya royal
"""

import numpy as np
two_darray=np.array(([[1,2,3,4],[9,8,7,6]],[[5,9,0,9],[8,4,2,9]]))
from scipy.ndimage import interpolation
g=interpolation.rotate(two_darray,170,axes=(2,0),reshape=False)
j=interpolation.rotate(g,190,axes=(2,0),reshape=False)
#h=interpolation.rotate(g,180,axes=(0,1))
#i=interpolation.rotate(h,10,axes=(1,2))