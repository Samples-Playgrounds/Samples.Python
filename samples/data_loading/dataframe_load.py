# https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
# Load the Pandas libraries with alias 'pd' 

# pip install pandas
import pandas as pd


# Read data from file 'filename.csv' 
data = pd.read_csv("/Users/katodix/Projects/HolisticWare.Core.Math.Statistics.Descriptive.Sequential/externals/Core.Math.Samples/data/Pejcic_318.csv")

#show data
data

# ‘shape’ returns a tuple with the number of rows, and the number of columns for the data in the DataFrame
data.shape

# Preview the first 5 lines of the loaded data 
data.head

# variable names
data.columns

# variable data
print(data['ATV'])

data.describe()