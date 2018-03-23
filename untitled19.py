# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 12:45:42 2017

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 11:05:34 2017

@author: aditya royal
"""

import numpy as np
print(np.__version__)
z=np.zeros
z=np.arange(10,50)
z=np.arange(0,9).reshape(3,3)
z=np.nonzero(z)
z=np.eye(3)
z=np.random.random(100).reshape(10,10)
z.min()
z.max()
z=np.random.random(30)
m=np.random.random((10,10,10))
z=np.ones((10,10))
z[1:-1,1:-1]=0
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 * 0.1
z=np.diag(1+np.arange(4),k=-1)
z=np.zeros((8,8))
z[1::2,::2]=1
z[::2,1::2]=1
z=np.zeros((6,7,8))
print np.unravel_index(100,(6,7,8))
z=np.tile(np.array([[0,0,1],[1,1,0],]),(4,4))
z=np.random.random((5,5))
z=(z-z.min())/(z.max()-z.min())
z=np.dot(np.ones((5,3)),np.ones((3,3)))
z=np.arange(1,15)
z[(3<z)&(z<8)]=-1
print(sum(range(5),-1))
#from numpy import *
print(sum(range(5),-1))