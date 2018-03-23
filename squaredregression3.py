# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:19:59 2018

@author: aditya royal
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from numpy import ones,vstack
import sklearn

from numpy.linalg import lstsq
#from sklearn import datasets, linear_model
d=list()
n=6
df=df=pd.read_csv('y.csv')
x='num_critic_for_reviews'
y='duration'
#=[x_max for index,x_max in enumerate(df.loc[:,x]) if x_max is max(df.loc[:,x])]
sum_columns=np.array(df.loc[:,x].values)+np.array(df.loc[:,y].values)
df.loc[:,'xy']=sum_columns
total_max=[(df.loc[index,x],df.loc[index,y]) for index,xy_max in enumerate(df.loc[:,'xy']) if xy_max == max(df.loc[:,'xy'])]
x_max=[(x_max,df.loc[index,y]) for index,x_max in enumerate(df.loc[:,x]) if x_max == max(df.loc[:,x])]
y_max=[(df.loc[index,x],y_max) for index,y_max in enumerate(df.loc[:,y]) if y_max == max(df.loc[:,y])]
total_min=[(df.loc[index,x],df.loc[index,y]) for index,xy_min in enumerate(df.loc[:,'xy']) if xy_min == min(df.loc[:,'xy'])]
#print(total_min,x_max,total_max,y_max)
#divide(df,'minPrice','maxPrice')
if x_max==total_max:
    x_max=y_max
mat1=np.zeros((3,3))
mat2=np.zeros((3,3))
mat3=np.zeros((3,3))
mat4=np.zeros((3,3))
mat1[:,0]=np.array([total_max[0][0]**2+total_max[0][1]**2,x_max[0][0]**2+x_max[0][1]**2,total_min[0][0]**2+total_min[0][1]**2])
mat1[:,1]=np.array([total_max[0][1],x_max[0][1],total_min[0][1]])
mat1[:,2]=np.ones(3)
mat2[:,0]=np.array([total_max[0][0],x_max[0][0],total_min[0][0]])
mat2[:,1]=np.array([total_max[0][1],x_max[0][1],total_min[0][1]])
mat2[:,2]=np.ones(3)
mat3[:,0]=np.array([total_max[0][0]**2+total_max[0][1]**2,x_max[0][0]**2+x_max[0][1]**2,total_min[0][0]**2+total_min[0][1]**2])
mat3[:,1]=np.array([total_max[0][0],x_max[0][0],total_min[0][0]])
mat3[:,2]=np.ones(3)
mat4[:,0]=np.array([total_max[0][0]**2+total_max[0][1]**2,x_max[0][0]**2+x_max[0][1]**2,total_min[0][0]**2+total_min[0][1]**2])
mat4[:,1]=np.array([total_max[0][0],x_max[0][0],total_min[0][0]])
mat4[:,2]=np.array([total_max[0][1],x_max[0][1],total_min[0][1]])
x0=0.5*(np.linalg.det(mat1))/(np.linalg.det(mat2))
y0=-0.5*(np.linalg.det(mat3))/(np.linalg.det(mat2))
mat4div2=(np.linalg.det(mat4))/(np.linalg.det(mat2))
r=np.sqrt((total_max[0][0]-x0)**2+(total_max[0][1]-y0)**2)
plt.scatter(df.loc[:,x],df.loc[:,y])
#circle=plt.Circle((x0,y0),fc='y',radius=r)
#ax=plt.gca()
#ax.add_patch(circle)

#plt.show()
#points = [total_max[0],(x0,y0)]
#x_coords, y_coords = zip(*points)
#A = vstack([x_coords,ones(len(x_coords))]).T
#m, c = lstsq(A, y_coords)[0]
#m2=-1/m
#c2=y0-m2*x0
#cli=list()
#cli2=list()
#for i in range(len(df.index)):
#    cli.append(df.loc[i,x]-m*df.loc[i,y])
 #   cli2.append(df.loc[i,x]-m2*df.loc[i,y])
