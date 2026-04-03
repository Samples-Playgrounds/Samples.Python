## **Tidy Data** – A foundation for wrangling in pandas 

## **Data Wrangling** with pandas Cheat Sheet http://pandas.pydata.org 

In a tidy data set: Each **variable** is saved in its own **column**[&] 

Tidy data complements pandas’s **vectorized** `*` **operations** . pandas will automatically preserve observations as you manipulate variables. No other format works as intuitively with pandas. Each **observation** is `M A *` saved in its own **row** 

Pandas API Reference Pandas User Guide 

## **Creating DataFrames** 

## **Reshaping Data** – Change layout, sorting, reindexing, renaming 

**`df.sort_values('mpg')`** Order rows by values of a column (low to high). 

||**a**|**b**|**c**|
|---|---|---|---|
|**1**|4|7|10|
|**2**|5|8|11|
|**3**|6|9|12|



**`df.sort_values('mpg', ascending=False)`** Order rows by values of a column (high to low). 

**`df = pd.DataFrame( {"a" : [4, 5, 6],`** 

## **`pd.melt(df)`** 

## **`df.rename(columns = {'y':'year'})`** 

**`df.pivot(columns='var', values='val')`** Spread rows into columns. 

Gather columns into rows. 

Rename the columns of a DataFrame 

**`"b" : [7, 8, 9],`** 

**`"c" : [10, 11, 12]}, index = [1, 2, 3])`** Specify values for each column. **`df =`** : **`pd.DataFrame( [[4, 7, 10], [5, 8, 11], [6, 9, 12]], index=[1, 2, 3], columns=['a', 'b', 'c'])`** Specify values for each row. 

## **`df.sort_index()`** 

Sort the index of a DataFrame 

**`df.reset_index()`** Reset index of DataFrame to row numbers, moving index to columns. 

**`pd.concat([df1,df2], axis=1)`** Append columns of DataFrames 

## **`pd.concat([df1,df2])`** 

**`df.drop(columns=['Length', 'Height'])`** Drop columns from DataFrame 

Append rows of DataFrames 

## **Subset Observations - rows** 

## **Subset Variables - columns** 

## **Subsets - rows and columns** 

Use **`df.loc[]`** and **`df.iloc[]`** to select only rows, only columns or both. Use **`df.at[]`** and **`df.iat[]`** to access a single value by row and column. 

|||**a**|**b**|**c**|
|---|---|---|---|---|
|**N**|**v**||||
|**D**|**1**|4|7|10|
||**2**|5|8|11|
|**e**|**2**|6|9|12|



**`df[df.Length > 7]`** Extract rows that meet logical criteria. 

## **`df[['width', 'length', 'species']]`** 

Select multiple columns with specific names. **`df['width']`** _or_ **`df.width`** 

First index selects rows, second index columns. 

## **`df.drop_duplicates()`** 

## **`df.iloc[10:20]`** 

Remove duplicate rows (only considers columns). **`df.sample(frac=0.5)`** 

**`df = pd.DataFrame( {"a" : [4 ,5, 6],`** 

Select single column with specific name. **`df.filter(regex='`** _**`regex`**_ **`')`** Select columns whose name matches regular expression _regex_ . 

Select rows 10-20. 

## **`df.iloc[:, [1, 2, 5]]`** 

Randomly select fraction of rows. **`df.sample(n=10)`** Randomly select n rows. 

- **`"b" : [7, 8, 9],`** 

Select columns in positions 1, 2 and 5 (first column is 0). 

**`"c" : [10, 11, 12]}, index = pd.MultiIndex.from_tuples( [('d', 1), ('d', 2),`** 

## **`df.nlargest(n, 'value')`** 

## **`df.loc[:, 'x2':'x4']`** 

## **Using query** 

Select and order top n entries. 

