## Python For Data Science Cheat Sheet
#### Python Basics

Learn More Python for Data Science Interactively at www.datacamp.com











































































**Asking For Help**
```
>>> help(str)

```




























**Learn Python for Data Science** **Interactively**


##### Jupyter Notebook

Learn More Python for Data Science Interactively at www.DataCamp.com





























**Command Mode:**




























































##### **Subsetting, Slicing, Indexing**


## Python For Data Science Cheat Sheet
#### NumPy Basics

Learn Python for Data Science **Interactively** at www.DataCamp.com









**Also see Lists**




|1 .5|2|3|
|---|---|---|
|<br> <br>4|<br> <br> 5|<br> <br>6|


##### **NumPy**



2







The **NumPy** library is the core library for scientific computing in
Python. It provides a high-performance multidimensional array




|1|2|3|
|---|---|---|
|<br>1.5|<br>2|<br>3|
|<br>4|<br> 5|<br>6|
|<br>1.5|<br>2|<br>3|
|<br> <br>4|<br> <br> 5|<br> <br>6|



Use the following import convention:
```
  >>> import numpy as np
```

**NumPy Arrays**

**1D array** **2D array                   3D array**







1 2 3



axis 1


axis 0



axis 0


|1.5|2|3|
|---|---|---|
|4|5|6|

































**DataCamp**
**Learn Python for Data Science** **Interactively**


## Python For Data Science Cheat Sheet
#### SciPy - Linear Algebra

Learn More Python for Data Science Interactively at www.datacamp.com



























**DataCamp**
**Learn Python for Data Science** **Interactively**


## Python For Data Science Cheat Sheet




















|a|3|
|---|---|
|b|-5|
|c|7|
|d|4|














































|Belgium|Brussels|11190846|
|---|---|---|
|India|New Delhi|1303171035|
|Brazil|Brasília|207847528|
















|Col1|Selection Also see NumPy Arrays|
|---|---|
||`>>> s['b']`Get one element<br> `-5`<br>`>>> df[1:]`Get subset of a DataFrame<br>`    Country    Capital  Population`<br>`  1   India  New Delhi  1303171035`<br>`  2  Brazil   Brasília  207847528`<br>**   By Position**<br>`>>> df.iloc([0],[0])`Select single value by row &<br> `'Belgium'`                                                                         column<br>`>>> df.iat([0],[0])`<br> `'Belgium'` <br>**   By Label**<br>`>>> df.loc([0], ['Country'])`Select single value by row &<br> `'Belgium'`                                                                   column labels<br>`>>> df.at([0], ['Country'])`<br> `'Belgium'`<br>**   By Label/Position**<br>`>>> df.ix[2]`Select single row of<br>`  Country      Brazil`subset of rows<br>`  Capital    Brasília`<br>`  Population  207847528`<br>`>>> df.ix[:,'Capital']`Select a single column of <br>`  0     Brussels`                                                            subset of columns<br>`  1    New Delhi`<br>`  2     Brasília` <br>`>>> df.ix[1,'Capital']`Select rows and columns<br>`  'New Delhi'`<br>**   Boolean Indexing**<br>`>>> s[~(s > 1)]`Series`s `where value is not >1<br>`>>> s[(s < -1) | (s > 2)]           s`where value is <-1 or >2 <br>`>>> df[df['Population']>1200000000]`Use flter to adjust DataFrame<br>**   Seting**<br>`>>> s['a'] = 6`Set index`a` of Series`s` to 6<br>**Geting**<br>  <br>**Selecting, Boolean Indexing & Seting**|
|**Series**<br>**DataFrame**<br>4<br> 7<br>-5<br>3<br>d<br>c<br>b<br>a<br>A **one-dimensional** labeled array<br>capable of holding any data type<br>Index<br>Index<br>Columns<br>A **two-dimensional** labeled<br>data structure with columns<br>of potentially diferent types<br>**Pandas Data Structures**<br>`>>> s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])`<br>`>>> data = {'Country': ['Belgium', 'India', 'Brazil'],`<br> `'Capital': ['Brussels', 'New Delhi', 'Brasília'],`<br> `'Population': [11190846, 1303171035, 207847528]}`<br>`>>> df = pd.DataFrame(data,`<br>`                     columns=['Country', 'Capital', 'Population'])`<br>Belgium<br>Brussels<br>India<br>New Delhi<br>Brazil<br>Brasília<br>0<br>1<br>2<br>Country<br>Capital<br>11190846<br>1303171035<br>207847528<br>Population|**Series**<br>**DataFrame**<br>4<br> 7<br>-5<br>3<br>d<br>c<br>b<br>a<br>A **one-dimensional** labeled array<br>capable of holding any data type<br>Index<br>Index<br>Columns<br>A **two-dimensional** labeled<br>data structure with columns<br>of potentially diferent types<br>**Pandas Data Structures**<br>`>>> s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])`<br>`>>> data = {'Country': ['Belgium', 'India', 'Brazil'],`<br> `'Capital': ['Brussels', 'New Delhi', 'Brasília'],`<br> `'Population': [11190846, 1303171035, 207847528]}`<br>`>>> df = pd.DataFrame(data,`<br>`                     columns=['Country', 'Capital', 'Population'])`<br>Belgium<br>Brussels<br>India<br>New Delhi<br>Brazil<br>Brasília<br>0<br>1<br>2<br>Country<br>Capital<br>11190846<br>1303171035<br>207847528<br>Population|














