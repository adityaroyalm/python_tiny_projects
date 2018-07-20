# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:59:19 2018

@author: aditya royal
"""
import pydicom
from matplotlib import pyplot as plt
from sklearn.preprocessing import normalize
import os
import math
y=list()
plan100=list()
plan=list()
import numpy as np
plan2=list()
plan0=list()
b=list()
plan5=list()
import pydicom.uid
ju='00cba091fa4ad62cc3200a657aeb957e'
for x in os.listdir('D:/lung cancer/sample_images/'+ju):
    plan.append(pydicom.read_file('D:/lung cancer/sample_images/'+ju+'/'+x).ImagePositionPatient)

    y.append(x)
    ds=pydicom.read_file('D:/lung cancer/sample_images/'+ju+'/'+x,force=True)
    dcmfile=ds
    j=0
    if j>0:
        dcmfile.SliceThickness=list(np.abs(np.array([0,0,dcmfile.SliceLocation],dtype=np.float)-previous))
            #print(10)
    else:
        dcmfile.SliceThickness=list(np.abs([0,0,dcmfile.SliceLocation]))
            #print(11)
    j=j+1
    previous=np.array([0,0,dcmfile.SliceLocation],dtype=np.float)
    ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian 
    #plan5.append(pydicom.read_file('D:/lung cancer/sample_images/'+ju+'/'+x).SliceThickness)
sor=sorted(plan,key=lambda x:x[2])
ran=[sor.index(x) for x in plan]
y=[y[x] for x in ran] 
import numpy as np
slices=list()
plan299=list()
from scipy.ndimage.interpolation import rotate 
from skimage import filters   
for x in y:
    plan0.append(pydicom.read_file('D:/lung cancer/sample_images/'+ju+'/'+x).pixel_array)
for x in y:
    plan2=pydicom.read_file('D:/lung cancer/sample_images/'+ju+'/'+x).ImageOrientationPatient
    plan299.append(pydicom.read_file('D:/lung cancer/sample_images/'+ju+'/'+x).SliceLocation)
    b=[math.acos(int(x))*180/math.pi for x in plan2]
    #sorted([dicom.read_file(BytesIO(dicom_file))],key=lambda x:x)
    plan3=pydicom.read_file('D:/lung cancer/sample_images/'+ju+'/'+x).pixel_array#fourd_array=plan.pixel_array
    n=rotate(np.expand_dims(plan3,axis=2),b[0],axes=(1,2))
    n=rotate(np.expand_dims(plan3,axis=2),b[1],axes=(2,0))
    plan3=rotate(np.expand_dims(plan3,axis=2),b[2],axes=(1,0))
    val=filters.threshold_otsu(plan3)
    mask=plan3>val
    plan3=mask*plan3
    plan3=np.squeeze(plan3,axis=2)
    plan3=normalize(plan3,axis=0)
    plan100.append(plan3)
    slices=np.stack([x for x in plan100],axis=2)
    plt.imshow(plan3.reshape((512,512)))
    plt.show()
    #i=i+1
from skimage import filters
fourd_array=slices
sorted(plan,key=lambda x: x[2]) 
import matplotlib as mat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#if i==3:
#print(dicom_file)

sum(plan3)
import scipy.ndimage
scipy.ndimage.zoom(plan3,2,order=3)
import keras.backend as back
count=0
def falsepositive(y_true,y_pred):
    if y_true==0 and y_pred==1:
        count=count+1
    return count
model.compile(loss=falsepositive)
fpr=falsepositive(y_true,y_pred)
from scipy import ndimage
distance=ndimage.distance_transform_edt(image)
peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=image)

