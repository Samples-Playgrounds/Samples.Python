# pip install pandas
# Load the Pandas libraries with alias 'pd' 
import pandas as pd

# pip install pandas

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("/Users/katodix/Projects/HolisticWare.Core.Math.Statistics.Descriptive.Sequential/externals/Core.Math.Samples/data/Pejcic_318.csv")

# df=DataFrame()
# df.read_tbl("/Users/katodix/Projects/HolisticWare.Core.Math.Statistics.Descriptive.Sequential/externals/Core.Math.Samples/data/Pejcic_318.csv")                   

# Preview the first 5 lines of the loaded data 
data.head()

#show data
data

# matrix shape
data.shape

#variable names
data.columns

# variable data
print(data['SPOL'])

data.describe()