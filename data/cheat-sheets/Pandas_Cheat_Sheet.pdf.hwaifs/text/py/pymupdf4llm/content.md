### **Data Wrangling**
##### with pandas Cheat Sheet http://pandas.pydata.org

[Pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api) [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide)



Each **variable** is saved
in its own **column**


#### Tidy Data – A foundation for wrangling in pandas



Each **observation** is
saved in its own **row**



In a tidy
data set:



Tidy data complements pandas’s **vectorized**
**operations** . pandas will automatically preserve
## `*`
observations as you manipulate variables. No
other format works as intuitively with pandas.


### `M A`





|Col1|a|b|c|
|---|---|---|---|
|**1**|4|7|10|
|**2**|5|8|11|
|**3**|6|9|12|

```
df = pd.DataFrame(
{"a" : [4, 5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])
```

Specify values for each column.

```
df = pd.DataFrame(
[[4, 7, 10],
[5, 8, 11],
[6, 9, 12]],
index=[1, 2, 3],
columns=['a', 'b', 'c'])
```

Specify values for each row.



















|Col1|Col2|a|b|c|
|---|---|---|---|---|
|**N**|**v**||||
|**D**|**1**|4|7|10|
|**D**|**2**|5|8|11|
|**e**|**2**|6|9|12|

```
df = pd.DataFrame(
{"a" : [4,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = pd.MultiIndex.from_tuples(
[('d', 1), ('d', 2),
('e', 2)], names=['n', 'v']))
```

Create DataFrame with a MultiIndex


```
df[df.Length > 7]
```

Extract rows that meet logical criteria.
```
df.drop_duplicates()
```

Remove duplicate rows (only considers columns).
```
df.sample(frac=0.5)
```

Randomly select fraction of rows.
**`[df.sample(n=10)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html?highlight=sample#pandas.DataFrame.sample)`** Randomly select n rows.
```
df.nlargest(n, 'value')
```

Select and order top n entries.
```
df.nsmallest(n, 'value')
```

Select and order bottom n entries.
```
df.head(n)
```

Select first n rows.
```
df.tail(n)
```

Select last n rows.


```
df[['width', 'length', 'species']]
```

Select multiple columns with specific names.
**`df['width']`** _or_ **`df.width`**
Select single column with specific name.
```
df.filter(regex=' regex ')
```

Select columns whose name matches
regular expression _regex_ .



query() allows Boolean expressions for filtering
rows.
```
df.query('Length > 7')
df.query('Length > 7 and Width < 8')
df.query('Name.str.startswith("abc")',
     engine="python")

```




Use **`df.loc[]`** and **`df.iloc[]`** to select only
rows, only columns or both.
Use **`df.at[]`** and **`df.iat[]`** to access a single
value by row and column.
First index selects rows, second index columns.

```
df.iloc[10:20]
```

Select rows 10-20.
```
df.iloc[:, [1, 2, 5]]
```

Select columns in positions 1, 2 and 5 (first

column is 0).
```
df.loc[:, 'x2':'x4']
```

Select all columns between x2 and x4 (inclusive).
```
df.loc[df['a'] > 10, ['a', 'c']]
```

Select rows meeting logical condition, and only

the specific columns .
**`[df.iat[1, 2]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat)`** Access single value by index
**`[df.at[4, 'A']](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at)`** Access single value by label




|Logic in Python (and pandas)|Col2|Col3|Col4|
|---|---|---|---|
|**`<`**|Less than|**`!=`**|Not equal to|
|**`>`**|Greater than|**`df.column.isin(`****_`values`_****`)`**|Group membership|
|**`==`**|Equals|**`pd.isnull(`****_`obj`_****`)`**|Is NaN|
|**`<=`**|Less than or equals|**`pd.notnull(`****_`obj`_****`)`**|Is not NaN|
|**`>=`**|Greater than or equals|**`&,|,~,^,df.any(),df.all()`**|Logical and, or, not, xor, any, all|


|regex (Regular Expressions) Examples|Col2|
|---|---|
|**`'\.'`**|Matches strings containing a period '.'|
|**`'Length$'`**|Matches strings ending with word 'Length'|
|**`'^Sepal'`**|Matches strings beginning with the word 'Sepal'|
|**`'^x[1-5]$'`**|Matches strings beginning with 'x' and ending with 1,2,3,4,5|
|**`'^(?!Species$).*'`**|Matches strings except the string 'Species'|