Select all columns between x2 and x4 (inclusive). **`('e', 2)], names=['n', 'v'])) df.nsmallest(n, 'value')`** query() allows Boolean expressions for filtering **`df.loc[df['a'] > 10, ['a', 'c']]`** Create DataFrame with a MultiIndex Select and order bottom n entries. rows. Select rows meeting logical condition, and only **`df.head(n) df.query('Length > 7')`** the specific columns . Select first n rows. **`df.query('Length > 7 and Width < 8') df.iat[1, 2]`** Access single value by index **`df.tail(n)` Method Chaining** **`df.query('Name.str.startswith("abc")', df.at[4, 'A']`** Access single value by label Select last n rows. Most pandas methods return a DataFrame so that **`engine="python")`** another pandas method can be applied to the result. **Logic in Python (and pandas) regex (Regular Expressions) Examples** This improves readability of code. **`<`** Less than **`!=`** Not equal to **`'\.'`** Matches strings containing a period '.' **`df = (pd.melt(df) >`** Greater than **`df.column.isin(`** _**`values`**_ **`)`** Group membership **`'Length$'`** Matches strings ending with word 'Length' **`.rename(columns={ 'variable':'var', ==`** Equals **`pd.isnull(`** _**`obj`**_ **`)`** Is NaN **`'^Sepal'`** Matches strings beginning with the word 'Sepal' **`'value':'val'}) <=`** Less than or equals **`pd.notnull(`** _**`obj`**_ **`)`** Is not NaN **`'^x[1-5]$'`** Matches strings beginning with 'x' and ending with 1,2,3,4,5 **`.query('val >= 200') >=`** Greater than or equals **`&,|,~,^,df.any(),df.all()`** Logical and, or, not, xor, any, all **`'^(?!Species$).*'`** Matches strings except the string 'Species' ~~—=—————~~ **`)`** Cheatsheet for pandas (http://pandas.pydata.org/ originally written by Irv Lustig, Princeton Consultants,  inspired by Rstudio Data Wrangling Cheatsheet 

## **Group Data** 

## **Combine Data Sets** 

The examples below can also be applied to groups. In this case, the function is applied on a per-group basis, and the returned vectors are of the length of the original DataFrame. 

**`df.groupby(by="col")`** Return a GroupBy object, grouped by values in column named "col". 

||||**x1 x2**<br>**A**<br>**1**<br>**adf**|**x1 x2**<br>**A**<br>**1**<br>**adf**|**x1 x2**<br>**A**<br>**1**<br>**adf**|||**x1 x3**<br>**A**<br>**T**<br>**bdf**||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Standard Joins<br>**x1**<br>**x2**|||**B**<br>**C**<br>Standard Joins<br>**x3**||**2**<br>**3**<br>**B**<br>**F**<br>**D**<br>**T**<br>**pd.merge**<br>**(adf, bdf,**|||||||
||**A**|**1**|**T**||**how='left', on='x1')**|**how='left', on='x1')**|**how='left', on='x1')**|**how='left', on='x1')**||||
||**B**|**2**|**F**|||Join matching rows from bdf to adf.|Join matching rows from bdf to adf.|Join matching rows from bdf to adf.|Join matching rows from bdf to adf.|Join matching rows from bdf to adf.|Join matching rows from bdf to adf.|



## **`shift(1)`** 

## **`shift(-1)`** 

## **`df.groupby(level="ind")`** 

Copy with values shifted by 1. Copy with values lagged by 1. **`rank(method='dense') cumsum()`** Ranks with no gaps. Cumulative sum. **`rank(method='min') cummax()`** Ranks. Ties get min rank. Cumulative max. 

Return a GroupBy object, grouped by values in index level named "ind". 

**`rank(pct=True)(pct=True)`** 

