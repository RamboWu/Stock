#  -*- coding: utf-8 -*-
#!/usr/bin/python

'''
from yahoo_finance import Share
from matplotlib import pylab
import numpy as np
import pandas as pd
import DataAPI
import seaborn as sns
sns.set_style('white')

yahoo = Share('YHOO')
print( yahoo.get_historical('2016-06-25', '2016-07-27') )
'''
import pandas_datareader.data as web
import datetime
import requests_cache

expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

start = datetime.datetime(2013, 1, 1)
end = datetime.datetime(2016, 1, 27)
df = web.DataReader("GOOGL", 'yahoo', start, end, session=session)

dates =[]
for x in range(len(df)):
    newdate = str(df.index[x])
    newdate = newdate[0:10]
    dates.append(newdate)

df['dates'] = dates

print(df.head())
print(df.tail())
