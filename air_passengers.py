# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:14:47 2017

@author: aditya royal
"""
import pandas as pd
import numpy as np
dateparser=lambda dates: pd.datetime.strptime(dates,'%Y-%m')
data=pd.read_csv('C:/Users/aditya royal/Desktop/AirPassengers.csv',parse_dates=['Month'],index_col='Month',date_parser=dateparser)
ts = data.iloc[:,0]
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    #determinig rolling statistics
    rolmean=pd.rolling_mean(timeseries,window=12)
    rolstd=pd.rolling_std(timeseries,window=12)
    #plotting rolling statistics
    orig=plt.plot(timeseries,color='blue',label='original')
    mean=plt.plot(rolmean,color='red',label='rolling mean')
    std=plt.plot(rolstd,color='yellow',label='rolstd')
    #perform dikey-fuller test
    dftest=adfuller(timeseries,autolag='AIC')
    dfoutput=pd.Series(dftest[0:4],index=['Test Statistc','p-value','#lags used','number of observations'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print dfoutput
test_stationarity(ts)
plt.show()
plt.plot(np.log(ts))
moving_avg=pd.rolling_mean(np.log(ts),12)
plt.plot(moving_avg)
ts_log_moving_avg_diff=np.log(ts)-moving_avg
plt.show()
plt.plot(ts_log_moving_avg_diff)
ts_log_moving_avg_diff.dropna(inplace=True)
test_stationarity(ts_log_moving_avg_diff)
expwmavg=pd.ewma(np.log(ts),halflife=12)
ts_log_expwmavg=np.log(ts)-expwmavg
plt.show()
test_stationarity(ts_log_expwmavg)
plt.plot(ts_log_expwmavg)
plt.show()
plt.plot(np.log(ts)-np.log(ts).shift())

from statsmodels.tsa.seasonal import seasonal_decompose
decomposition=seasonal_decompose(np.log(ts))
trend=decomposition.trend
seasonal=decomposition.seasonal
resid=decomposition.resid

plt.show()
plt.plot(trend)
plt.show()
plt.plot(seasonal)
plt.show()
plt.plot(resid)
