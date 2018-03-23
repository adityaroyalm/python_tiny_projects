# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 16:43:49 2017

@author: aditya royal
"""
import numpy as np
print(np.__version__)
np.zeros(10)
z=np.arange(50)
z=np.arange(9).reshape(3,3)
nz=np.array([1,2,3,0,9,0,8,0,0])
nz=np.nonzero(nz)
#print nz
np.eye(3)
z=np.random.random((3,3))
zz=np.argmin(z)
z=np.zeros((4,4))
z=np.diag(1+np.arange(4),k=-1)
z=np.ones((8,8))
z[::2,:-1:2]=0
z[1::2,1::2]=0
z=np.ones((100,100))
np.unravel_index(100,(100,100))
np.tile(np.array([[0,1],[1,0]]),(4,4))
k=np.dot(z,z)
z=np.random.random((4,4))
np.trunc(z+np.copysign(0.5,z))
z=np.random.uniform(1,10,10)
z=z.astype(np.int,copy=False)
#for index,value in np.ndenumerate(z):
 #   print(index,value)
z = np.random.randint(0,10,(10,10))
z=z[z[:,0].argsort()]
z= np.random.randint(0,3,(3,10))
#print (~z.any(axis=0)).any()
Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
#print(Z)
#z=np.genfromtxt("missing.dat",delimiter=",")
for index,value in np.ndenumerate(z):
    print index,z[index]
x=np.random.rand(5,10)
y=x-x.mean(axis=1,keepdims=True)
j=x[x[:,1].argsort(),]

#print (~x.any(axis=0)).any()
#class NamedArray(np.ndarray):
 #   def __new__(cls,array,name="no name"):
      #  obj=np.asarray(array).view(cls)
     #   obj.name=name
    #    return obj
   # def __array_finalize__(self,obj):
  #      if obj is None: return
 #       self.info = getattr(obj,'name',"no name")
#z= NamedArray(np.arange(10),"range_10")
#print z.name
#xz=np.ones(10)
#I=np.random.randint(0,len(xz),20)
#xz+=np.bincount(I,minlength=len(xz))
a=np.random.randint(0,10,(3,4,4))
sum=a.shape[:-2]+(-1,)
x=[1,2,3,4,5,6]
I=[1,3,9,3,4,1]
F=np.bincount(I,x)
c=np.bincount([1,1,2,3,10,10,6])
a=np.repeat(np.arange(len(c)),c)
def moving_average(a,n=3):
    ret=np.cumsum(a,dtype=float)
    