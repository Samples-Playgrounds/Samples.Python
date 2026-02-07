### **Data Wrangling**

with pandas Cheat Sheet http://pandas.pydata.org

Pandas [API Reference](https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api) Pandas [User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide)

**a b c**

|                       | 2 | 5 | 8                | 11 |  |  |  |
|-----------------------|---|---|------------------|----|--|--|--|
|                       | 3 | 6 | 9                | 12 |  |  |  |
| df<br>= pd.DataFrame( |   |   |                  |    |  |  |  |
| {"a" : [4, 5, 6],     |   |   |                  |    |  |  |  |
|                       |   |   | "b" : [7, 8, 9], |    |  |  |  |

 **"c" : [10, 11, 12]},** 

**1** 4 7 10

 **index = [1, 2, 3])** Specify values for each column.

```
df = pd.DataFrame(
 [[4, 7, 10],
 [5, 8, 11],
 [6, 9, 12]], 
 index=[1, 2, 3], 
 columns=['a', 'b', 'c'])
 Specify values for each row.
```

|   |   | a | b | c  |
|---|---|---|---|----|
| N | v |   |   |    |
| D | 1 | 4 | 7 | 10 |
|   | 2 | 5 | 8 | 11 |
| e | 2 | 6 | 9 | 12 |

```
df = pd.DataFrame(
 {"a" : [4 ,5, 6], 
 "b" : [7, 8, 9], 
 "c" : [10, 11, 12]}, 
index = pd.MultiIndex.from_tuples(
 [('d', 1), ('d', 2),
 ('e', 2)], names=['n', 'v']))
 Create DataFrame with a MultiIndex
```

## **Method Chaining**

Most pandas methods return a DataFrame so that another pandas method can be applied to the result. This improves readability of code.

```
df = (pd.melt(df)
 .rename(columns={
 'variable':'var', 
 'value':'val'})
 .query('val >= 200')
 )
```

#### **Tidy Data** – A foundation for wrangling in pandas

In a tidy data set:

![](_page_0_Picture_14.jpeg)

in its own **column**

![](_page_0_Picture_15.jpeg)

![](_page_0_Picture_16.jpeg)

Each **observation** is saved in its own **row**

Tidy data complements pandas's **vectorized operations**. pandas will automatically preserve observations as you manipulate variables. No other format works as intuitively with pandas.

![](_page_0_Picture_19.jpeg)

## **[Creating DataFrames](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) [Reshaping Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)** – Change layout, [sorting,](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#sorting) [reindexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#reindexing-and-altering-labels), renaming

![](_page_0_Figure_21.jpeg)

