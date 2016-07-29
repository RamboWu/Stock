#  -*- coding: utf-8 -*-
#!/usr/bin/python

import pandas_datareader.data as web
import datetime
import time
import requests_cache
import seaborn as sns
import numpy as np
from matplotlib import pylab
import pandas as pd

expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

start = datetime.datetime(2013, 1, 1)
end = time.strftime( '%Y-%m-%d', time.localtime() )
df = web.DataReader("GOOGL", 'yahoo', start, end, session=session)

dates =[]
for x in range(len(df)):
    newdate = str(df.index[x])
    newdate = newdate[0:10]
    dates.append(newdate)

df['dates'] = dates

print(df['Adj Close'].tail())

df['Adj Close'].plot(grid=False, figsize=(12,8))
sns.plt.show()
#print(df.head())
#print(df.tail())