## Python For Data Science Cheat Sheet
#### Scikit-Learn

Learn Python for data science **Interactively** at www.DataCamp.com






























|Classification Metrics|Col2|
|---|---|
|**   Accuracy Score**<br>`>>> knn.score(X_test, y_test)`<br>`>>> from sklearn.metrics import accuracy_score`<br>`>>> accuracy_score(y_test, y_pred)`<br>**  Classifcation Report**<br>>>> from sklearn.metrics import classifcation_report<br>>>> print(classifcation_report(y_test, y_pred))<br>**  Confusion Matrix**<br>`>>> from sklearn.metrics import confusion_matrix`<br>`>>> print(confusion_matrix(y_test, y_pred))`|Estimator score method<br>Metric scoring functions<br>Precision, recall, f1-score<br>and support|
|<br>**Regression Metrics**|<br>**Regression Metrics**|
|**   Mean Absolute Error**<br>`>>> from sklearn.metrics import mean_absolute_error`<br>`>>> y_true = [3, -0.5, 2]`<br>`>>> mean_absolute_error(y_true, y_pred)`<br>**   Mean Squared Error**<br>`>>> from sklearn.metrics import mean_squared_error`<br>`>>> mean_squared_error(y_test, y_pred)`<br>**   R² Score**<br>`>>> from sklearn.metrics import r2_score`<br>`>>> r2_score(y_true, y_pred)`|**   Mean Absolute Error**<br>`>>> from sklearn.metrics import mean_absolute_error`<br>`>>> y_true = [3, -0.5, 2]`<br>`>>> mean_absolute_error(y_true, y_pred)`<br>**   Mean Squared Error**<br>`>>> from sklearn.metrics import mean_squared_error`<br>`>>> mean_squared_error(y_test, y_pred)`<br>**   R² Score**<br>`>>> from sklearn.metrics import r2_score`<br>`>>> r2_score(y_true, y_pred)`|
|<br>**Clustering Metrics**|<br>**Clustering Metrics**|
|**   Adjusted Rand Index**<br>`>>> from sklearn.metrics import adjusted_rand_score`<br>`>>> adjusted_rand_score(y_true, y_pred)`<br>**  Homogeneity**<br>`>>> from sklearn.metrics import homogeneity_score`<br>`>>> homogeneity_score(y_true, y_pred)`<br> ** V-measure**<br>`>>> from sklearn.metrics import v_measure_score`<br>`>>> metrics.v_measure_score(y_true, y_pred)`|**   Adjusted Rand Index**<br>`>>> from sklearn.metrics import adjusted_rand_score`<br>`>>> adjusted_rand_score(y_true, y_pred)`<br>**  Homogeneity**<br>`>>> from sklearn.metrics import homogeneity_score`<br>`>>> homogeneity_score(y_true, y_pred)`<br> ** V-measure**<br>`>>> from sklearn.metrics import v_measure_score`<br>`>>> metrics.v_measure_score(y_true, y_pred)`|
|**Cross-Validation**<br> <br>|**Cross-Validation**<br> <br>|
|`>>> from sklearn.cross_validation import cross_val_score`<br>`>>> print(cross_val_score(knn, X_train, y_train, cv=4))`<br>`>>> print(cross_val_score(lr, X, y, cv=2))`|`>>> from sklearn.cross_validation import cross_val_score`<br>`>>> print(cross_val_score(knn, X_train, y_train, cv=4))`<br>`>>> print(cross_val_score(lr, X, y, cv=2))`|























