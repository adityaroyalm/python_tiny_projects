# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:07:22 2018

@author: aditya royal
"""
from crontab import CronTab
job = my_cron.new(command='~/facebook3.py')
job.minute.every(1)
my_cron.write()