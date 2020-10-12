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
data_frame = pd.read_csv("../../externals/Core.Math.Data/data/Pejcic_318.csv")

# show data
# data
print('DataFrame\n----------\n', data_frame)

# ‘shape’ returns a tuple with the number of rows, and the number of columns for the data in the DataFrame
data_frame.shape

# Preview the first 5 lines of the loaded data 
data_frame.head(10)

data_frame.tail(3)

data_frame.dtypes

# variable names
data_frame.columns

# variable data
print(data_frame['ATV'])

data_frame['MJESTO'].describe()
data_frame['ATV'].describe()
data_frame.describe()

#convert dataframe to numpy array (matrix)
arr = data_frame.to_numpy()

print('\nNumpy Array\n----------\n', arr)
