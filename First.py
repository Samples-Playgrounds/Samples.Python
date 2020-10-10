# pip install pandas
# Load the Pandas libraries with alias 'pd' 
import pandas as pd

# pip install pandas

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("Babies.csv")

# Preview the first 5 lines of the loaded data 
data.head()

#show data
data

# matrix shape
data.shape

#variable names
data.columns

# variable data
print(data['Age'])

data.describe()