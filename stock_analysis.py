# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:20:58 2018

@author: aditya royal
"""

import pandas_datareader as pdr
import datetime
import pandas as pd
import quandl
#aapl = pdr.get_data_yahoo('AAPL',start=datetime.datetime(2006, 10, 1),
                          #end=datetime.datetime(2012, 1, 1))
mydata=quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")
def get(tickers, startdate, enddate):
  def data(ticker):
    return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']
all_data = get(tickers, datetime.datetime(2006, 10, 1), datetime.datetime(2012, 1, 1))