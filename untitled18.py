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
zz=np.tile(np.array([[0,0,1],[1,1,0],]),(4,4))
z=np.random.random((5,5))
z=(z-z.min())/(z.max()-z.min())
z=np.dot(np.ones((5,3)),np.ones((3,3)))
z=np.arange(1,15)
z[(3<z)&(z<8)]=-1
print(sum(range(5),-1))
#from numpy import *
#print np.array(0)//np.array(0.)
z= np.random.uniform(-10,+10,10)
print np.trunc(z+np.copysign(0.5,z))
z=np.random.uniform(0,10,10)
b=z-z%1
b=np.trunc(z)
b=np.floor(z)
b=z.astype(int)
z=np.zeros((5,5))
v=np.tile(np.array([[np.arange(1,5)],]),(4,1))
#z=z+np.tile(v,(5,5))
k=np.arange(5)
z=np.zeros((5,5))
z+=np.arange(1,6)
zzz=np.arange(5)
def generate():
    for x in xrange(10):
        yield x**x
z=np.fromiter(generate(),dtype=float)
z=np.linspace(1,10,5)
ran=np.random.random(10) 
print ran.sort()
z=np.arange(10)
np.add.reduce(z)
a=np.random.randint(0,2,5)
b=np.random.randint(0,2,5)
equal=np.allclose(a,b)
z=np.zeros(10)
#z.flags.writable=False
z[0]=1
z=np.random.random((10,2))
x,y=z[:,0],z[:,1]
r=np.sqrt(x**2+y**2)
maxi=np.random.random(10)
maxi[maxi.argmax()]=0
x=np.arange(8)
y=x+0.5
c=1/np.subtract.outer(x,y)
np.set_printoptions(threshold=np.nan)
Z = np.random.random((25,25))
print(Z)
z=np.arange(100)
v=np.random.uniform(0,100)
index=(np.abs(z-v)).argmin()