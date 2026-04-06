|    | 0                           | 1                                     |
|---:|:----------------------------|:--------------------------------------|
|  0 | pd.melt(df)                 | df.pivot(columns='var', values='val') |
|    |   Gather columns into rows. |   Spread rows into columns.           |
|  1 | pd.concat([df1,df2])        | pd.concat([df1,df2], axis=1)          |
|    |   Append rows of DataFrames |   Append columns of DataFrames        |