- **df.[sort\\_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html?highlight=sort_values#pandas.DataFrame.sort_values)('mpg')** Order rows by values of a column (low to high).
- **df.[sort\\_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html?highlight=sort_values#pandas.DataFrame.sort_values)('mpg', ascending=False)** Order rows by values of a column (high to low).
- **df.[rename](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html?highlight=rename#pandas.DataFrame.rename)(columns = {'y':'year'})** Rename the columns of a DataFrame
- **df.[sort\\_index\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html?highlight=sort_index#pandas.DataFrame.sort_index))**
- Sort the index of a DataFrame
- **df.[reset\\_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html?highlight=reset_index#pandas.DataFrame.reset_index)()** Reset index of DataFrame to row numbers, moving index to columns.
- **df[.drop](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html?highlight=drop#pandas.DataFrame.drop)(columns=['Length', 'Height'])** Drop columns from DataFrame

![](_page_0_Picture_30.jpeg)

**df[df.Length > 7]**

Extract rows that meet logical criteria.

**df.[drop\\_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html?highlight=drop_dupli#pandas.DataFrame.drop_duplicates)()**

Remove duplicate rows (only considers columns).

**df.[sample](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html?highlight=sample#pandas.DataFrame.sample)(frac=0.5)**

Randomly select fraction of rows.

- **df.[sample](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html?highlight=sample#pandas.DataFrame.sample)(n=10)** Randomly select n rows.
- **df.[nlargest](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nlargest.html?highlight=nlargest)(n, 'value')** Select and order top n entries.
- **df.[nsmallest](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nsmallest.html?highlight=nsmallest)(n, 'value')** Select and order bottom n entries.
- **df.[head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html?highlight=head)(n)**
- Select first n rows.
- **df.[tail](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html?highlight=tail)(n)** Select last n rows.

#### **[Subset Observations](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html) - rows [Subset Variables](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html) - columns [Subsets](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html) - rows and columns**

![](_page_0_Picture_44.jpeg)

**df[['width', 'length', 'species']]** Select multiple columns with specific names.

**df['width']** *or* **df.width**

Select single column with specific name.

**df[.filter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html?highlight=filter#pandas.DataFrame.filter)(regex='***regex***')**

 Select columns whose name matches regular expression *regex*.

#### **Using [query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)**

query() allows Boolean expressions for filtering rows.

- **df[.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)('Length > 7')**
- **df[.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)('Length > 7 and Width < 8')**
- **df[.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)('Name.str.startswith("abc")', engine="python")**

Use **df.loc[]** and **df.iloc[]** to select only rows, only columns or both.

Use **df.at[]** and **df.iat[]** to access a single value by row and column.

First index selects rows, second index columns.

**df.[iloc\[](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)10:20]**

Select rows 10-20.

- **df.[iloc\[](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html):, [1, 2, 5]]**
- Select columns in positions 1, 2 and 5 (first column is 0).
- **df.[loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html?highlight=loc)[:, 'x2':'x4']**

Select all columns between x2 and x4 (inclusive).

**df.[loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html?highlight=loc)[df['a'] > 10, ['a', 'c']]** Select rows meeting logical condition, and only

the specific columns . **df.[iat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat)[1, 2]** Access single value by index

- **df.[at](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at)[4, 'A']** Access single value by label
- **regex (Regular Expressions) Examples '\.'** Matches strings containing a period '.' **'Length\$'** Matches strings ending with word 'Length' **'^Sepal'** Matches strings beginning with the word 'Sepal'

|   | Logic in Python (and pandas) |                                                     |                                     |  |  |  |
|---|------------------------------|-----------------------------------------------------|-------------------------------------|--|--|--|
| < | Less than                    | !=                                                  | Not equal to                        |  |  |  |
| > | Greater than                 | df.column.isin(values)                              | Group membership                    |  |  |  |
|   | == Equals                    | pd.isnull(obj)                                      | Is NaN                              |  |  |  |
|   | <= Less than or equals       | pd.notnull(obj)                                     | Is not NaN                          |  |  |  |
|   |                              | >= Greater than or equals &, ,~,^,df.any(),df.all() | Logical and, or, not, xor, any, all |  |  |  |

**'^x[1-5]\$'** Matches strings beginning with 'x' and ending with 1,2,3,4,5 **'^(?!Species\$).\*'** Matches strings except the string 'Species'

Cheatsheetfor pandas [\(http://pandas.pydata.org/](http://pandas.pydata.org/) originally written by Irv Lustig, [Princeton Consultants,](http://www.princetonoptimization.com/) inspired by [Rstudio](https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf) [Data Wrangling Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf)

### **[Group Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)**

![](_page_1_Picture_1.jpeg)

**df[.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html?highlight=groupby#pandas.DataFrame.groupby)(by="col")**

Return a GroupBy object, grouped by values in column named "col".

**df[.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html?highlight=groupby#pandas.DataFrame.groupby)(level="ind")**

Return a GroupBy object, grouped by values in index level named "ind".

All of the summary functions listed above can be applied to a group. Additional GroupBy functions:

**[size\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.size.html?highlight=size#pandas.DataFrame.size))**

Size of each group.

**[agg](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html?highlight=agg#pandas.DataFrame.agg)(***function***)**

Aggregate group using function.

The examples below can also be applied to groups. In this case, the function is applied on a per-group basis, and the returned vectors are of the length of the original DataFrame.

**[shift](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shift.html?highlight=shift#pandas.DataFrame.shift)(1)**

Copy with values shifted by 1. **[rank\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rank.html?highlight=rank#pandas.DataFrame.rank)method='dense')**

Ranks with no gaps.

**[rank\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rank.html?highlight=rank#pandas.DataFrame.rank)method='min')**

Ranks. Ties get min rank.

**[rank\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rank.html?highlight=rank#pandas.DataFrame.rank)pct=True)**

Ranks rescaled to interval [0, 1].

**[rank\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rank.html?highlight=rank#pandas.DataFrame.rank)method='first')**

Ranks. Ties go to first value.

**[shift](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shift.html?highlight=shift#pandas.DataFrame.shift)(-1)**

Copy with values lagged by 1.

**[cumsum](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.cumsum.html?highlight=cumsum#pandas.DataFrame.cumsum)()**

Cumulative sum.

**[cummax](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.cummax.html?highlight=cummax#pandas.DataFrame.cummax)()**

Cumulative max.

**[cummin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.cummin.html?highlight=cummin#pandas.DataFrame.cummin)()**

Cumulative min.

**[cumprod](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cumprod.html?highlight=cumprod#pandas.Series.cumprod)()**

Cumulative product.

### **[Summarize Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#descriptive-statistics)**

**df['w'][.value\\_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html?highlight=value_counts#pandas.DataFrame.value_counts)()**

Count number of rows with each unique value of variable **len(df)**

# of rows in DataFrame.

**df.[shape](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html)**

Tuple of # of rows, # of columns in DataFrame.

**df['w'].[nunique](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html?highlight=nunique)()**

# of distinct values in a column.

**df[.describe\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html?highlight=describe#pandas.DataFrame.describe))**

Basic descriptive and statistics for each column (or GroupBy).

**df.[info](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)()**

Prints a concise summary of the DataFrame.

**df[.memory\\_usage](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html)()**

Prints the memory usage of each column in the DataFrame.

**df[.dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html#pandas.DataFrame.dtypes)()**

Prints a Series with the dtype of each column in the DataFrame.

![](_page_1_Picture_47.jpeg)

pandas provides a large set of **[summary functions](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#descriptive-statistics)** that operate on different kinds of pandas objects (DataFrame columns, Series, GroupBy, Expanding and Rolling (see below)) and produce single values for each of the groups. When applied to a DataFrame, the result is returned as a pandas Series for each column. Examples:

**[min](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.min.html?highlight=min#pandas.DataFrame.min)()**

**[max\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html?highlight=max#pandas.DataFrame.max))**

**[mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html?highlight=mean#pandas.DataFrame.mean)()**

**[var](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.var.html?highlight=var#pandas.DataFrame.var)()**

**[std](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.std.html?highlight=std#pandas.DataFrame.std)()**

object.

Minimum value in each object.

Maximum value in each object.

Mean value of each object.

Standard deviation of each

Variance of each object.

**[sum\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html?highlight=sum#pandas.DataFrame.sum))**

Sum values of each object.

**[count](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.count.html?highlight=count#pandas.DataFrame.count)()**

Count non-NA/null values of each object.

**[median](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html?highlight=median#pandas.DataFrame.median)()**

Median value of each object. **[quantile\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.quantile.html?highlight=quantile#pandas.DataFrame.quantile)[0.25,0.75])**

Quantiles of each object.

**[apply\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html?highlight=apply#pandas.DataFrame.apply)***function***)**

Apply function to each object.

#### **df.[dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html?highlight=dropna#pandas.DataFrame.dropna)()**

Drop rows with any column having NA/null data.

**df.[fillna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html?highlight=fillna#pandas.DataFrame.fillna)(value)**

Replace all NA/null data with value.

### **Make New Columns**

**[Handling Missing Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)**

![](_page_1_Picture_63.jpeg)

**df.[assign\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html?highlight=assign)Area=lambda df: df.Length\*df.Height)**

Compute and append one or more new columns.

**df['Volume'] = df.Length\*df.Height\*df.Depth** Add single column.

**pd.[qcut\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.qcut.html?highlight=qcut#pandas.qcut)df.col, n, labels=False)** Bin column into n buckets.

![](_page_1_Picture_68.jpeg)

pandas provides a large set of **vector functions** that operate on all columns of a DataFrame or a single selected column (a pandas Series). These functions produce vectors of values for each of the columns, or a single Series for the individual Series. Examples:

**[max\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html?highlight=max#pandas.DataFrame.max)axis=1)** Element-wise max. **[min](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.min.html?highlight=min#pandas.DataFrame.min)(axis=1)** Element-wise min.

**[clip\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.clip.html?highlight=clip#pandas.DataFrame.clip)lower=-10,upper=10) [abs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.abs.html?highlight=abs)()**

Trim values at input thresholds Absolute value.

### **[Windows](https://pandas.pydata.org/pandas-docs/stable/user_guide/window.html)**

#### **df.[expanding](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.expanding.html?highlight=expanding#pandas.DataFrame.expanding)()**

Return an Expanding object allowing summary functions to be applied cumulatively.

#### **df.[rolling\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html?highlight=rolling#pandas.DataFrame.rolling)n)**

Return a Rolling object allowing summary functions to be applied to windows of length n.

### **[Combine Data Sets](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)**

**x1 x3 A T B F D T adf bdf**

#### Standard Joins

**x1 x2 A 1 B 2 C 3**

**x1 x2 x3 A 1 T B 2 F C 3 NaN pd[.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)(adf, bdf, how='left', on='x1')** Join matching rows from bdf to adf.

**x1 x2 x3 A 1.0 T B 2.0 F D NaN T pd[.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)(adf, bdf, how='right', on='x1')** Join matching rows from adf to bdf.

**x1 x2 x3 A 1 T B 2 F pd[.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)(adf, bdf, how='inner', on='x1')** Join data. Retain only rows in both sets.

**x1 x2 x3 A 1 T B 2 F C 3 NaN D NaN T pd[.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)(adf, bdf, how='outer', on='x1')** Join data. Retain all values, all rows.

#### Filtering Joins

**x1 x2 adf[adf.x1.[isin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html?highlight=isin#pandas.DataFrame.isin)(bdf.x1)]** All rows in adf that have a match in bdf.

**A 1 B 2**

**x1 x2 C 3 adf[~adf.x1.[isin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html?highlight=isin#pandas.DataFrame.isin)(bdf.x1)]** All rows in adf that do not have a match in bdf.

> **x1 x2 A 1 B 2 C 3 x1 x2 B 2 C 3 D 4 ydf zdf**

#### Set-like Operations

**A 1**

**x1 x2 B 2 C 3 x1 x2 A 1 B 2 C 3 D 4 x1 x2 pd[.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)(ydf, zdf)** Rows that appear in both ydf and zdf (Intersection). **pd[.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)(ydf, zdf, how='outer')** Rows that appear in either or both ydf and zdf (Union). **pd[.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)(ydf, zdf, how='outer', indicator=True) .[query\(](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html?highlight=query#pandas.DataFrame.query)'\_merge == "left\_only"')**

**.[drop](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html?highlight=drop#pandas.DataFrame.drop)(columns=['\_merge'])**

Rows that appear in ydf but not zdf (Setdiff).

Cheatsheet for pandas (<http://pandas.pydata.org/>) originally written by Irv Lustig, [Princeton Consultants,](http://www.princetonoptimization.com/) inspired by [Rstudio](https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf) [Data](https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf) [Wrangling Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf)

## **[Plotting](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)**

**df.[plot.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)[hist\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html))**

**df.[plot.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)[area\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.area.html))**

**s.str.[count](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html)(pattern)**

entire Series efficiently.

counts in each element. **s.str.[get\(](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html)index)**

has been concatenated.

word to be a capital.

**s.str.[join\(](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html)sep)**

**s.str.[title](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html)()**

**s.str.[len\(](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#pandas.Series.str.len))**

each element.

Returns a series with the integer

given index for each element.

Returns a series with the data at the

Returns a series where each element

Converts the first character of each

Returns a series with the lengths of

Plot a histogram of the DataFrame.

Plot an area graph of the DataFrame.

**df[.plot\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html))**

Plot a line graph for the DataFrame.

![](_page_2_Figure_3.jpeg)

**df[.plot.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)[bar\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html))**

Plot a line graph for the DataFrame.

![](_page_2_Figure_6.jpeg)

**df.[plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html).[boxplot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html)()**

Plot a scatter graph of the DataFrame.

**df.[plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html).[scatter](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html)(x='w', y='h')**

![](_page_2_Figure_9.jpeg)

**df.[plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)(subplots=True)**

Separate into different graphs for each column in the DataFrame.

**df.[plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)(title="Graph of A against B")** Sets the title of the graph.

**df.[plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)(cumulative=True)**

Creates a cumulative plot

**df.[plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)(bins=30)**

Set the number of bins into which data is grouped

(histograms)

**df.[plot.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)[pie\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html))**

Plot a pie chart of the DataFrame.

![](_page_2_Picture_22.jpeg)

**df.[plot.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)[hexbin](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html)()**

Plot a hexbin graph of the DataFrame.

![](_page_2_Figure_25.jpeg)

Concatenate elements into a single

Splits the string on the first instance

Use regex to replace patterns in each

Checks whether each element is

**s.str.[slice](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html)(start, stop,** 

**s.str.[replace](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html)(pat, rep)**

**s.str.[partition](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.partition.html)(sep)**

**df[.plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)(stacked=True)**

Stacks the data for the columns on top of each other. (bar, barh and area only)

**df[.plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)(alpha=0.5)**

**Series String Operations**

Similar to python string operations, except these are vectorized to apply to the

Sets the transparency of the plot to 50%.

**s.str.[cat](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.cat.html)()**

of the separator

Slices each string

**s.str.[isalnum\(](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalnum.html))**

alpha-numeric

string

**step)**

string.

**df[.plot\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)subplots=True, title=['col1', 'col2', 'col3'])**

Arguments can be combined for more flexibility when graphing, this would plot a separate line graph for of column of a 3-columned DataFrame. The first string in the list of titles applies to the graph of the left-most column.

### **Changing Type**

**pd[.to\\_numeric](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)(data)**

Convert non-numeric types to numeric.

**pd[.to\\_datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)(data)**

Convert non-datetime types to datetime type

**pd[.to\\_timedelta](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html)(data)**

Convert non- timedelta types to timedelta

**df.[astype\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)type)**

Convert data to (almost) any given type including categorical

**df.[infer\\_objects](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.infer_objects.html)()**

object type data.

**df.[convert\\_dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html)()**

Convert columns to best possible dtypes

Attempts to infer a better type for

### **Datetime**

With a Series containing data of type datetime, the dt accessor is used to get various components of the datetime values:

**s.dt.year**

Extract the year

**s.dt.month**

Extract the month as an integer.

**s[.map](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html)(lambda x: 2\*x)**

recategorizing or transforming data.

each row of the DataFrame

**s.dt.day**

Extract the day (int) from the date.

**s.dt.quarter**

Find which quarter the date lies in.

**s.dt.hour**

Extract the hour.

**s.dt.minute**

Extract the minute.

**s.dt.second**

**Mapping**

Apply a mapping to every element in a DataFrame or Series, useful for

Returns a Series with the difference of the maximum and minimum values of

Returns a copy of the series where every entry is doubled **df.[apply](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply)(lambda s: s.max() - s.min(), axis=1)**

Extract the second.

# **[Input/Output](https://pandas.pydata.org/docs/reference/io.html)**

Common file types for data input include CSV, JSON, HTML which are humanreadable, while the common output types are usually more optimized for performance and scalability such as feather, parquet and HDF.

**df = pd.[read\\_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)(filepath)** Read data from csv file

**df = pd.[read\\_html\(](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)filepath)** Read data from html file

**df = pd.[read\\_excel\(](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)filepath)** Read data from xls (and related) files

**df = pd.[read\\_sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)(filepath)** Read data from sql file

**pd.[read\\_clipboard](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html)()** Read text from clipboard **df[.to\\_parquet\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html)filepath)** Write data to parquet file

**df[.to\\_feather\(](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html)filepath)**

Write data to feather file **df[.to\\_hdf](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html)(filepath)**

Write data to HDF file

**df[.to\\_clipboard](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html)()**

Copy object to the system clipboard

# **[Frequently Used](https://pandas.pydata.org/docs/user_guide/options.html) [Options](https://pandas.pydata.org/docs/user_guide/options.html)**

Pandas offers some 'options' to globally control how Pandas behaves, display etc. Options can be queried and set via:

**pd.options.***option\_name* (where *option\_name* is the name of an option). For example:

**pd.options.display.max\_rows = 20** Set the **display.max\_rows** option to 20.

Functions

**[get\\_option](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html)(option)**

Fetch the value of the given option.

**[set\\_option](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html)(option)**

Set the value of the given option.

**[reset\\_option](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html)(options)**

Reset the values of all given options to default settings.

**[describe\\_option](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html)(options)**

Print descriptions of given options.

**[option\\_context\(](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html)options)**

Execute code with temporary option settings that revert to prior settings after execution.

Display options

**display.max\_rows**

The maximum number of rows displayed in pretty-print.

**display.max\_columns**

The maximum number of columns displayed in pretty-print.

**display.expand\_frame\_repr**

Controls whether the DataFrame representation stretches across pages.

**display.large\_repr**

Controls whether a DataFrame that exceeds maximum rows/columns is truncated or summarized

**display.precision**

The output display precision in decimal places.

**display.max\_colwidth**

The maximum width of columns, longer cells will be truncated.

**display.max\_info\_columns**

The maximum number of columns displayed after calling **info()**.

**display.chop\_threshold**

Sets the rounding threshold to zero when displaying a Series/DataFrame.

**display.colheader\_justify**

Controls how column headers are justified.