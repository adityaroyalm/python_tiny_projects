# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 19:56:56 2017

@author: aditya royal
"""

import numpy as np
print np.__version__
z=np.zeros(10)
z=np.arange(10,50)
Z=np.arange(50)
Z=Z[::-1]
z=np.arange(0,9).reshape((3,3))
z=np.eye(3)
print(z)
z=np.random.random((3,3,3))
print z.argmin()
print z.argmax()
z=np.random.random(30).mean()
z=np.ones((10,10))
z[1:-1,1:-1]=0
d=np.diag(np.arange(1,5),k=-1)
z=np.ones((10,10))
z[::2,::2]=0
z[1::2,1::2]=0
print np.unravel_index(100,(6,7,8))
z=np.tile(np.array([[0,1,0],[1,0,1]]),(4,4))
z=np.arange(11)
z[(3<z)&(z<8)]*=-1
z=np.random.uniform(-10,10,10)
np.trunc(z+np.copysign(0.5,z))
Z = np.zeros((5,5))
Z += np.arange(5)
print(Z)
