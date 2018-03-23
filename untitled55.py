# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 08:41:14 2017

@author: aditya royal
"""
import pandas as pd
new_contract=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Train_BG1IL20\Train\Contracts_New.csv')
end_contract=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Train_BG1IL20\Train\Contracts_End.csv')
pre_contacts=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Train_BG1IL20\Train\Contacts_Pre_2017.csv')
pre_resolutions=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\mlfest\Train_BG1IL20\Train\Resolution_Pre_2017.csv')
##knearest neighbours#
from sklearn import neighbors
n_neighbors=5
for i,weights in enumerate(['uniform','distance']):
    knn=neighbors.KNeighborsRegressor(n_neighbors,weights=weights)
    y_=knn.fit().predict()