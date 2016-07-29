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

start = datetime.datetime(2005, 1, 1)
end = time.strftime( '%Y-%m-%d', time.localtime() )
df = web.DataReader("000001.ss", 'yahoo', start, end, session=session)

window_short = 20
window_long = 120
SD = 0.05

df['short_window'] = np.round(df['Adj Close'].rolling(window=window_short,center=False).mean(), 4)
df['long_window'] = np.round(df['Adj Close'].rolling(window=window_long,center=False).mean(), 4)
df['s-l'] = df['short_window'] - df['long_window']
df['Regime'] = np.where(df['s-l'] > df['long_window'] * SD, 1, 0)
print(df['Regime'].value_counts())
print(df[['Adj Close', 'short_window', 'long_window', 's-l']].tail())

df[['Adj Close', 'short_window', 'long_window']].plot(grid=False, figsize=(12,8))
#sns.plt.show()

df['Regime'].plot(grid=False, lw=1.5, figsize=(12,8))
pylab.ylim((-0.1,1.1))
#sns.plt.show()

df['Market'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))
df['Strategy'] = df['Regime'].shift(1) * df['Market']
print(df[['Market', 'Strategy', 'Regime']].tail())