[Cheatsheet for pandas (http://pandas.pydata.org/ originally written by Irv Lustig,](http://pandas.pydata.org/) [Princeton Consultants, inspired by](http://www.princetonoptimization.com/) [Rstudio Data Wrangling Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf)






### **Combine Data Sets**
```
 adf bdf

```










|x1|x2|
|---|---|
|**A**|<br>**1**|
|**B**|**2**|
|**C**|**3**|


Standard Joins


|x1|x3|
|---|---|
|<br>**A**|<br>**T**|
|**B**|**F**|
|**D**|**T**|








```
pd.merge(adf, bdf,
how='left', on='x1')
```

Join matching rows from bdf to adf.

```
pd.merge(adf, bdf,
how='right', on='x1')
```

Join matching rows from adf to bdf.

```
pd.merge(adf, bdf,
how='inner', on='x1')
```

Join data. Retain only rows in both sets.

```
pd.merge(adf, bdf,
how='outer', on='x1')
```

Join data. Retain all values, all rows.

```
adf[~adf.x1.isin(bdf.x1)]
```

All rows in adf that do not have a match in bdf.


|x1|x2|x3|
|---|---|---|
|**A**|**1**|**T**|
|**B**|**2**|**F**|
|**C**|**3**|**NaN**|






### **Summarize Data**

```
df['w'].value_counts()
```

Count number of rows with each unique value of variable
```
len(df)
```

# of rows in DataFrame.
```
df.shape
```

Tuple of # of rows, # of columns in DataFrame.
```
df['w'].nunique()
```

# of distinct values in a column.
```
df.describe()
```

Basic descriptive and statistics for each column (or GroupBy).
```
df.info()
```

Prints a concise summary of the DataFrame.
```
df.memory_usage()
```

Prints the memory usage of each column in the DataFrame.
```
df.dtypes()
```

Prints a Series with the dtype of each column in the DataFrame.


pandas provides a large set of **[summary functions](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#descriptive-statistics)** that operate on
different kinds of pandas objects (DataFrame columns, Series,
GroupBy, Expanding and Rolling (see below)) and produce single
values for each of the groups. When applied to a DataFrame, the
result is returned as a pandas Series for each column. Examples:
```
sum() min()

```

### **Handling Missing Data**

```
df.dropna()
```

Drop rows with any column having NA/null data.
```
df.fillna(value)
```

Replace all NA/null data with value.
### **Make New Columns**

```
df.assign(Area=lambda df: df.Length*df.Height)
```

Compute and append one or more new columns.
```
df['Volume'] = df.Length*df.Height*df.Depth
```

Add single column.
```
pd.qcut(df.col, n, labels=False)
```

Bin column into n buckets.


pandas provides a large set of **vector functions** that operate on all
columns of a DataFrame or a single selected column (a pandas
Series). These functions produce vectors of values for each of the
columns, or a single Series for the individual Series. Examples:


|x1|x2|x3|
|---|---|---|
|**A**|**1.0**|**T**|
|**B**|**2.0**|**F**|
|**D**|**NaN**|**T**|


|x1|x2|x3|
|---|---|---|
|**A**|**1**|**T**|
|**B**|**2**|**F**|


|x1|x2|x3|
|---|---|---|
|**A**|**1**|**T**|
|**B**|**2**|**F**|
|**C**|**3**|**NaN**|
|**D**|**NaN**|**T**|


|x1|x2|
|---|---|
|<br>**A**|<br>**1**|
|**B**|**2**|


|x1|x2|
|---|---|
|**C**|**3**|


|x1|x2|
|---|---|
|<br>**A**|<br>**1**|
|**B**|**2**|
|**C**|**3**|


|x1|x2|
|---|---|
|<br>**B**|<br>**2**|
|**C**|**3**|
|**D**|**4**|







Set-like Operations




```
pd.merge(ydf, zdf)
```

Rows that appear in both ydf and zdf
(Intersection).

```
pd.merge(ydf, zdf, how='outer')
```

Rows that appear in either or both ydf and zdf
(Union).

```
pd.merge(ydf, zdf, how='outer',
indicator=True)
.query('_merge == "left_only"')
.drop(columns=['_merge'])
```

Rows that appear in ydf but not zdf (Setdiff).


```
min(axis=1)
```

Element-wise min.
```
abs()
```

Absolute value.



Sum values of each object.
```
count()
```

Count non-NA/null values of
each object.
```
median()
```

Median value of each object.
```
quantile([0.25,0.75])
```

Quantiles of each object.
```
apply( function )
```

Apply function to each object.



Minimum value in each object.
```
max()
```

Maximum value in each object.
```
mean()
```

Mean value of each object.
```
var()
```

Variance of each object.
```
std()
```

Standard deviation of each
object.


```
max(axis=1)
```

Element-wise max.
```
clip(lower=-10,upper=10)
```

Trim values at input thresholds


|x1|x2|
|---|---|
|<br>**B**|<br>**2**|
|**C**|**3**|


### **Windows**
```
df.expanding()
```

Return an Expanding object allowing summary functions to be
applied cumulatively.
```
df.rolling(n)

```

|x1|x2|
|---|---|
|<br>**A**|<br>**1**|
|**B**|**2**|
|**C**|**3**|
|**D**|**4**|


|x1|x2|
|---|---|
|<br>**A**|<br>**1**|



Return a Rolling object allowing summary functions to be
applied to windows of length n.



[Cheatsheet for pandas (http://pandas.pydata.org/) originally written by Irv Lustig,](http://pandas.pydata.org/) [Princeton Consultants, inspired by](http://www.princetonoptimization.com/) [Rstudio Data Wrangling Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf)


### **Plotting**




```
df.plot()
```

Plot a line graph for the DataFrame.

```
df.plot.bar()
```

Plot a line graph for the DataFrame.

```
df.plot(subplots=True)

```

```
df.plot.scatter(x='w', y='h')
```

Plot a scatter graph of the DataFrame.

```
df.plot.boxplot()
```

Plot a scatter graph of the DataFrame.

```
       df.plot(cumulative=True)

```

```
df.plot.hist()
```

Plot a histogram of the DataFrame.

```
df.plot.area()
```

Plot an area graph of the DataFrame.


```
df.plot.pie()
```

Plot a pie chart of the DataFrame.

```
df.plot.hexbin()
```

Plot a hexbin graph of the DataFrame.





Separate into different graphs for each column in
the DataFrame.
```
df.plot(title=“Graph of A against B”)
```

Sets the title of the graph.



Creates a cumulative plot
```
df.plot(bins=30)
```

Set the number of bins into which data is grouped
(histograms)


```
df.plot(stacked=True)
```

Stacks the data for the columns on top of each
other. (bar, barh and area only)
```
df.plot(alpha=0.5)
```

Sets the transparency of the plot to 50%.


```
df.plot(subplots=True, title=['col1', 'col2', 'col3'])
```

Arguments can be combined for more flexibility when graphing, this would plot a separate line graph for of column of a 3-columned DataFrame. The first string in the
list of titles applies to the graph of the left-most column.


```
        df.astype(type)

```



```
pd.to_numeric(data)

```

```
df.astype(type)

```


Convert non-numeric types to
numeric.
```
pd.to_datetime(data)

```










Convert non-datetime types to
datetime type
```
pd.to_timedelta(data)
```

Convert non- timedelta types to
timedelta



Convert data to (almost) any given
type including categorical
```
df.infer_objects()
```

Attempts to infer a better type for
object type data.
```
df.convert_dtypes()
```

Convert columns to best possible
dtypes




### **Input/Output**

Common file types for data input include CSV, JSON, HTML which are humanreadable, while the common output types are usually more optimized for
performance and scalability such as feather, parquet and HDF.












### **Mapping**

Apply a mapping to every element in a DataFrame or Series, useful for
recategorizing or transforming data.

```
s.map(lambda x: 2*x)
```

Returns a copy of the series where every entry is doubled
```
df.apply(lambda s: s.max() - s.min(), axis=1)
```

Returns a Series with the difference of the maximum and minimum values of
each row of the DataFrame


```
df = pd.read_csv(filepath)
```

Read data from csv file
```
df = pd.read_html(filepath)
```

Read data from html file
```
df = pd.read_excel(filepath)
```

Read data from xls (and related) files
```
df = pd.read_sql(filepath)
```

Read data from sql file
```
pd.read_clipboard()
```

Read text from clipboard


```
df.to_parquet(filepath)
```

Write data to parquet file
```
df.to_feather(filepath)
```

Write data to feather file
```
df.to_hdf(filepath)
```

Write data to HDF file
```
df.to_clipboard()
```

Copy object to the system clipboard