#cli3=list(np.zeros(len(cli)))
#num=0
#for i in range(int(c-r),int(c+r),2*int(r)/3):
 #   num=0
  #  for k in cli:
   #     if k>i:
    #        cli3[num]=i
     #   num=num+1  
#cli4=list(np.zeros(len(cli)))
#for i in range(int(c2-r),int(c2+r),2*int(r)/3):
 #   num=0
  #  for k in cli2:
   #     if k>i:
    #        cli4[num]=i
     #   num=num+1 
#df.loc[:,'cli3']=cli3
#df.loc[:,'cli4']=cli4
#tup=list()
#for x in np.unique(cli3):
 #   for y in np.unique(cli4):
  #      tup.append((x,y))
#indexes=list()
#kk=[(x,y) for x,y in df.groupby(['cli3','cli4'])]
# equation of circle
#(x-x0)**2+(y-y0)**2=r**2
li_x1=list()
li_y1=list()
li_x2=list()
li_y2=list()
li_x3=list()
li_y3=list()
li_x4=list()
li_y4=list()
li_x1=list()
li_y1=list()
li_x2=list()
li_y2=list()
li_x3=list()
li_y3=list()
li_x4=list()
li_y4=list()
li_x5=list()
li_y5=list()
li_x6=list()
li_y6=list()
li_x7=list()
li_y7=list()
li_x8=list()
li_y8=list()
li_x9=list()
li_y9=list()
li_x10=list()
li_y10=list()
li_x11=list()
li_y11=list()
li_x12=list()
li_y12=list()
li_x13=list()
li_y13=list()
li_x14=list()
li_y14=list()
li_x15=list()
li_y15=list()
li_x16=list()
li_y16=list()
li_x17=list()
li_y17=list()
li_x18=list()
li_y18=list()
li_x19=list()
li_y19=list()
li_x20=list()
li_y20=list()


for (x,y) in zip(df['num_critic_for_reviews'],df['duration']):
    if x>x0 and y>y0:
        li_x20.append(x)
        li_y20.append(y)
        if n>4:
            if x>x0+r/2 and y>y0+r/2:
                li_x1.append(x)
                li_y1.append(y)
            if x>x0+r/2 and y<y0+r/2:
                li_x2.append(x)
                li_y2.append(y)
            if x<x0+r/2 and y<y0+r/2:
                li_x3.append(x)
                li_y3.append(y)
            if x<x0+r/2 and y>y0+r/2:
                li_x4.append(x)
                li_y4.append(y)
    if x>x0 and y<y0:
        li_x19.append(x)
        li_y19.append(y)
        if n>4:
            if x>x0+r/2 and y>y0-r/2:
                li_x5.append(x)
                li_y5.append(y)
            if x>x0+r/2 and y<y0-r/2:
                li_x6.append(x)
                li_y6.append(y)
            if x<x0+r/2 and y<y0-r/2:
                li_x7.append(x)
                li_y7.append(y)
            if x<x0+r/2 and y>y0-r/2:
                li_x8.append(x)
                li_y8.append(y)
    if x<x0 and y<y0:
        li_x18.append(x)
        li_y18.append(y)
        if n>4:
            if x>x0-r/2 and y>y0-r/2:
                li_x9.append(x)
                li_y9.append(y)
            if x>x0-r/2 and y<y0-r/2:
                li_x10.append(x)
                li_y10.append(y)
            if x<x0-r/2 and y<y0-r/2:
                li_x11.append(x)
                li_y11.append(y)
            if x<x0-r/2 and y>y0-r/2:
                li_x12.append(x)
                li_y12.append(y)
    if x<x0 and y>y0:
        li_x17.append(x)
        li_x17.append(y)
        if n>4:
            if x>x0-r/2 and y>y0+r/2:
                li_x13.append(x)
                li_y13.append(y)
            if x>x0-r/2 and y<y0+r/2:
                li_x14.append(x)
                li_y14.append(y)
            if x<x0-r/2 and y<y0+r/2:
                li_x15.append(x)
                li_y15.append(y)
            if x<x0-r/2 and y>y0+r/2:
                li_x16.append(x)
                li_y16.append(y)   