All of the summary functions listed above can be applied to a group. **`rank(pct=True)(pct=True) cummin()` B 2 F** Join matching rows from bdf to adf. Additional GroupBy functions: Ranks rescaled to interval [0, 1]. Cumulative min. **C 3 NaN** **`size() agg(`** _`function`_ **`) rank(method='first')`** ~~3~~ **`cumprod()` x1 x2 x3** Size of each group. Aggregate group using function. Ranks. Ties go to first value. Cumulative product. **`pd.merge(adf, bdf,` A 1.0 T** **`how='right', on='x1')` B 2.0 F** Join matching rows from adf to bdf. **Summarize Data Handling Missing Data D NaN T** ~~=~~ **`df['w'].value_counts()`** ~~:~~ **`df.dropna()` x1 x2 x3** Count number of rows with each unique value of variable Drop rows with any column having NA/null data. **`pd.merge(adf, bdf,` A 1 T** **`len(df) df.fillna(value) how='inner', on='x1')` B 2 F** # of rows in DataFrame. Join data. Retain only rows in both sets. Replace all NA/null data with value. **`df.`** Tuple of # of rows, # of columns in DataFrame. **`shape`** ~~~~~ **Make New Columns x1A x21 x3T** **`pd.merge(adf, bdf, df['w'].nunique()`** ~~a~~ e **`how='outer', on='x1')`** # of distinct values in a column. **B 2 F** Join data. Retain all values, all rows. **`df.describe()` C 3 NaN** Basic descriptive and statistics for each column (or GroupBy). **D NaN T** **`df.info()`** Filtering Joins Prints a concise summary of the DataFrame. **`df.assign(Area=lambda df: df.Length*df.Height)` x1 x2** **`adf[adf.x1.isin(bdf.x1)] df.memory_usage()`** Compute and append one or more new columns. **A 1** All rows in adf that have a match in bdf. Prints the memory usage of each column in the DataFrame. **`df['Volume'] = df.Length*df.Height*df.Depth` B 2** **`df.dtypes()dtypes()())`** Add single column. Prints a Series with the dtype of each column in the DataFrame. **`pd.qcut(df.col, n, labels=False).qcut(df.col, n, labels=False)qcut(df.col, n, labels=False)(df.col, n, labels=False)` x1 x2** **`adf[~adf.x1.isin(bdf.x1)]`** Bin column into n buckets. **C 3** All rows in adf that do not have a match in bdf. 

**`df['Volume'] = df.Length*df.Height*df.Depth`** Add single column. **`pd.qcut(df.col, n, labels=False).qcut(df.col, n, labels=False)qcut(df.col, n, labels=False)(df.col, n, labels=False)`** Bin column into n buckets. **Vector Vector function function** ~~—~~ pandas provides a large set of **vector functions** that operate on all columns of a DataFrame or a single selected column (a pandas Series). These functions produce vectors of values for each of the columns, or a single Series for the individual Series. Examples: 

Prints the memory usage of each column in the DataFrame. **`df.dtypes()dtypes()())`** Prints a Series with the dtype of each column in the DataFrame. ~~-~~ 

||||||**x1 x2**<br>**A**<br>**1**<br>**x1 x2**<br>**B**<br>**2**<br>**ydf**<br>**zdf**|**x1 x2**<br>**A**<br>**1**<br>**x1 x2**<br>**B**<br>**2**<br>**ydf**<br>**zdf**||||
|---|---|---|---|---|---|---|---|---|---|
||||||**B**<br>**C**|**2**<br>**3**<br>**C**<br>**3**<br>**D**<br>**4**||||
|||||||||||
|Set-like Operations||||Set-like Operations||||||
||**x1 **<br>**B**<br>**C**<br>**x1 **<br>**A**<br>**B**<br>**C**|**x2**<br>**2**<br>**3**<br> **x2**<br>**1**<br>**2**<br>**3**||||**pd.merge**<br>**(ydf, zdf)**<br>Rows that appear in both ydf and zdf<br>(Intersection).<br>**pd.merge**<br>**(ydf, zdf, how='outer')**<br>Rows that appear in either or both ydf and zdf<br>(Union).||||
||**D**<br>**x1 **<br>**A**|**4**<br> **x2**<br>**1**||||**pd.merge**<br>**(ydf, zdf, how='outer',**<br>**indicator=True)**<br>**.query**<br>**('_merge == "left_only"')**<br>**.drop**<br>**(columns=['_merge'])**<br>Rows that appear in ydf but not zdf (Setdiff).||||



