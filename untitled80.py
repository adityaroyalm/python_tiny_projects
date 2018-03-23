# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 10:06:24 2017

@author: aditya royal
"""
import plotly.offline as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
from plotly.graph_objs import Scatter,Figure,Layout
plot([Scatter(x=[1,2,3],y=[3,1,6])])
