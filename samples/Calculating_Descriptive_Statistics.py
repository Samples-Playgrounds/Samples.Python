#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://realpython.com/python-statistics/

#import math
#import statistics
#import numpy as np
#import scipy.stats
import pandas as pd

data = pd.read_csv("/Users/katodix/Projects/HolisticWare.Core.Math.Statistics.Descriptive.Sequential/externals/Core.Math.Samples/data/Pejcic_318.csv")

data['ATV'].mean()
data.mean()


statistics.mean(data['ATV'])
statistics.harmonic_mean(data['ATV'])
statistics.geometric_mean(data['ATV'])