pandas provides a large set of **summary functions** that operate on different kinds of pandas objects (DataFrame columns, Series, GroupBy, Expanding and Rolling (see below)) and produce single values for each of the groups. When applied to a DataFrame, the result is returned as a pandas Series for each column. Examples: 

## **`sum() min()`** 

## **`max(axis=1) min(axis=1)`** Element-wise max. 

Sum values of each object. Minimum value in each object. **`count() max()`** Count non-NA/null values of Maximum value in each object. each object. **`mean() median()`** Mean value of each object. ~~_~~ Median value of each object. ~~-~~ **`var() quantile([0.25,0.75])`** Variance of each object. Quantiles of each object. **`std() apply(`** _`function`_ **`)`** Standard deviation of each Apply function to each object. object. 

Element-wise min. 

**`clip(lower=-10,upper=10) abs()`** Trim values at input thresholds Absolute value. **Windows** = : **`df.expanding()`** Return an Expanding object allowing summary functions to be applied cumulatively. 

## **`df.rolling(n)`** 

Return a Rolling object allowing summary functions to be applied to windows of length n. 

Cheatsheet for pandas (http://pandas.pydata.org/) originally written by Irv Lustig, Princeton Consultants,  inspired by Rstudio Data Wrangling Cheatsheet 

## **`df.plot()`** 

Plot a line graph for the DataFrame. 

## **`df.plot.bar()`** 

Plot a line graph for the DataFrame. 

## **Plotting** 

## **`df.plot.scatter(x='w', y='h')`** 

## **`df.plot.hist()`** 

## **`df.plot.pie()`** 

Plot a scatter graph of the DataFrame. 

Plot a histogram of the DataFrame. 

Plot a pie chart of the DataFrame. 

## **`df.plot.boxplot()`** 

## **`df.plot.area()`** 

## **`df.plot.hexbin()`** 

Plot a scatter graph of the DataFrame. 

Plot an area graph of the DataFrame. Plot a hexbin graph of the DataFrame. 

## **Frequently Used Options** 

Pandas offers some ‘options’ to globally control how Pandas behaves, display etc. Options can be queried and set via: **`pd.options.`** _**`option_name`**_ (where _option_name_ is the name of an option). For example: 

**`pd.options.display.max_rows = 20`** Set the **`display.max_rows`** option to 20. 

## **`df.plot(subplots=True)`** 

## **`df.plot(cumulative=True)`** 

## **`df.plot(stacked=True)`** 

Separate into different graphs for each column in the DataFrame. 

Stacks the data for the columns on top of each other. (bar, barh and area only) 

Creates a cumulative plot 

## **`df.plot(bins=30)`** 

**`df.plot(title=“Graph of A against B”)`** Sets the title of the graph. 

**`df.plot(alpha=0.5)`** 

Set the number of bins into which data is grouped (histograms) 

Sets the transparency of the plot to 50%. 

## **`df.plot(subplots=True, title=['col1', 'col2', 'col3'])`** 

Arguments can be combined for more flexibility when graphing, this would plot a separate line graph for of column of a 3-columned DataFrame. The first string in the list of titles applies to the graph of the left-most column. 

## **Changing Type** 

## **Series String Operations** 

Similar to python string operations, except these are vectorized to apply to the entire Series efficiently. 

## **`pd.to_numeric(data)`** 

## **`df.astype(type)`** 

Convert data to (almost) any given type including categorical 

Convert non-numeric types to numeric. 

**`s.str.count(pattern)`** Returns a series with the integer counts in each element. 

## **`s.str.cat()`** 

Concatenate elements into a single string 

## **`pd.to_datetime(data)`** 

**`df.infer_objects()`** Attempts to infer a better type for object type data. 

Convert non-datetime types to datetime type 

## **`s.str.get(index)`** 

**`s.str.partition(sep)`** 

Splits the string on the first instance of the separator 

Returns a series with the data at the given index for each element. 

**`pd.to_timedelta(data) df.convert_dtypes()`** Convert non- timedelta types to Convert columns to best possible timedelta dtypes 

## **`s.str.join(sep)`** 

## **`s.str.slice(start, stop,`** 

## **`step)`** 

Returns a series where each element has been concatenated. 

Slices each string 

## **Datetime** 

## **`s.str.title()`** 

**`s.str.replace(pat, rep)`** 

## **`s.dt.day`** 

Converts the first character of each word to be a capital. 

Use regex to replace patterns in each string. 

Extract the day (int) from the date. 

With a Series containing data of type datetime, the dt accessor is used to get various components of the datetime values: 

## **`s.dt.quarter`** 

## **`s.str.len()`** 

**`s.str.isalnum()`** Checks whether each element is alpha-numeric 

Find which quarter the date lies in. **`s.dt.hour`** Extract the hour. 

Returns a series with the lengths of each element. 

> **`s.dt.year s.dt.minute`** Extract the year Extract the minute. **`s.dt.month s.dt.second`** Extract the month as an integer. Extract the second. 

## **Input/Output** 

Common file types for data input include CSV, JSON, HTML which are humanreadable, while the common output types are usually more optimized for performance and scalability such as feather, parquet and HDF. 

## **Mapping** 

**`df = pd.read_csv(filepath)`** Read data from csv file 

**`df.to_parquet(filepath)`** Write data to parquet file 

**`df = pd.read_html(filepath)`** Read data from html file 

**`df.to_feather(filepath)`** Write data to feather file 

Apply a mapping to every element in a DataFrame or Series, useful for recategorizing or transforming data. 

**`df = pd.read_excel(filepath)`** Read data from xls (and related) files 

**`df.to_hdf(filepath)`** Write data to HDF file 

## **`s.map(lambda x: 2*x)`** 

Returns a copy of the series where every entry is doubled 

**`df = pd.read_sql(filepath)`** Read data from sql file 

## **`df.to_clipboard()`** 

## **`df.apply(lambda s: s.max() - s.min(), axis=1)`** 

Copy object to the system clipboard 

Returns a Series with the difference of the maximum and minimum values of each row of the DataFrame 

**`pd.read_clipboard()`** 

## Functions 

## **`get_option(option)`** 

Fetch the value of the given option. 

## **`set_option(option)`** 

Set the value of the given option. 

## **`reset_option(options)`** 

Reset the values of all given options to default settings. 

## **`describe_option(options)`** 

Print descriptions of given options. 

## **`option_context(options)`** 

Execute code with temporary option settings that revert to prior settings after execution. 

## Display options 

## **`display.max_rows`** 

The maximum number of rows displayed in pretty-print. 

## **`display.max_columns`** 

The maximum number of columns displayed in pretty-print. 

## **`display.expand_frame_repr`** 

Controls whether the DataFrame representation stretches across pages. 

## **`display.large_repr`** 

Controls whether a DataFrame that exceeds maximum rows/columns is truncated or summarized 

## **`display.precision`** 

The output display precision in decimal places. 

## **`display.max_colwidth`** 

The maximum width of columns, longer cells will be truncated. 

## **`display.max_info_columns`** 

The maximum number of columns displayed after calling **`info()`** . 

## **`display.chop_threshold`** 

Sets the rounding threshold to zero when displaying a Series/DataFrame. 

**`display.colheader_justify`** Controls how column headers are justified. 

Read text from clipboard 