**DataCamp**
**Learn Python for Data Science** **Interactively**




Matplotlib 2.0.0 - Updated on: 02/2017


|3<br>Python For Data Science Cheat Sheet Renderers & Visual Customizations<br>Bokeh Glyphs Grid Layout<br>Learn Bokeh Interactively at www.DataCamp.com, Scatet r Markers >>> from bokeh.layouts import gridplot<br>taught by Bryan Van de Ven, core contributor >>> p1.circle(np.array([1,2,3]), np.array([3,2,1]), >>> row1 = [p1,p2]<br>fill_color='white') >>> row2 = [p3]<br>>>> p2.square(np.array([1.5,3.5,5.5]), [1,4,3], >>> layout = gridplot([[p1,p2],[p3]])<br>color='blue', size=1)<br>Plotting With Bokeh Line Glyphs Tabbed Layout<br>>>> p1.line([1,2,3,4], [3,4,5,6], line_width=2)<br>The Python interactive visualization library Bokeh >>> p2.multi_line(pd.DataFrame([[1,2,3],[5,6,7]]), >>> from bokeh.models.widgets import Panel, Tabs<br>pd.DataFrame([[3,4,5],[3,2,1]]), >>> tab1 = Panel(child=p1, title="tab1")<br>enables high-performance visual presentation of color="blue") >>> tab2 = Panel(child=p2, title="tab2")<br>large datasets in modern web browsers. >>> layout = Tabs(tabs=[tab1, tab2])<br>Customized Glyphs Also see Data<br>Linked Plots<br>Bokeh’s mid-level general purpose bokeh.plotting Selection and Non-Selection Glyphs<br>interface is centered around two main components: data >>> p = figure(tools='box_select') Linked Axes<br>>>> p.circle('mpg', 'cyl', source=cds_df, >>> p2.x_range = p1.x_range<br>and glyphs. selection_color='red', >>> p2.y_range = p1.y_range<br>nonselection_alpha=0.1) Linked Brushing<br>+ = Hover Glyphs >>> p4 = figure(plot_width = 100,<br>tools='box_select,lasso_select')<br>>>> from bokeh.models import HoverTool >>> p4.circle('mpg', 'cyl', source=cds_df)<br>data glyphs plot >>> hover = HoverTool(tooltips=None, mode='vline') >>> p5 = figure(plot_width = 200,<br>>>> p3.add_tools(hover)<br>tools='box_select,lasso_select')<br>The basic steps to creating plots with the bokeh.plotting<br>>>> p5.circle('mpg', 'hp', source=cds_df)<br>interface are: Colormapping >>> layout = row(p4,p5)<br>1. Prepare some data: UAE usSiraope >>> from bokeh.models import CategoricalColorMapper<br>4<br>Python lists, NumPy arrays, Pandas DataFrames and other sequences of values >>> color_mapper = CategoricalColorMapper( Output & Export<br>factors=['US', 'Asia', 'Europe'],<br>2. Create a new plot<br>palette=['blue', 'red', 'green'])<br>3. Add renderers for your data, with visual customizations >>> p3.circle('mpg', 'cyl', source=cds_df, Notebook<br>4. Specify where to generate the output color=dict(field='origin',<br>transform=color_mapper), >>> from bokeh.io import output_notebook, show<br>5. Show or save the results legend='Origin') >>> output_notebook()<br>>>> from bokeh.plotting import figure<br>>>> from bokeh.io import output_fli e, show Legend Location HTML<br>>>> x = [1, 2, 3, 4, 5]<br>Step 1 Inside Plot Area Standalone HTML<br>>>> y = [6, 7, 2, 4, 5]<br>>>> p.legend.location = 'bottom_left' >>> from bokeh.embed import file_html<br>>>> p = figure(title="simple line example", Step 2<br>>>> from bokeh.resources import CDN<br>x_axis_label='x',<br>>>> html = file_html(p, CDN, "my_plot")<br>y_axis_label='y') Outside Plot Area<br>>>> p.line(x, y, legend="Temp.", line_width=2) Step 3 > >> >> > f rr 1o m = b po 2k .e ah s. tm eo rd ie sl ks ( ni pm .p ao rr rt a yL (e [g 1e ,n 2d ,3]), np.array([3,2,1]) >>> from bokeh.io import output_file, show<br>>>> output_file("lines.html") Step 4 >>> r2 = p2.line([1,2,3,4], [3,4,5,6]) >>> output_file('my_bar_chart.html', mode='cdn')<br>>>> show(p) Step 5 >>> legend = Legend(items=[("One" ,[p1, r1]),("Two",[r2])],<br>location=(0, -30)) Components<br>1 >>> p.add_layout(legend, 'right')<br>Data Also see Lists, NumPy & Pandas >>> from bokeh.embed import components<br>>>> script, div = components(p)<br>Legend Orientation<br>Under the hood, your data is converted to Column Data<br>PNG<br>Sources. You can also do this manually: >>> p.legend.orientation = "horizontal"<br>>>> import numpy as np >>> p.legend.orientation = "vertical" >>> from bokeh.io import export_png<br>>>> import pandas as pd Legend Background & Border >>> export_png(p, filename="plot.png")<br>>>> df = pd.DataFrame(np.array([[33.9,4,65, 'US'],<br>[32.4,4,66, 'Asia'],<br>[21.4,4,109, 'Europe']]), >>> p.legend.border_line_color = "navy" SVG<br>columns=['mpg','cyl', 'hp', 'origin'], >>> p.legend.background_fill_color = "white"<br>index=['Toyota', 'Fiat', 'Volvo']) >>> from bokeh.io import export_svgs<br>Rows & Columns Layout >>> p.output_backend = "svg"<br>>>> from bokeh.models import ColumnDataSource<br>>>> export_svgs(p, filename="plot.svg")<br>>>> cds_df = ColumnDataSource(df) Rows<br>2 >>> from bokeh.layouts import row 5<br>Plotting >>> layout = row(p1,p2,p3) Show or Save Your Plots<br>Columns<br>>>> from bokeh.plotting import figure >>> from bokeh.layouts import columns >>> show(p1) >>> show(layout)<br>>>> p1 = figure(plot_width=300, tools='pan,box_zoom') >>> layout = column(p1,p2,p3) >>> save(p1) >>> save(layout)<br>>>> p2 = figure(plot_width=300, plot_height=300, Nesting Rows & Columns<br>x_range=(0, 8), y_range=(0, 8)) >>>layout = row(column(p1,p2), p3) DataCamp<br>>>> p3 = figure() Learn Python for Data Science Interactively|Col2|
|---|---|
|**Python For Data Science** _Cheat Sheet_<br>Bokeh<br>Learn Bokeh**Interactively** at www.DataCamp.com, <br>taught by Bryan Van de Ven, core contributor<br>**Ploting With Bokeh**<br>**DataCamp**<br>**Learn Python for Data Science Interactively**<br>>>> from bokeh.plotting import fgure<br>>>> p1 = fgure(plot_width=300, tools='pan,box_zoom'`)`<br>>>> p2 = fgure(plot_width=300, plot_height=300,<br>               x_range=(0, 8), y_range=(0, 8))<br>>>> p3 = fgure()<br>>>> from bokeh.io import output_notebook, show<br>>>> output_notebook()<br>**         Ploting**<br>**    Components**<br>>>> from bokeh.embed import components<br>>>> script, div = components(p)<br>**                      Selection and Non-Selection Glyphs**<br>         >>> p = fgure(tools='box_select'`)`<br>         >>> p.circle(`'mpg'`, 'cyl', source=cds_df,<br>                      selection_color='red', <br>                      nonselection_alpha=0.1)<br>**                       Hover Glyphs**<br> >>> from bokeh.models import HoverTool<br> >>> hover = HoverTool(tooltips=None, mode='vline'`)`<br>         >>> p3.add_tools(hover)<br>**                       Colormapping**<br>  >>> from bokeh.models import CategoricalColorMapper<br> >>> color_mapper = CategoricalColorMapper(<br>                            factors=[`'US'`, 'Asia', 'Europe'],<br>                            palette=['blue', 'red',` 'green'])`<br>         >>> p3.circle(`'mpg'`, 'cyl', source=cds_df,<br>                      color=dict(feld=`'origin'`, <br>                                 transform=color_mapper),<br>                      legend=`'Origin')`<br> <br>>>> from bokeh.io import output_fle, show<br>>>> output_fle('my_bar_chart.html', mode='cdn'`)`<br>>>> from bokeh.models import ColumnDataSource<br>>>> cds_df = ColumnDataSource(df)<br>**         Data**<br>**Also seeLists, NumPy& Pandas**<br>Under the hood, your data is converted to Column Data<br>Sources. You can also do this manually:<br>**Customized Glyphs**<br>The Python interactive visualization library**Bokeh** <br>enables high-performance visual presentation of<br>large datasets in modern web browsers.<br>Bokeh’s mid-level general purpose`bokeh.plotting` <br>interface is centered around two main components: data<br>and glyphs.<br>The basic steps to creating plots with the`bokeh.plotting` <br>interface are:<br>    1. Prepare some data:<br>Python lists, NumPy arrays, Pandas DataFrames and other sequences of values<br>    2. Create a new plot<br>    3. Add renderers for your data, with visual customizations<br>    4. Specify where to generate the output<br>    5. Show or save the results<br>+<br>=<br>_        data                    glyphs             plot_<br>>>> from bokeh.plotting import fgure<br>>>> from bokeh.io import output_fle, show<br>>>> x = [1, 2, 3, 4, 5]<br>>>> y = [6, 7, 2, 4, 5]<br>>>> p = fgure(title="simple line example", <br>              x_axis_label='x', <br>              y_axis_label='y'`)`<br>>>> p.line(x, y, legend="Temp.", line_width=2)<br>>>> output_fle("lines.html"`)`<br>>>> show(p)<br>Step 4<br>Step 2<br>Step 1<br>Step 5<br>Step 3<br>**          Renderers & Visual Customizations**<br>2<br> **Scater Markers**<br>           >>> p1.circle(np.array([1,2,3]), np.array([3,2,1]),<br>                       fll_color='white'`)`<br>           >>> p2.square(np.array([1.5,3.5,5.5]), [1,4,3],<br>                       color='blue', size=1)<br> **Line Glyphs**<br>           >>> p1.line([1,2,3,4], [3,4,5,6], line_width=2)<br>           >>> p2.multi_line(pd.DataFrame([[1,2,3],[5,6,7]]),<br>                            pd.DataFrame([[3,4,5],[3,2,1]]),<br>                            color="blue"`)`<br>3<br>**Glyphs**<br>**         Output & Export**<br>4<br>1<br>>>> import numpy as np<br>>>> import pandas as pd<br>>>> df = pd.DataFrame(np.array([[33.9,4,65,`'US'`],<br>                                [32.4,4,66,'Asia'],<br>                                [21.4,4,109,'Europe']]),<br>                     columns=[`'mpg'`,'cyl', 'hp', 'origin'],<br>                     index=['Toyota', 'Fiat', 'Volvo'`])`<br>**Also see Data**<br>**HTML**<br>US<br>Asia<br>Europe<br>**Grid Layout**<br>>>> from bokeh.layouts import gridplot<br>>>> row1 = [p1,p2]<br>>>> row2 = [p3]<br>>>> layout = gridplot([[p1,p2],[p3]])<br>**Tabbed Layout**<br>>>> from bokeh.models.widgets import Panel, Tabs<br>>>> tab1 = Panel(child=p1, title=`"tab1")`<br>>>> tab2 = Panel(child=p2, title=`"tab2")`<br>>>> layout = Tabs(tabs=[tab1, tab2])<br>**Linked Plots**<br>**    Inside Plot Area**<br>>>> p.legend.location ='bottom_left'<br>**    Outside Plot Area**<br>>>> from bokeh.models import Legend<br>>>> r1 = p2.asterisk(np.array([1,2,3]), np.array([3,2,1])<br>>>> r2 = p2.line([1,2,3,4], [3,4,5,6])<br>>>> legend = Legend(items=[(`"One"` ,[p1, r1]),("Two",[r2])],<br>                    location=(0, -30))<br>>>> p.add_layout(legend,`'right')`<br>**Legend Location**<br>**    Linked Axes**<br>>>> p2.x_range = p1.x_range<br>>>> p2.y_range = p1.y_range<br>**    Linked Brushing**<br>>>> p4 = fgure(plot_width = 100,<br>               tools='box_select,lasso_select'`)`<br>>>> p4.circle(`'mpg'`, 'cyl', source=cds_df)<br>>>> p5 = fgure(plot_width = 200,<br>               tools='box_select,lasso_select'`)`<br>>>> p5.circle(`'mpg'`, `'hp'`, source=cds_df)<br>>>> layout = row(p4,p5)<br>>>> show(p1)              >>> show(layout)<br>>>> save(p1)              >>> save(layout)<br>**      Show or Save Your Plots**<br>5<br>>>> p.legend.orientation ="horizontal"<br>>>> p.legend.orientation ="vertical"<br>>>> p.legend.border_line_color ="navy"<br>>>> p.legend.background_fll_color ="white"<br>**Legend Orientation**<br>**Legend Background & Border**<br>**Rows & Columns Layout**<br>**    Rows**<br>>>> from bokeh.layouts import row<br>>>> layout = row(p1,p2,p3)<br>**   Columns**<br>>>> from bokeh.layouts import columns<br>>>> layout = column(p1,p2,p3)<br>**   Nesting Rows & Columns**<br>>>>layout = row(column(p1,p2), p3)<br>**PNG**<br>>>> from bokeh.io import export_png<br>>>> export_png(p, flename=`"plot.png")`<br>**SVG**<br>>>> from bokeh.io import export_svgs<br>>>> p.output_backend ="svg"<br>>>> export_svgs(p, flename="plot.svg"`)`<br>**Notebook**<br>**    Standalone HTML**<br>>>> from bokeh.embed import fle_html<br>>>> from bokeh.resources import CDN<br>>>> html = fle_html(p, CDN,"my_plot"`)`|**DataCamp**<br>**Learn Python for Data Science Interactively**<br>>>> from bokeh.io import output_notebook, show<br>>>> output_notebook()<br>**    Components**<br>>>> from bokeh.embed import components<br>>>> script, div = components(p)<br>>>> from bokeh.io import output_fle, show<br>>>> output_fle('my_bar_chart.html', mode='cdn'`)`<br>**         Output & Export**<br>4<br>**HTML**<br>>>> show(p1)              >>> show(layout)<br>>>> save(p1)              >>> save(layout)<br>**      Show or Save Your Plots**<br>5<br>**PNG**<br>>>> from bokeh.io import export_png<br>>>> export_png(p, flename=`"plot.png")`<br>**SVG**<br>>>> from bokeh.io import export_svgs<br>>>> p.output_backend ="svg"<br>>>> export_svgs(p, flename="plot.svg"`)`<br>**Notebook**<br>**    Standalone HTML**<br>>>> from bokeh.embed import fle_html<br>>>> from bokeh.resources import CDN<br>>>> html = fle_html(p, CDN,"my_plot"`)`|
|>>> from bokeh.plotting import fgure<br>>>> p1 = fgure(plot_width=300, tools='pan,box_zoom'`)`<br>>>> p2 = fgure(plot_width=300, plot_height=300,<br>               x_range=(0, 8), y_range=(0, 8))<br>>>> p3 = fgure()<br> <br>|>>> from bokeh.plotting import fgure<br>>>> p1 = fgure(plot_width=300, tools='pan,box_zoom'`)`<br>>>> p2 = fgure(plot_width=300, plot_height=300,<br>               x_range=(0, 8), y_range=(0, 8))<br>>>> p3 = fgure()<br> <br>|


