# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:19:59 2018

@author: aditya royal
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from numpy import ones,vstack
from numpy.linalg import lstsq
d=list()
df=df=pd.read_csv('C:/Users/aditya royal/Desktop/cnt_km_year_powerPS_minPrice_maxPrice_avgPrice_sdPrice.csv')
x='minPrice'
y='maxPrice'
#=[x_max for index,x_max in enumerate(df.loc[:,x]) if x_max is max(df.loc[:,x])]
sum_columns=np.array(df.loc[:,x].values)+np.array(df.loc[:,y].values)
df.loc[:,'xy']=sum_columns
total_max=[(df.loc[index,'minPrice'],df.loc[index,'maxPrice']) for index,xy_max in enumerate(df.loc[:,'xy']) if xy_max == max(df.loc[:,'xy'])]
x_max=[(x_max,df.loc[index,'maxPrice']) for index,x_max in enumerate(df.loc[:,x]) if x_max == max(df.loc[:,x])]
y_max=[(df.loc[index,'minPrice'],y_max) for index,y_max in enumerate(df.loc[:,y]) if y_max == max(df.loc[:,y])]
total_min=[(df.loc[index,'minPrice'],df.loc[index,'maxPrice']) for index,xy_min in enumerate(df.loc[:,'xy']) if xy_min == min(df.loc[:,'xy'])]
#print(total_min,x_max,total_max,y_max)
#divide(df,'minPrice','maxPrice')
if x_max==total_max:
    x_max=y_max
mat1=np.zeros((3,3))
mat2=np.zeros((3,3))
mat3=np.zeros((3,3))
mat4=np.zeros((3,3))
mat1[:,0]=np.array([total_max[0][0]^2+total_max[0][1]^2,x_max[0][0]^2+x_max[0][1]^2,total_min[0][0]^2+total_min[0][1]^2])
mat1[:,1]=np.array([total_max[0][1],x_max[0][1],total_min[0][1]])
mat1[:,2]=np.ones(3)
mat2[:,0]=np.array([total_max[0][0],x_max[0][0],total_min[0][0]])
mat2[:,1]=np.array([total_max[0][1],x_max[0][1],total_min[0][1]])
mat2[:,2]=np.ones(3)
mat3[:,0]=np.array([total_max[0][0]^2+total_max[0][1]^2,x_max[0][0]^2+x_max[0][1]^2,total_min[0][0]^2+total_min[0][1]^2])
mat3[:,1]=np.array([total_max[0][0],x_max[0][0],total_min[0][0]])
mat3[:,2]=np.ones(3)
mat4[:,0]=np.array([total_max[0][0]^2+total_max[0][1]^2,x_max[0][0]^2+x_max[0][1]^2,total_min[0][0]^2+total_min[0][1]^2])
mat4[:,1]=np.array([total_max[0][0],x_max[0][0],total_min[0][0]])
mat4[:,2]=np.array([total_max[0][1],x_max[0][1],total_min[0][1]])
x0=0.5*(np.linalg.det(mat1))/(np.linalg.det(mat2))
y0=-0.5*(np.linalg.det(mat3))/(np.linalg.det(mat2))
mat4div2=(np.linalg.det(mat4))/(np.linalg.det(mat2))
r=np.sqrt((total_max[0][0]-x0)**2+(total_max[0][1]-y0)**2)
plt.scatter(df.loc[:,'minPrice'],df.loc[:,'maxPrice'])
circle=plt.Circle((x0,y0),fc='y',radius=r)
ax=plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
plt.show()
points = [total_max[0],(x0,y0)]
x_coords, y_coords = zip(*points)
A = vstack([x_coords,ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]
m2=-1/m
c2=y0-m2*x0
cli=list()
cli2=list()
for i in range(len(df.index)):
    cli.append(df.loc[i,'minPrice']-m*df.loc[i,'maxPrice'])
    cli2.append(df.loc[i,'minPrice']-m2*df.loc[i,'maxPrice'])
cli3=list(np.zeros(len(cli)))
num=0
for i in range(int(c-r),int(c+r),2*int(r)/3):
    num=0
    for k in cli:
        if k>i:
            cli3[num]=i
        num=num+1  
cli4=list(np.zeros(len(cli)))
for i in range(int(c2-r),int(c2+r),2*int(r)/3):
    num=0
    for k in cli2:
        if k>i:
            cli4[num]=i
        num=num+1 
df.loc[:,'cli3']=cli3
df.loc[:,'cli4']=cli4
#tup=list()
#for x in np.unique(cli3):
 #   for y in np.unique(cli4):
  #      tup.append((x,y))
indexes=list()
kk=[(x,y) for x,y in df.groupby(['cli3','cli4'])]

    