from sklearn.linear_model import LinearRegression
regr =LinearRegression()
p=list()
try:
    model=regr.fit(np.array(li_x1).reshape(-1,1),np.array(li_y1).reshape(-1,1))
    predicted=model.predict(np.array(li_x1).reshape(-1,1))
    plt.plot(np.array(li_x1).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x2).reshape(-1,1),np.array(li_y2).reshape(-1,1))
    predicted=model.predict(np.array(li_x2).reshape(-1,1))
    plt.plot(np.array(li_x2).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x3).reshape(-1,1),np.array(li_y3).reshape(-1,1))
    predicted=model.predict(np.array(li_x3).reshape(-1,1))
    plt.plot(np.array(li_x3).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x4).reshape(-1,1),np.array(li_y4).reshape(-1,1))
    predicted=model.predict(np.array(li_x4).reshape(-1,1))
    plt.plot(np.array(li_x4).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x5).reshape(-1,1),np.array(li_y5).reshape(-1,1))
    predicted=model.predict(np.array(li_x5).reshape(-1,1))
    plt.plot(np.array(li_x5).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x6).reshape(-1,1),np.array(li_y6).reshape(-1,1))
    predicted=model.predict(np.array(li_x6).reshape(-1,1))
    plt.plot(np.array(li_x6).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x7).reshape(-1,1),np.array(li_y7).reshape(-1,1))
    predicted=model.predict(np.array(li_x7).reshape(-1,1))
    plt.plot(np.array(li_x7).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x8).reshape(-1,1),np.array(li_y8).reshape(-1,1))
    predicted=model.predict(np.array(li_x8).reshape(-1,1))
    plt.plot(np.array(li_x8).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x9).reshape(-1,1),np.array(li_y9).reshape(-1,1))
    predicted=model.predict(np.array(li_x9).reshape(-1,1))
    plt.plot(np.array(li_x10).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x11).reshape(-1,1),np.array(li_y11).reshape(-1,1))
    predicted=model.predict(np.array(li_x11).reshape(-1,1))
    plt.plot(np.array(li_x11).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x12).reshape(-1,1),np.array(li_y12).reshape(-1,1))
    predicted=model.predict(np.array(li_x12).reshape(-1,1))
    plt.plot(np.array(li_x12).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x13).reshape(-1,1),np.array(li_y13).reshape(-1,1))
    predicted=model.predict(np.array(li_x13).reshape(-1,1))
    plt.plot(np.array(li_x13).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x14).reshape(-1,1),np.array(li_y14).reshape(-1,1))
    predicted=model.predict(np.array(li_x14).reshape(-1,1))
    plt.plot(np.array(li_x14).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x15).reshape(-1,1),np.array(li_y15).reshape(-1,1))
    predicted=model.predict(np.array(li_x15).reshape(-1,1))
    plt.plot(np.array(li_x15).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x16).reshape(-1,1),np.array(li_y16).reshape(-1,1))
    predicted=model.predict(np.array(li_x16).reshape(-1,1))
    plt.plot(np.array(li_x16).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x17).reshape(-1,1),np.array(li_y17).reshape(-1,1))
    predicted=model.predict(np.array(li_x16).reshape(-1,1))
    plt.plot(np.array(li_x17).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x18).reshape(-1,1),np.array(li_y18).reshape(-1,1))
    predicted=model.predict(np.array(li_x16).reshape(-1,1))
    plt.plot(np.array(li_x18).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x19).reshape(-1,1),np.array(li_y19).reshape(-1,1))
    predicted=model.predict(np.array(li_x19).reshape(-1,1))
    plt.plot(np.array(li_x19).reshape(-1,1),predicted)
except:
    pass
try:
    model=regr.fit(np.array(li_x20).reshape(-1,1),np.array(li_y20).reshape(-1,1))
    predicted=model.predict(np.array(li_x20).reshape(-1,1))
    plt.plot(np.array(li_x20).reshape(-1,1),predicted)
except:
    pass
plt.show()
