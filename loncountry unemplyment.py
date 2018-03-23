# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:44:40 2017

@author: aditya royal
"""

country=pd.read_csv(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects\country unemployment\API_ILO_country_YU.csv')
country.head()
country_list=list(country.ix[:,'Country Name'].unique())
trace1=