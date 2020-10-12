#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
# Load the Pandas libraries with alias 'pd' 

# pip install wheel
# pip install pandas
# pip3 install wheel
# pip3 install pandas
# python -m pip install wheel
# python -m pip2 install pandas
# python2 -m pip2 install wheel
# python2 -m pip2 install pandas
# python3 -m pip3 install wheel
# python3 -m pip3 install pandas
# python3 -m pip install wheel
# python3 -m pip install pandas
import pandas as pd
import numpy as np


# Read data from file 'filename.csv' 
data = pd.read_csv("/Users/katodix/Projects/HolisticWare.Core.Math.Statistics.Descriptive.Sequential/externals/Core.Math.Samples/data/Pejcic_318.csv")

#show data
#data
print('DataFrame\n----------\n', data)

# ‘shape’ returns a tuple with the number of rows, and the number of columns for the data in the DataFrame
data.shape

# Preview the first 5 lines of the loaded data 
data.head(10)

data.tail(3)

data.dtypes

# variable names
data.columns

# variable data
print(data['ATV'])

data['MJESTO'].describe()
data['ATV'].describe()
data.describe()

#convert dataframe to numpy array (matrix)
arr = data.to_numpy()

print('\nNumpy Array\n----------\n', arr)
