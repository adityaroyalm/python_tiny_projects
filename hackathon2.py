# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:08:18 2017

@author: aditya royal
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
train_data=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\Day5\train_ysMSKmQ (1).csv') 
test_data=pd.read_csv(r'C:\Users\aditya royal\Desktop\hackathon\Day5\test_uLBXQQR.csv')
lin=LinearRegression()
X = train_data[['instant', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday',
       'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed']]
y = train_data[['cnt']]
X_test=X_test = test_data[['instant', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday',
       'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed']]
lin.fit(X,y)
lin.coef_
lin.intercept_
predictions=lin.predict(X_test)
#train_data.hist(column='cnt')
import numpy as np
#train_data.cnt.hist()
#np.log(train_data.cnt).hist()
np.sqrt(train_data.cnt).hist()
return_type='dict'
train_data.boxplot(column='temp')
train_data['temp_bins']=pd.cut(train_data.temp,[0,0.3,0.7,1],labels=['Low','Average','High'])
train_data['su']=train_data.groupby('hr')['cnt'].sum().plot.bar()
train_data.groupby('weekday').median().cnt.plot.bar()
# define label encoder
from sklearn.preprocessing import LabelEncoder
lb_temp = LabelEncoder()

# replace the temp bins column
train_data['temp_bins'] = lb_temp.fit_transform(train_data.temp_bins)
train_data['hr_bins'] = pd.cut(train_data.hr, [-1, 6, 9, 15, 20, 24], labels=['Late_Night', 'Office_Going', 'Mid_Day', 'Office_Returning', 'Night'])

lb_hr=LabelEncoder()
train_data['hr_bins']=lb_hr.fit_transform(train_data.hr_bins)
df=pd.cut(train_data.atemp,[0,0.3,0.7,1],labels=['atemp_low','atemp_avg','atemp_high'])
df=pd.get_dummies(df)
train_data['weekend'] = ((train_data.holiday == 0) & (train_data.workingday == 0)).astype(int)
pd.concat([train_data,df],axis=1)
train_data.corr()[((train_data.corr()<-0.85)|(train_data.corr()>0.85))&(train_data.corr()!=1)]
train_data=train_data.drop(['temp'],axis=1)
train_data=train_data.drop('instant',axis=1)
train_data = train_data[['season', 'hr', 'mnth', 'weekend', 'yr', 'weathersit', 'temp_bins', 
               'hum', 'windspeed', 'atemp', 'hr_bins', 'cnt']]
X=train_data.drop('cnt',axis=1)
y=train_data['cnt']


# step 2
test_data['temp_bins'] = pd.cut(test_data.temp, [0, 0.3, 0.7, 1], labels=['Low', 'Average', 'High'])
test_data['hr_bins'] = pd.cut(test_data.hr, [-1, 6, 9, 15, 20, 24], labels=['Late_Night', 'Office_Going', 'Mid_Day', 'Office_Returning', 'Night'])

# step 3
## Note: we have already trained our label encoder, so no need to train again. 
## Therefore we use lb.transform instead of lb.fit_transform function
test_data['temp_bins'] = lb_temp.transform(test_data.temp_bins)
test_data['hr_bins'] = lb_hr.transform(test_data.hr_bins)
df = pd.cut(test_data.atemp, [0, 0.3, 0.7, 1], labels=['atemp_low', 'atemp_avg', 'atemp_high'])
dummy = pd.get_dummies(df)
test_data = pd.concat([test_data, dummy], axis=1)
test_data['weekend'] = ((test_data.holiday == 0) & (test_data.workingday == 0)).astype(int)
# step 5
test_data = test_data[['season', 'hr', 'mnth', 'weekend', 'yr', 'weathersit', 'temp_bins', 'hum', 'windspeed', 'atemp', 'hr_bins']]

X_test_data = test_data#.drop([ 'temp_bins'], axis=1)
lin=LinearRegression()
lin.fit(X,y)
predictions=lin.predict(X_test_data)
