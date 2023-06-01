# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:24:17 2023

@author: Shoeb
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series


s1 = Series(range(0,4))
s2 = Series(range(1,5))

type(s1) #pandas.core.series.Series


s3 = s1 + s2


s1 = Series(range(6))
s2 = s1*s1

s2.index = s2.index + 2

df = pd.concat([s1,s2], axis = 1 )

s3 = Series({"Tom":1,
             "Dick":2,
             "Har":3})

s4 = Series({"Tom":3,
             "Dick":4,
             "Mar":10})

df2 = pd.concat({"A":s3, "B":s4}, axis = 1)

#create a pyflake data
df = DataFrame(np.random.rand(50,5))

#Now timestamp as row index
df = DataFrame(np.random.rand(500,5))
# df.index = pd.date_range('1/1/2018', periods=len(df), freq="D")   #indexing by date wise increment
df.index = pd.date_range('1/1/2018', periods=len(df), freq="M")   #indexing by month wise increment

df.columns = ["A","B", "C", "D", "E"]

idx = df.columns #GET COLUMNS INDEX
L = df.columns.tolist() #getting columns in list format
a = df.columns.values  #getting columns in array formatr

df.index.is_monotonic_increasing
df.index.is_monotonic_decreasing
df.index.has_duplicates



























