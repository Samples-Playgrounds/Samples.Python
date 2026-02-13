# **Python Basics**

Learn More Python for Data Science Interactively at <a href="https://www.datacamp.com">www.datacamp.com</a>

![](_page_0_Picture_3.jpeg)

# Variables and Data Types

# Variable Assignment

| >>> | x=5 |
|-----|-----|
| >>> | X   |
| 5   |     |

## Calculations With Variables

| >>> x+2        | Sum of two variables            |
|----------------|---------------------------------|
| 7<br>>>> x-2   | Subtraction of two variables    |
| 3              | Subtraction of two variables    |
| >>> x*2        | Multiplication of two variables |
| 10<br>>>> x**2 | Exponentiation of a variable    |
| 25             |                                 |
| >>> x%2        | Remainder of a variable         |
| 1              |                                 |
| >>> x/float(2) | Division of a variable          |
| 2.5            |                                 |

# Types and Type Conversion

| str()   | '5', '3.45', 'True' | Variables to strings  |
|---------|---------------------|-----------------------|
| int()   | 5, 3, 1             | Variables to integers |
| float() | 5.0, 1.0            | Variables to floats   |
| bool()  | True, True, True    | Variables to booleans |

# **Asking For Help**

>>> help(str)

## Strings

```
>>> my string = 'thisStringIsAwesome'
>>> my string
'thisStringTsAwesome'
```

## **String Operations**

```
>>> my string * 2
 'thisStringIsAwesomethisStringIsAwesome'
>>> my string + 'Innit'
 'thisStringIsAwesomeInnit'
>>> 'm' in mv string
```

#### Lists

```
>>> a = 'is'
>>> b = 'nice'
>>> my list = ['my', 'list', a, b]
>>> my list2 = [[4,5,6,7], [3,4,5,6]]
```

### Selecting List Elements

Also see NumPy Arrays

#### Subset

| >>>  | my_ | _list[1] |
|------|-----|----------|
| >>>  | my_ | list[-3] |
| Clic |     | _        |

- >>> my list[1:3] >>> mv list[1:] >>> my list[:3] >>> my list[:]
- **Subset Lists of Lists** >>> my list2[1][0]
- >>> my list2[1][:2]

### Index starts at o

## Select item at index 1 Select 3rd last item

Select items at index 1 and 2 Select items after index o Select items before index 3 Copy my list

mv list[list][itemOfList]

## **List Operations**

```
>>> my list + my list
['my', 'list', 'is', 'nice', 'my', 'list', 'is', 'nice']
>>> my list * 2
['my', 'list', 'is', 'nice', 'my', 'list', 'is', 'nice']
>>> my list2 > 4
```

#### List Methods

| >>> | my list.index(a)                 | Get the index of an item |
|-----|----------------------------------|--------------------------|
| >>> | <pre>my_list.count(a)</pre>      | Count an item            |
| >>> | <pre>my_list.append('!')</pre>   | Append an item at a time |
| >>> | <pre>my_list.remove('!')</pre>   | Remove an item           |
| >>> | del(my_list[0:1])                | Remove an item           |
| >>> | <pre>my_list.reverse()</pre>     | Reverse the list         |
| >>> | <pre>my_list.extend('!')</pre>   | Append an item           |
| >>> | <pre>my_list.pop(-1)</pre>       | Remove an item           |
| >>> | <pre>my_list.insert(0,'!')</pre> | Insert an item           |
| >>> | <pre>my_list.sort()</pre>        | Sort the list            |

# String Operations

#### Index starts at o

```
>>> my string[3]
>>> my string[4:9]
```

# String Methods

| String Methods                  |                         |
|---------------------------------|-------------------------|
|                                 |                         |
| >>> my_string.upper()           | String to uppercase     |
| >>> my string.lower()           | String to lowercase     |
| >>> my string.count('w')        | Count String elements   |
| >>> my_string.replace('e', 'i') | Replace String elements |
| >>> my string.strip()           | Strip whitespaces       |

#### Libraries

#### **Import libraries**

>>> import numpy

>>> import numpy as np Selective import

>>> from math import pi

![](_page_0_Picture_44.jpeg)

![](_page_0_Picture_45.jpeg)

Machine learning

![](_page_0_Picture_47.jpeg)

\* matplotlib 2D plotting

# **Install Python**

![](_page_0_Picture_50.jpeg)

Leading open data science platform powered by Python

![](_page_0_Picture_52.jpeg)

with Anaconda

![](_page_0_Picture_54.jpeg)

Create and share documents with live code. visualizations text

# **Numpy Arrays**

### Also see Lists

```
>>>  my list = [1, 2, 3, 4]
>>> my array = np.array(my list)
>>> my 2darray = np.array([[1,2,3],[4,5,6]])
```

# **Selecting Numpy Array Elements**

### Index starts at o

# Subset >>> my array[1]

Slice

```
>>> my array[0:2]
  arrav([1, 2])
Subset 2D Numpy arrays
>>> my 2darray[:,0]
  array([1, 4])
```

Select item at index 1

Select items at index o and 1

my 2darray[rows, columns]

# Numpy Array Operations

```
>>> mv arrav > 3
 array([False, False, False, True], dtype=bool)
>>> my array * 2
  array([2, 4, 6, 8])
>>> my array + np.array([5, 6, 7, 8])
 array([6, 8, 10, 12])
```

# Numpy Array Functions

| >>> my_array.shape            | Get the dimensions of the arra |
|-------------------------------|--------------------------------|
| >>> np.append(other_array)    | Append items to an array       |
| >>> np.insert(my_array, 1, 5) | Insert items in an array       |
| >>> np.delete(my_array,[1])   | Delete items in an array       |
| >>> np.mean(my_array)         | Mean of the array              |
| >>> np.median(my_array)       | Median of the array            |
| >>> my_array.corrcoef()       | Correlation coefficient        |
| >>> np.std(my_array)          | Standard deviation             |
|                               |                                |

# **Python For Data Science** Cheat Sheet Jupyter Notebook

Learn More Python for Data Science Interactively at www.DataCamp.com

![](_page_1_Picture_2.jpeg)

![](_page_1_Figure_3.jpeg)

## Writing Code And Text

Add new cell above the

current one

Code and text are encapsulated by 3 basic cell types: markdown cells, code cells, and raw NBConvert cells.

#### Edit Cells

![](_page_1_Figure_7.jpeg)

Cell

Insert Cell Below

Add new cell below the

current one

![](_page_1_Figure_8.jpeg)

## Widgets

Notebook widgets provide the ability to visualize and control changes in your data, often as a control like a slider, textbox, etc.

You can use them to build interactive GUIs for your notebooks or to synchronize stateful and stateless information between Python and JavaScript.

![](_page_1_Figure_12.jpeg)

#### **Command Mode:**

![](_page_1_Figure_14.jpeg)

![](_page_1_Figure_15.jpeg)

In [ ]: |

View Cells

Toggle display of Jupyter

Toggle line numbers

logo and filename

in cells

![](_page_1_Figure_16.jpeg)

Insert

Toggle Header

Cell Toolbar

Toggle Toolbar • \*

Toggle Line Numbers

Toggle display of toolbar

action icons:

- None

- Tags

Toggle display of cell

Edit metadata

- Slideshow

Attachments

Raw cell format

- 1. Save and checkpoint
- 2. Insert cell below 3. Cut cell
- 4. Copy cell(s)
- 5. Paste cell(s) below
- 6. Move cell up
- 7. Move cell down
- 8. Run current cell

- 9. Interrupt kernel
- 10. Restart kernel
- 11. Display characteristics 12. Open command palette
- 13. Current kernel
- 14. Kernel status
- 15. Log out from notebook server

## **Asking For Help**

![](_page_1_Figure_33.jpeg)

**DataCamp** Learn Python for Data Science Interactively

![](_page_1_Picture_35.jpeg)

# NumPy Basics

Learn Python for Data Science Interactively at <a href="https://www.DataCamp.com">www.DataCamp.com</a>

![](_page_2_Picture_3.jpeg)

# NumPv

The NumPy library is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.

Use the following import convention: >>> import numpy as np

![](_page_2_Picture_7.jpeg)

# NumPy Arrays

![](_page_2_Figure_9.jpeg)

# **Creating Arrays**

```
>>> a = np.array([1,2,3])
>>> b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
>>> c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],
                 dtype = float)
```

#### Initial Placeholders

| >>> np.ones((2,3,4),dtype=np.int16)                                          | Create an array of zeros<br>Create an array of ones<br>Create an array of evenly                                       |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| >>> np.linspace(0,2,9)                                                       | spaced values (step value) Create an array of evenly spaced values (number of samples)                                 |
| >>> e = np.full((2,2),7)<br>>>> f = np.eye(2)<br>>>> np.random.random((2,2)) | Create a constant array<br>Create a 2X2 identity matrix<br>Create an array with random values<br>Create an empty array |

# 1/0

# Saving & Loading On Disk

```
>>> np.save('mv arrav', a)
>>> np.savez('array.npz', a, b)
>>> np.load('my array.npy')
```

## Saving & Loading Text Files

| >>> | np.loadtxt("myfile.txt")                    |
|-----|---------------------------------------------|
| >>> | np.genfromtxt("my file.csv", delimiter=',') |
| >>> | np.savetxt("mvarrav.txt", a, delimiter=" ") |

# **Data Types**

|                 | Ct. Landau .                               |
|-----------------|--------------------------------------------|
| >>> np.int64    | Signed 64-bit integer types                |
| >>> np.float32  | Standard double-precision floating point   |
| >>> np.complex  | Complex numbers represented by 128 floats  |
| >>> np.bool     | Boolean type storing TRUE and FALSE values |
| >>> np.object   | Python object type                         |
| >>> np.string_  | Fixed-length string type                   |
| >>> np.unicode_ | Fixed-length unicode type                  |

## Inspecting Your Array

| >>> | a.shape       | Array dimensions                     |
|-----|---------------|--------------------------------------|
| >>> | len(a)        | Length of array                      |
| >>> | b.ndim        | Number of array dimensions           |
| >>> | e.size        | Number of array elements             |
| >>> | b.dtype       | Data type of array elements          |
| >>> | b.dtype.name  | Name of data type                    |
| >>> | b.astype(int) | Convert an array to a different type |

# Asking For Help

>>> np.info(np.ndarrav.dtvpe)

# **Array Mathematics**

# **Arithmetic Operations**

| >>> q = a - b                                            | Subtraction                    |
|----------------------------------------------------------|--------------------------------|
| array([[-0.5, 0. , 0.],                                  |                                |
| [-3. , -3. , -3. ]])                                     |                                |
| >>> np.subtract(a,b)                                     | Subtraction                    |
| >>> b + a                                                | Addition                       |
| array([[ 2.5, 4. , 6. ],                                 |                                |
| [5., 7., 9.]])                                           |                                |
| >>> np.add(b,a)                                          | Addition                       |
| >>> a / b                                                | Division                       |
| array([[ 0.66666667, 1. , 1. ]]<br>[ 0.25 , 0.4 , 0.5 ]] |                                |
| >>> np.divide(a,b)                                       | Division                       |
| >>> a * b                                                | Multiplication                 |
| array([[ 1.5, 4., 9.],                                   | a.c.p.i.cac.o.i                |
| [ 4., 10., 18.]])                                        |                                |
| >>> np.multiply(a,b)                                     | Multiplication                 |
| >>> np.exp(b)                                            | Exponentiation                 |
| >>> np.sqrt(b)                                           | Square root                    |
| >>> np.sin(a)                                            | Print sines of an array        |
| >>> np.cos(b)                                            | Element-wise cosine            |
| >>> np.log(a)                                            | Element-wise natural logarithm |
| >>> e.dot(f)                                             | Dot product                    |
| array([[ 7., 7.],                                        |                                |
| [ 7., 7.]])                                              |                                |

## Comparison

| t-wise comparison |
|-------------------|
| t-wise comparison |
| vise comparison   |
|                   |

# Aggregate Functions

| >>> a.sum()          | Array-wise sum                 |
|----------------------|--------------------------------|
| >>> a.min()          | Array-wise minimum value       |
| >>> b.max(axis=0)    | Maximum value of an array row  |
| >>> b.cumsum(axis=1) | Cumulative sum of the elements |
| >>> a.mean()         | Mean                           |
| >>> b.median()       | Median                         |
| >>> a.corrcoef()     | Correlation coefficient        |
| >>> np.std(b)        | Standard deviation             |

# **Copying Arrays**

| >>> h = a.view() | Create a view of the array with the same data |
|------------------|-----------------------------------------------|
| >>> np.copy(a)   | Create a copy of the array                    |
| >>> h = a.copy() | Create a deep copy of the array               |

# Sorting Arrays

| >>> a.sort()       | Sort an array                        |
|--------------------|--------------------------------------|
| >>> c.sort(axis=0) | Sort the elements of an array's axis |

# Subsetting, Slicing, Indexing

Subsetting

>>> a[2]

6.0 Slicing

>>> b[1,2]

>>> a[0:21

>>> b[:11

array([1, 2])

arrav([ 2., 5.1)

array([[1.5, 2., 3.]])

array([[[ 3., 2., 1.],

[4., 5., 6.]]])

>>> b[[1, 0, 1, 0], [0, 1, 2, 0]]

array([ 4. , 2. , 6. , 1.5]) >>> b[[1, 0, 1, 0]][:,[0,1,2,0]]

array([[4.,5.,6.,4.],

1 2 3

>>> b[0:2,1]

>>> c[1,...]

>>> a[a<2]

array([1])

Fancy Indexing

>>> a[ : :-1]
array([3, 2, 1])

**Boolean Indexing** 

```
1 2 3
            Select the element at the 2nd index
1.5 2 3
            Select the element at row o column 2
             (equivalent to b[1][2])
```

Select items at index 0 and 1

Select items at rows 0 and 1 in column 1

Also see Lists

Select all items at row o (equivalent to b[0:1, :]) Same as [1.:.:]

Reversed array a

Select elements from a less than 2

Select elements (1,0), (0,1), (1,2) and (0,0)

Select a subset of the matrix's rows and columns

# **Array Manipulation**

#### Transposing Array >>> i = np.transpose(b) >>> i.T

#### **Changing Array Shape** >>> b.ravel()

>>> g.reshape(3.-2) Adding/Removing Elements

>>> h.resize((2,6)) >>> np.append(h,q) >>> np.insert(a, 1, 5) >>> np.delete(a,[1])

#### **Combining Arrays** >>> np.concatenate((a,d),axis=0)

```
array([ 1, 2, 3, 10, 15, 20])
>>> np.vstack((a,b))
 array([[ 1. , 2. , 3. ], [ 1.5, 2. , 3. ], [ 4. , 5. , 6. ]])
>>> np.r [e,f]
>>> np.hstack((e,f))
 array([[ 7., 7., 1., 0.],
         [ 7., 7., 0., 1.]])
>>> np.column stack((a,d))
 arrav([[ 1, 10],
          2, 15],
         [ 3, 2011)
>>> np.c [a,d]
```

## **Splitting Arrays**

```
>>> np.hsplit(a,3)
 [array([1]),array([2]),array([3])]
>>> np.vsplit(c,2)
[array([[[ 1.5, 2., 1. ],
```

[4., 5., 6.]]])]

Permute array dimensions Permute array dimensions

Flatten the array Reshape, but don't change data

Return a new array with shape (2,6) Append items to an array Insert items in an array

Concatenate arrays

Delete items from an array

Stack arrays vertically (row-wise)

Stack arrays vertically (row-wise) Stack arrays horizontally (column-wise)

Create stacked column-wise arrays

Create stacked column-wise arrays

Split the array horizontally at the 3rd

Split the array vertically at the 2nd index

![](_page_2_Picture_64.jpeg)

# **Python For Data Science** Cheat Sheet SciPv - Linear Algebra

Learn More Python for Data Science Interactively at www.datacamp.com

![](_page_3_Picture_2.jpeg)

# SciPv

The **SciPy** library is one of the core packages for scientific computing that provides mathematical algorithms and convenience functions built on the NumPy extension of Python.

![](_page_3_Picture_5.jpeg)

# Interacting With NumPy

#### Also see NumP

```
>>> import numpy as np
>>> a = np.arrav([1,2,3])
>>> b = np.array([(1+5j,2j,3j), (4j,5j,6j)])
>>> c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]])
```

#### **Index Tricks**

| >>> | np.mgrid[0:5,0:5] | Create a dense meshgrid            |
|-----|-------------------|------------------------------------|
| >>> |                   | Create an open meshgrid            |
| >>> |                   | Stack arrays vertically (row-wise) |
| >>> | np.c_[b,c]        | Create stacked column-wise arrays  |

# Shape Manipulation

|     | The second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second secon |                                               |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| >>> | np.transpose(b)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Permute array dimensions                      |
| >>> | b.flatten()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Flatten the array                             |
| >>> | np.hstack((b,c))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Stack arrays horizontally (column-wise)       |
| >>> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Stack arrays vertically (row-wise)            |
| >>> | np.hsplit(c,2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Split the array horizontally at the 2nd index |
| >>> | np.vpslit(d,2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Split the array vertically at the 2nd index   |

# **Polynomials**

| >>> | from numpy import polyid |                            |
|-----|--------------------------|----------------------------|
| >>> | p = poly1d([3,4,5])      | Create a polynomial object |

# **Vectorizing Functions**

```
>>> def myfunc(a):
         if a < 0:
           return a*2
         else.
           return a/2
>>> np vectorize(myfunc)
                                     Vectorize functions
```

# Type Handling

| >>> | > np.real(c)                   | Return the real part of the array elements      |
|-----|--------------------------------|-------------------------------------------------|
| >>> | > np.imag(c)                   | Return the imaginary part of the array element  |
| >>> | > np.real if close(c,tol=1000) | Return a real array if complex parts close to o |
| >>> | > np.cast['f'](np.pi)          | Cast object to a data type                      |

# Other Useful Functions

| >>> | np.angle(b,deg=True)           | Return the angle of the complex argument            |
|-----|--------------------------------|-----------------------------------------------------|
| >>> | g = np.linspace(0,np.pi,num=5) | Create an array of evenly spaced values             |
| >>> | g [3:] += np.pi                | (number of samples)                                 |
| >>> | np.unwrap(g)                   | Unwrap                                              |
| >>> | np.logspace(0,10,3)            | Create an array of evenly spaced values (log scale) |
| >>> | np.select([c<4],[c*2])         | Return values from a list of arrays depending on    |
|     | _                              | conditions                                          |
| >>> | misc.factorial(a)              | Factorial                                           |
| >>> | misc.comb(10,3,exact=True)     | Combine N things taken at k time                    |
| >>> | misc.central_diff_weights(3)   | Weights for Np-point central derivative             |
| >>> | misc.derivative(myfunc, 1.0)   | Find the n-th derivative of a function at a point   |

# Linear Algebra

```
You'll use the linal and sparse modules. Note that scipy, linal acontains and expands on numby, linal acontains and expands on numby, linal acontains and expands on numby, linal acontains and expands on numby, linal acontains and expands on numby, linal acontains and expands on numby, linal acontains and expands on numby, linal acontains and expands on numby, linal acontains acontains and expands on numby, linal acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains acontains
```

```
>>> from scipy import linalg, sparse
```

# Creating Matrices

```
>>> A = np.matrix(np.random.random((2,2)))
>>> B = np.asmatrix(b)
>>> C = np.mat(np.random.random((10,5)))
>>> D = np.mat([[3,4], [5,6]])
```

#### **Basic Matrix Routines**

### Inverse

| >>> | A.I           | Ir |
|-----|---------------|----|
| >>> | linalg.inv(A) | lr |
| >>> | A.T           | Ti |
| >>> | A.H           | С  |
| >>> | np.trace(A)   | Ti |

#### Norm

| >>> | linalg.norm(A)        |
|-----|-----------------------|
| >>> | linalg.norm(A,1)      |
| >>> | linalg.norm(A,np.inf) |

#### Rank

>>> np.linalg.matrix rank(C)

#### Determinant

>>> linalg.det(A)

# Solving linear problems

| >>> | linalg.solve(A,b) |
|-----|-------------------|
| >>> | E = np.mat(a).T   |
|     | linalg.lstsq(D,E) |
|     |                   |

#### Generalized inverse >>> linalg.pinv(C)

| >>> | linalg.pinv2(C) |
|-----|-----------------|

nverse

nverse Tranpose matrix Conjugate transposition

Frobenius norm L1 norm (max column sum) L inf norm (max row sum)

Matrix rank

Determinant

Solver for dense matrices Solver for dense matrices Least-squares solution to linear matrix equation

Compute the pseudo-inverse of a matrix (least-squares solver) Compute the pseudo-inverse of a matrix

(SVD)

# Creating Sparse Matrices

| >>> $F = np.eye(3, k=1)$       | Create a 2X2 identity matrix    |
|--------------------------------|---------------------------------|
| >>> G = np.mat(np.identity(2)) | Create a 2x2 identity matrix    |
| >>> C[C > 0.5] = 0             |                                 |
| >>> H = sparse.csr_matrix(C)   | Compressed Sparse Row matrix    |
| >>> I = sparse.csc matrix(D)   | Compressed Sparse Column matrix |
| >>> J = sparse.dok matrix(A)   | Dictionary Of Keys matrix       |
| >>> E.todense()                | Sparse matrix to full matrix    |
| >>> sparse.isspmatrix_csc(A)   | Identify sparse matrix          |

# Sparse Matrix Routines

# >>> sparse.linalg.inv(I)

| _    | _ |  |
|------|---|--|
| Norm |   |  |

>>> sparse.linalg.norm(I) Solving linear problems

>>> sparse.linalg.spsolve(H,I)

Inverse

Norm

Solver for sparse matrices

#### Sparse Matrix Functions

| > sparse.linalg.expm(I) | Sparse matrix exponential |
|-------------------------|---------------------------|
|                         |                           |

#### **Matrix Functions**

## Addition

| >>> np.add(A,D) |  |
|-----------------|--|
| Subtraction     |  |

# >>> np.subtract(A,D)

Division >>> np.divide(A,D)

## Multiplication

```
>>> np.multiply(D,A)
                                        Multiplication
>>> np.dot(A,D)
                                        Dot product
>>> np.vdot(A,D)
                                        Inner product
>>> np.inner(A,D)
>>> np.outer(A,D)
                                        Outer product
>>> np.tensordot(A,D)
>>> np.kron(A,D)
```

#### **Exponential Functions** >>> linalq.expm(A)

```
>>> linalg.expm2(A)
>>> linalg.expm3(D)
```

### **Logarithm Function**

>>> linalg.logm(A)

#### **Trigonometric Tunctions** >>> linalg.sinm(D)

```
>>> linalg.cosm(D)
>>> linalg.tanm(A)
```

#### Hyperbolic Trigonometric Functions

```
>>> linalg.sinhm(D)
>>> linalg coshm(D)
>>> linalg.tanhm(A)
```

#### **Matrix Sign Function** >>> np.sigm(A)

# **Matrix Square Root**

#### >>> linalg.sgrtm(A) **Arbitrary Functions**

| >>> | linalg. | funm(A, | lambda | x: | х*х |
|-----|---------|---------|--------|----|-----|

Vector dot product Tensor dot product Kronecker product

Addition

Division

Subtraction

#### Matrix exponential Matrix exponential (Taylor Series) Matrix exponential (eigenvalue decomposition)

Also see NumPv

### Matrix logarithm

Matrix sine Matrix cosine Matrix tangent

Hypberbolic matrix sine Hyperbolic matrix cosine Hyperbolic matrix tangent

Matrix sign function

Matrix square root

Evaluate matrix function

# **Decompositions**

# **Eigenvalues and Eigenvectors**

|   |     | ia, v - iinaig.eig |
|---|-----|--------------------|
|   | >>> | 11, 12 = 1a        |
|   | >>> | v[:,0]             |
| J | >>> | v[:,1]             |
|   | >>> | linalg.eigvals(A)  |

# Singular Value Decomposition

|  | >>> | U,s,Vh = linalg.svd(B) |
|--|-----|------------------------|
|  | >>> | M,N = B.shape          |

# >>> Sig = linalg.diagsvd(s,M,N)

# LU Decomposition

| >> | >> | Р, Ь, | U = | = 1 | ına. | Lg. | ⊥u | (C |
|----|----|-------|-----|-----|------|-----|----|----|
|----|----|-------|-----|-----|------|-----|----|----|

Solve ordinary or generalized eigenvalue problem for square matrix Unpack eigenvalues First eigenvector

Second eigenvector Unpack eigenvalues

Singular Value Decomposition (SVD)

Construct sigma matrix in SVD

LU Decomposition

## Sparse Matrix Decompositions

| >>> | <pre>la, v = sparse.linalg.eigs(F,1)</pre> |
|-----|--------------------------------------------|
| >>> | sparse linala syds (H 2)                   |

Eigenvalues and eigenvectors

# Asking For Help

>>> help(scipy.linalg.diagsvd) >>> np.info(np.matrix)

![](_page_3_Picture_107.jpeg)

![](_page_3_Picture_108.jpeg)

# Pandas Basics

Learn Python for Data Science Interactively at www.DataCamp.com

![](_page_4_Picture_3.jpeg)

### **Pandas**

The **Pandas** library is built on NumPy and provides easy-to-use data structures and data analysis tools for the Python programming language. pandas 🖳

# Use the following import convention:

>>> import pandas as pd

# **Pandas Data Structures**

### Series

A one-dimensional labeled array capable of holding any data type

![](_page_4_Picture_11.jpeg)

```
>>> s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
```

### DataFrame

![](_page_4_Picture_14.jpeg)

A two-dimensional labeled data structure with columns of potentially different types

```
>>> data = {'Country': ['Belgium', 'India', 'Brazil'],
           'Capital': ['Brussels', 'New Delhi', 'Brasília'],
           'Population': [11190846, 1303171035, 207847528]}
>>> df = pd.DataFrame(data,
                     columns=['Country', 'Capital', 'Population'])
```

# **Asking For Help**

>>> help(pd.Series.loc)

# Selection

Also see NumPy Arrays

## Getting

```
>>> s['b']
>>> df[1:1
   Country
             Capital Population
 1 India New Delhi 1303171035
 2 Brazil
            Brasília 207847528
```

#### Get one element

Get subset of a DataFrame

# Selecting, Boolean Indexing & Setting

### **By Position**

```
>>> df.iloc([0],[0])
 'Belaium'
>>> df.iat([0],[0])
 'Belgium'
```

#### **By Label**

```
>>> df.loc([0], ['Country'])
 'Belaium'
>>> df.at([0], ['Country'])
 'Belgium'
```

### By Label/Position

```
>>> df.ix[2]
 Country
             Brazil
 Capital Brasília
 Population 207847528
>>> df.ix[:.'Capital']
       Brussels
      New Delhi
      Brasília
>>> df.ix[1,'Capital']
```

'New Delhi'

# **Boolean Indexing**

| Canton |                                |  |  |  |
|--------|--------------------------------|--|--|--|
| >>>    | df[df['Population']>1200000000 |  |  |  |
| >>>    | s[(s < -1)   (s > 2)]          |  |  |  |
| >>>    | s[~(s > 1)]                    |  |  |  |

# Setting

>>> s['a'] = 6

## Select single value by row & column

Select single value by row & column labels

#### Select single row of subset of rows

Select a single column of subset of columns

Select rows and columns

# Series s where value is not >1 s where value is <-1 or >2

Use filter to adjust DataFrame

Set index a of Series s to 6

# Read and Write to SQL Query or Database Table

| >>> | pd.read_csv('file.csv', | header=None, | nrows=5) |
|-----|-------------------------|--------------|----------|
| >>> | df.to csv('myDataFrame  | e.csv')      |          |

#### Read and Write to Excel

Read and Write to CSV

```
>>> pd.read excel('file.xlsx')
>>> pd.to excel('dir/myDataFrame.xlsx', sheet name='Sheet1')
Read multiple sheets from the same file
```

| - |     |      | •                           |
|---|-----|------|-----------------------------|
| ŀ | >>> | xlsx | = pd.ExcelFile('file.xls')  |
| 1 | /// | df - | nd read excel/vlev 'Sheet1' |

```
>>> from sqlalchemy import create engine
```

| >>> | engine = | = create_ | _engine | ∍('sql | ite | ::///:me | emoi | ry:')   |
|-----|----------|-----------|---------|--------|-----|----------|------|---------|
| >>> | pd.read  | sql("SEI  | LECT *  | FROM   | my  | table;"  | ', ( | engine) |

- >>> pd.read sql table('my table', engine)
- >>> pd.read sgl guery("SELECT \* FROM my table;", engine)

read sql() is a convenience wrapper around read sql table() and read sql query()

>>> pd.to sql('myDf', engine)

## **Dropping**

| >>> | s.drop(['a', 'c'])                    | Drop values from rows (axis=0)   |
|-----|---------------------------------------|----------------------------------|
| >>> | <pre>df.drop('Country', axis=1)</pre> | Drop values from columns(axis=1) |

### **Sort & Rank**

```
>>> df.sort index()
                                        Sort by labels along an axis
>>> df.sort values(by='Country')
                                        Sort by the values along an axis
>>> df.rank()
                                        Assign ranks to entries
```

# Retrieving Series/DataFrame Information

### **Basic Information**

```
>>> df.shape
                             (rows columns)
>>> df.index
                             Describe index
>>> df.columns
                             Describe DataFrame columns
                             Info on DataFrame
>>> df.info()
                             Number of non-NA values
>>> df.count()
```

### Summary

```
Sum of values
>>> df.sum()
>>> df.cumsum()
                                Cummulative sum of values
                                Minimum/maximum values
>>> df.min()/df.max()
                               Minimum/Maximum index value
>>> df.idxmin()/df.idxmax(
>>> df.describe()
                                Summary statistics
                                Mean of values
>>> df.mean()
                                Median of values
>>> df.median()
```

# **Applying Functions**

```
>>> f = lambda x: x*2
>>> df.apply(f)
                            Apply function
>>> df.applymap(f)
                            Apply function element-wise
```

# **Data Alignment**

# Internal Data Alignment

NA values are introduced in the indices that don't overlap:

```
>>> s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
>>> s + s3
       10 0
       NaN
       5.0
       7 0
```

# **Arithmetic Operations with Fill Methods**

You can also do the internal data alignment yourself with the help of the fill methods:

```
>>> s.add(s3, fill value=0)
 a 10.0
 h
     -5.0
     5.0
 d
     7.0
>>> s.sub(s3, fill value=2)
>>> s.div(s3, fill value=4)
>>> s.mul(s3, fill value=3)
```

# **DataCamp**

![](_page_4_Picture_76.jpeg)

# Scikit-Learn

Learn Python for data science Interactively at www.DataCamp.com

![](_page_5_Picture_3.jpeg)

# Scikit-learn

Scikit-learn is an open source Python library that implements a range of machine learning, preprocessing, cross-validation and visualization algorithms using a unified interface.

![](_page_5_Picture_6.jpeg)

## A Basic Example

```
>>> from sklearn import neighbors, datasets, preprocessing
>>> from sklearn.model selection import train test split
>>> from sklearn.metrics import accuracy score
>>> iris = datasets.load iris()
>>> X, y = iris.data[:, :2], iris.target
>>> X_train, X_test, y_train, y_test= train_test_split(X, y, random_state=33)
>>> scaler = preprocessing.StandardScaler().fit(X_train)
>>> X train = scaler.transform(X train)
>>> X test = scaler.transform(X test)
>>> knn = neighbors.KNeighborsClassifier(n_neighbors=5)
>>> knn.fit(X train, y train)
>>> y pred = knn.predict(X test)
>>> accuracy score(y test, y pred)
```

# Loading The Data

#### Also see NumPy & Pandas

Your data needs to be numeric and stored as NumPy arrays or SciPy sparse matrices. Other types that are convertible to numeric arrays, such as Pandas DataFrame, are also acceptable.

```
>>> import numpy as np
>>> X = np.random.random((10,5))
>>> y = np.array(['M','M','F','F','M','F','M','M','F','F',
>>> X[X < 0.7] = 0
```

# Training And Test Data

```
>>> from sklearn.model selection import train test split
>>> X train, X test, y train, y test = train test split(X,
                                                 random state=0)
```

# **Create Your Model**

## Supervised Learning Estimators

### Linear Regression

```
>>> from sklearn.linear model import LinearRegression
>>> lr = LinearRegression(normalize=True)
```

#### Support Vector Machines (SVM)

```
>>> from sklearn.svm import SVC
>>> svc = SVC(kernel='linear')
```

>>> from sklearn.naive bayes import GaussianNB >>> gnb = GaussianNB()

#### KNN

>>> from sklearn import neighbors >>> knn = neighbors.KNeighborsClassifier(n neighbors=5)

### Unsupervised Learning Estimators

#### **Principal Component Analysis (PCA)**

>>> from sklearn decomposition import PCA >>> pca = PCA(n components=0.95)

#### K Means

>>> from sklearn.cluster import KMeans >>> k means = KMeans(n clusters=3, random state=0)

# **Model Fitting**

### Supervised learning

>>> lr.fit(X, y) >>> knn.fit(X train, v train) >>> svc.fit(X train, v train)

#### Unsupervised Learning

>>> k means.fit(X train) >>> pca model = pca.fit transform(X train) Fit to data, then transform it

# **Prediction**

### **Supervised Estimators**

>>> v pred = svc.predict(np.random.random((2,5))) >>> y\_pred = lr.predict(X\_test)

#### >>> y pred = knn.predict proba(X test) **Unsupervised Estimators**

>>> y pred = k means.predict(X test)

#### Predict labels Predict labels

Fit the model to the data

Fit the model to the data

Estimate probability of a label

Predict labels in clustering algos

# **Preprocessing The Data**

#### Standardization

- >>> from sklearn.preprocessing import StandardScaler >>> scaler = StandardScaler().fit(X train)
- >>> standardized X = scaler.transform(X\_train)
  >>> standardized X test = scaler.transform(X test)

#### Normalization

- >>> from sklearn.preprocessing import Normalizer >>> scaler = Normalizer().fit(X train) >>> normalized X = scaler.transform(X train)
- >>> normalized X test = scaler.transform(X test)

#### Binarization

- >>> from sklearn.preprocessing import Binarizer >>> binarizer = Binarizer(threshold=0.0).fit(X)
- >>> binary X = binarizer.transform(X)

# **Encoding Categorical Features**

- >>> from sklearn.preprocessing import LabelEncoder
- >>> enc = LabelEncoder()
- >>> y = enc.fit transform(y)

## Imputing Missing Values

- >>> from sklearn.preprocessing import Imputer >>> imp = Imputer(missing values=0, strategy='mean', axis=0)
- >>> imp.fit transform(X train)

# **Generating Polynomial Features**

- >>> from sklearn.preprocessing import PolynomialFeatures >>> polv = PolvnomialFeatures (5)
- >>> polv.fit transform(X)

### **Evaluate Your Model's Performance**

#### Classification Metrics

#### **Accuracy Score**

- >>> knn.score(X test, v test)
- Estimator score method >>> from sklearn.metrics import accuracy score Metric scoring functions
- >>> accuracy score(y test, y pred)

#### Classification Report

>>> from sklearn.metrics import classification report Precision, recall, fi-score >>> print(classification report(y test, y pred)) and support

# Confusion Matrix

- >>> from sklearn metrics import confusion matrix >>> print(confusion matrix(y test, y pred))
  - Regression Metrics

#### Mean Absolute Frror

- >>> from sklearn.metrics import mean absolute error >>> y true = [3, -0.5, 2]
- >>> mean absolute error(y true, y pred)

#### Mean Squared Error

- >>> from sklearn.metrics import mean squared error
- >>> mean squared error(y test, y pred)

- >>> from sklearn.metrics import r2 score
- >>> r2 score(y true, y pred)

# Clustering Metrics

#### **Adjusted Rand Index**

- >>> from sklearn.metrics import adjusted rand score >>> adjusted rand score(y true, y pred)
- Homogeneity
- >>> from sklearn.metrics import homogeneity score
- >>> homogeneity score(y true, y pred)

- >>> from sklearn.metrics import v measure score >>> metrics.v measure score(y true, y pred)
- **Cross-Validation**
- >>> from sklearn.cross validation import cross val score
- >>> print(cross\_val\_score(knn, X\_train, y\_train, cv=4))
  >>> print(cross\_val\_score(lr, X, y, cv=2))

# **Tune Your Model**

### Grid Search

- >>> from sklearn.grid search import GridSearchCV >>> params = {"n neighbors": np.arange(1,3),
- "metric": ["euclidean", "cityblock"]} >>> grid = GridSearchCV(estimator=knn,
- param grid=params)
- >>> grid.fit(X train, y train) >>> print(grid.best\_score\_)
  >>> print(grid.best\_estimator .n neighbors)

# Randomized Parameter Optimization

- >>> from sklearn.grid search import RandomizedSearchCV
- >>> room skreain.grid search import kandomizedsea
  >>> params = {"n\_neighbors": range(1,5),
- param distributions=params,
- n iter=8. random state=5) >>> rsearch.fit(X train, y train)
- >>> print(rsearch.best score )

#### **DataCamp** Learn Python for Data Science Interactively

![](_page_5_Picture_110.jpeg)

# **Python For Data Science** *Cheat Sheet* **Matplotlib**

Learn Python Interactively at <a href="https://www.DataCamp.com">www.DataCamp.com</a>

![](_page_6_Picture_2.jpeg)

# Matplotlib

Matplotlib is a Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms.

![](_page_6_Picture_5.jpeg)

# Prepare The Data

Also see Lists & NumPv

```
>>> import numpy as np
>>> x = np.linspace(0, 10, 100)
>>> y = np.cos(x)
>>> z = np.sin(x)
```

#### 2D Data or Images

```
>>> data = 2 * np.random.random((10, 10))
>>> data2 = 3 * np.random.random((10, 10))
>>> Y, X = np.mgrid[-3:3:100j, -3:3:100j]
>>> U = -1 - X**2 + Y
>>> V = 1 + X - Y**2
>>> from matplotlib.cbook import get sample data
>>> img = np.load(get sample data('axes grid/bivariate normal.npy'))
```

# Create Plot

```
>>> import matplotlib.pvplot as plt
```

```
>>> fig = plt.figure()
>>> fig2 = plt.figure(figsize=plt.figaspect(2.0))
```

All plotting is done with respect to an Axes. In most cases, a subplot will fit your needs. A subplot is an axes on a grid system.

```
>>> fig.add axes()
>> ax1 = fig.add subplot(221) # row-col-num
>>> ax3 = fig.add subplot(212)
>>> fig3, axes = plt.subplots(nrows=2,ncols=2)
>>> fig4, axes2 = plt.subplots(ncols=3)
```

## Plot Anatomy & Workflow

Plot Anatomy

# Axes/Subplot Y-axis Figure X-avis

#### Workflow

```
The basic steps to creating plots with matplotlib are:
```

```
>>> import matplotlib.pyplot as plt
>>> x = [1,2,3,4]
>>> y = [10, 20, 25, 30]
>>> fig = plt.figure() < Step 2
>>> ax = fig.add subplot(111) < Step 3
>>> ax.plot(x, y, color='lightblue', linewidth=3) Step 3.4
>>> ax.scatter([2,4,6],
                [5, 15, 25],
                color='darkgreen',
                marker='^')
>>> ax.set xlim(1, 6.5)
>>> plt.savefig('foo.png')
>>> plt.show()
```

1 Prepare data 2 Create plot 3 Plot 4 Customize plot 5 Save plot 6 Show plot

# Customize Plot

#### Colors, Color Bars & Color Maps

```
>>> plt.plot(x, x, x, x**2, x, x**3)
>>> ax.plot(x, v, alpha = 0.4)
>>> ax.plot(x, y, c='k')
>>> fig.colorbar(im, orientation='horizontal')
>>> im = ax.imshow(img,
                   cman='seismic')
```

| >>> | fig, ax = plt.subplots()              |
|-----|---------------------------------------|
| >>> | <pre>ax.scatter(x,y,marker=".")</pre> |
| >>> | <pre>ax.plot(x,y,marker="o")</pre>    |

```
>>> plt.plot(x,y,linewidth=4.0)
>>> plt.plot(x,v,ls='solid')
>>> plt.plot(x,y,ls='--')
>>> plt.plot(x,y,'--',x**2,y**2,'-.')
>>> plt.setp(lines,color='r',linewidth=4.0)
```

#### Text & Annotations

```
>>> ax.text(1.
            -2.1,
           'Example Graph',
           style='italic')
>>> ax.annotate("Sine",
                xv = (8, 0),
                xycoords='data'
                xytext = (10.5, 0),
                 textcoords='data'
                arrowprops=dict(arrowstyle="->"
                             connectionstyle="arc3"),)
```

```
>>> plt.title(r'$sigma i=15$', fontsize=20)
```

#### Limits, Legends & Layouts

 $\Rightarrow$  ax.margins(x=0.0,y=0.1)

Limits & Autoscaling

```
>>> ax axis('equal')
                                                           Set the aspect ratio of the plot to 1
                                                           Set limits for x-and y-axis
>>> ax.set(xlim=[0,10.5],ylim=[-1.5,1.5])
                                                           Set limits for x-axis
>>> ax.set xlim(0,10.5)
>>> ax.set(title='An Example Axes',
                                                           Set a title and x-and y-axis labels
             vlabel='Y-Axis',
             xlabel='X-Axis')
>>> ax legend(loc='best')
                                                           No overlapping plot elements
>>> ax.xaxis.set(ticks=range(1,5),
                                                           Manually set x-ticks
                    ticklabels=[3.100,-12."foo"1)
                                                           Make y-ticks longer and go in and out
>>> ax.tick params(axis='v',
                      direction='inout'.
                      length=10)
 Subplot Spacing
                                                           Adjust the spacing between subplots
```

```
>>> fig3.subplots adjust(wspace=0.5,
                         hspace=0.3.
                         left=0.125,
                         right=0.9.
                         t.op=0.9.
                         bottom=0.1)
>>> fig.tight lavout()
Axis Spines
>>> ax1.spines['top'].set visible(False)
```

#### Fit subplot(s) in to the figure area

Add padding to a plot

#### Make the top axis line for a plot invisible >>> ax1.spines['bottom'].set position(('outward', 10)) Move the bottom axis line outward

# **Plotting Routines**

```
>>> fig. ax = plt.subplots()
>>> lines = ax.plot(x,y)
>>> ax.scatter(x,y)
>>> axes[0,0].bar([1,2,3],[3,4,5])
>>> axes[1.0].barh([0.5.1.2.5],[0.1.2])
>>> axes[1,1].axhline(0.45)
>>> axes[0.1] axvline(0.65)
>>> ax.fill(x, y, color='blue')
>>> ax.fill between (x, y, color='yellow')
```

Draw points with lines or markers connecting them Draw unconnected points, scaled or colored Plot vertical rectangles (constant width) Plot horiontal rectangles (constant height)

Draw a horizontal line across axes Draw a vertical line across axes Draw filled polygons

Fill between v-values and o

| >>> ax1.hist(y)       | Plot a histogram            |
|-----------------------|-----------------------------|
| >>> ax3.boxplot(y)    | Make a box and whisker plot |
| >>> ax3.violinplot(z) | Make a violin plot          |

#### 2D Data or Images

>>> fig. ax = plt subplots()

| >>> | im = | ax.imshow(img,          |
|-----|------|-------------------------|
|     |      | cmap='gist earth',      |
|     |      | interpolation='nearest' |
|     |      | vmin=-2,                |
|     |      | vmax=2)                 |

Colormapped or RGB arrays

| >>> | axes2[0].pcolor(data2)    |
|-----|---------------------------|
| >>> | axes2[0].pcolormesh(data) |
| >>> | CS = plt.contour(Y, X, U) |
| >>> | axes2[2].contourf(data1)  |
| >>> | axes2[2] = ax clabel(CS)  |

Pseudocolor plot of 2D array Pseudocolor plot of 2D array Plot contours Plot filled contours Label a contour plot

# Save Plot

Save figures >>> plt.savefig('foo.png') Save transparent figures >>> plt.savefig('foo.png', transparent=True)

# Show Plot

>>> plt.show()

# Close & Clear

| >> plt.cla()   | Clear an axis           |
|----------------|-------------------------|
| >> plt.clf()   | Clear the entire figure |
| >> plt.close() | Close a window          |

#### **DataCamp** Learn Python for Data Science Int

![](_page_6_Picture_62.jpeg)

# Seaborn

Learn Data Science Interactively at <a href="www.DataCamp.com">www.DataCamp.com</a>

![](_page_7_Picture_3.jpeg)

### Statistical Data Visualization With Seaborn

The Python visualization library **Seaborn** is based on matplotlib and provides a high-level interface for drawing attractive statistical graphics.

### Make use of the following aliases to import the libraries:

```
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
```

#### The basic steps to creating plots with Seaborn are:

- 1. Prepare some data
- 2. Control figure aesthetics
- 3. Plot with Seaborn
- 4. Further customize your plot

```
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> tips = sns.load_dataset("tips")
```

# 1 ) Data

Seaborn styles

#### Also see Lists, NumPy & Pandas

```
>>> import pandas as pd
>>> import numpy as np
>>> uniform_data = np.random.rand(10, 12)
>>> data = pd.DataFrame({'x':np.arange(1,101),
```

#### Seahorn also offers built-in data sets:

```
>>> titanic = sns.load_dataset("titanic")
>>> iris = sns.load_dataset("iris")
```

#### **Axis Grids**

```
>>> g = sns.FacetGrid(titanic,
```

Plotting With Seaborn

Subplot grid for plotting conditional relationships

Draw a categorical plot onto a Facetgrid

Plot data and regression model fits across a FacetGrid

```
>>> h = sns.PairGrid(iris)
>>> h = h.map(plt.scatter)
>>> sns.pairplot(iris)
>>> i = sns.JointGrid(x="x",
```

data=iris,

kind='kde'

### **Categorical Plots**

```
Scatterplot
                                                   Scatterplot with one
>>> sns.stripplot(x="species",
                    v="petal length".
                                                   categorical variable
                    data=iris)
                                                   Categorical scatterplot with
>>> sns.swarmplot(x="species",
                    v="petal length".
                                                   non-overlapping points
                    data=iris)
Rar Chart
                                                   Show point estimates and
>>> sns.barplot(x="sex",
                v="survived".
                                                   confidence intervals with
                                                   scatterplot glyphs
                hue="class".
                 data=titanic)
Count Plot
                                                   Show count of observations
>>> sns.countplot(x="deck",
                   data=titanic,
                   palette="Greens d")
Point Plot
>>> sns.pointplot(x="class",
```

Show point estimates and confidence intervals as rectangular bars

Boxplot with wide-form data

Also see Matplotlib

Boxplot

Violin plot

markers=["^","o"], linestyles=["-","--"])

palette={"male":"q",

"female": "m" },

v="survived",

data=titanic.

hue="sex",

>>> sns.boxplot(x="alive",

>>> sns.boxplot(data=iris,orient="h")
Violinplot
>>> sns.wiolinplot(y="age"

>>> sns.violinplot(x="age",

#### Regression Plots

```
>>> sns.regplot(x="sepal_width", y="sepal_length", data=iris, ax=ax)

Plot data and a linear regression model fit
```

#### Distribution Plots

```
>>> plot = sns.distplot(data.y, kde=False, color="b")
```

#### **Matrix Plots**

>>> sns.heatmap(uniform data,vmin=0,vmax=1) | Heatmap

# 4 Further Customizations

#### Also see Matplotlib

### Axisgrid Objects

```
>>> g.despine(left=True)
>>> g.set_ylabels("Survived")
>>> g.set_xticklabels(rotation=45)
>>> g.set_axis_labels("Survived",
```

#### Plot

| >>> plt.title("A Title") >>> plt.ylabel("Survived") >>> plt.xlabel("Sex") >>> plt.ylim(0,100) | Add plot title Adjust the label of the y-axis Adjust the label of the x-axis Adjust the limits of the y-axis |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| >>> plt.xlim(0,10)<br>>>> plt.setp(ax,yticks=[0,5])                                           | Adjust the limits of the x-axis Adjust a plot property                                                       |
| >>> plt.setp(ax,yticks=[0,3])<br>>>> plt.tight_layout()                                       | Adjust subplot params                                                                                        |

# 2) Figure Aesthetics

#### **Context Functions**

Boxplot

| <br>                               |                                                                                                 |
|------------------------------------|-------------------------------------------------------------------------------------------------|
| sns.set_context<br>sns.set_context | Set context to "talk" Set context to "notebook", scale font elements and override param mapping |
|                                    |                                                                                                 |

# >>> sns.set() (Re)set the seaborn default

>>> f, ax = plt.subplots(figsize=(5,6)) Create a figure and one subplot

| >>> | <pre>sns.set_style("whitegrid")</pre>  |
|-----|----------------------------------------|
| >>> | sns.set_style("ticks",                 |
|     | {"xtick.major.size":8,                 |
|     | "ytick.major.size":8})                 |
| >>> | <pre>sns.axes_style("whitegrid")</pre> |

(Re)set the seaborn default Set the matplotlib parameters Set the matplotlib parameters

Return a dict of params or use with with to temporarily set the style

## Color Palette

|     | <pre>sns.set_palette("husl",3) sns.color palette("husl")</pre> | Define the color palette Use with with to temporarily set palette |
|-----|----------------------------------------------------------------|-------------------------------------------------------------------|
| >>> | flatui = ["#9b59b6","#3498db",                                 | "#95a5a6","#e74c3c","#34495e","#2ecc71"]                          |
| >>> | sns.set_palette(flatui)                                        | Set your own color palette                                        |

# (5) Show or Save Plot

# Also see Matplotlib

| >>> | plt.show()             |
|-----|------------------------|
| >>> | plt.savefig("foo.png") |
| >>> | plt.savefig("foo.png", |
|     | transparent=True)      |

Show the plot Save the plot as a figure Save transparent figure

# Close & Clear

## Also see Matplotlib

|--|

# DataCamp Learn Python for Data Science Interactiv

![](_page_7_Picture_61.jpeg)

# **Bokeh**

Learn Bokeh Interactively at www.DataCamp.com, taught by Bryan Van de Ven, core contributor

![](_page_8_Picture_3.jpeg)

# Plotting With Bokeh

The Python interactive visualization library Bokeh enables high-performance visual presentation of large datasets in modern web browsers.

![](_page_8_Picture_6.jpeg)

Bokeh's mid-level general purpose bokeh.plotting interface is centered around two main components: data and alvphs.

![](_page_8_Picture_8.jpeg)

The basic steps to creating plots with the bokeh.plotting interface are:

1. Prepare some data:

Python lists, NumPy arrays, Pandas DataFrames and other sequences of values

- 2. Create a new plot
- 3. Add renderers for your data, with visual customizations
- 4. Specify where to generate the output
- 5. Show or save the results

```
>>> from bokeh.plotting import figure
>>> from bokeh.io import output file, show
>>> x = [1, 2, 3, 4, 5]
>>> v = [6, 7, 2, 4, 5]
>>> p = figure(title="simple line example", Step 2
              x axis label='x',
              y axis label='y')
>>> p.line(x, y, legend="Temp.", line width=2) < Step 3
>>> output file("lines.html") < Step 4
>>> show (p) Step 5
```

# Data

#### Also see Lists. NumPv & Pandas

Under the hood, your data is converted to Column Data Sources. You can also do this manually:

```
>>> import numpy as np
>>> import pandas as pd
>>> df = pd.DataFrame(np.array([[33.9,4,65, 'US'],
                                    [32.4,4,66, 'Asia'],
                       [21.4,4,109, 'Europe']]), columns=['mpg','cyl', 'hp', 'origin'],
                       index=['Toyota', 'Fiat', 'Volvo'])
>>> from bokeh.models import ColumnDataSource
```

# Plottina

>>> cds df = ColumnDataSource(df)

```
>>> from bokeh.plotting import figure
>>> p1 = figure(plot width=300, tools='pan,box zoom')
>>> p2 = figure(plot width=300, plot height=300,
               x range=(0, 8), y range=(0, 8))
>>> p3 = figure()
```

## Glyphs

#### **Scatter Markers** >>> p1.circle(np.array([1,2,3]), np.array([3,2,1]), fill color='white') >>> p2.square(np.array([1.5,3.5,5.5]), [1,4,3], color='blue', size=1) Line Glyphs >>> p1.line([1,2,3,4], [3,4,5,6], line width=2) >>> p2.multi line(pd.DataFrame([[1,2,3],[5,6,7]]), pd.DataFrame([[3,4,5],[3,2,1]]),

### **Customized Glyphs**

### Selection and Non-Selection Glyphs

**Renderers & Visual Customizations** 

![](_page_8_Picture_28.jpeg)

#### Hover Glyphs

>>> from bokeh.models import HoverTool >>> hover = HoverTool(tooltips=None, mode='vline') >>> p3.add tools(hover)

#### Colormapping

```
>>> from bokeh.models import CategoricalColorMapper
>>> color mapper = CategoricalColorMapper(
                   factors=['US', 'Asia', 'Europe'],
                   palette=['blue', 'red', 'green'])
>>> p3.circle('mpg', 'cyl', source=cds df,
             color=dict (field='origin'.
                        transform=color mapper),
             legend='Origin')
```

### Legend Location Inside Plot Area

```
>>> p.legend.location = 'bottom left'
 Outside Plot Area
>>> from bokeh.models import Legend
>>> r1 = p2.asterisk(np.array([1,2,3]), np.array([3,2,1])
>>> r2 = p2.line([1,2,3,4], [3,4,5,6])
>>> legend = Legend(items=[("One",[p1, r1]),("Two",[r2])],
location=(0, -30))
>>> p.add layout(legend, 'right')
```

### Legend Orientation

```
>>> n legend orientation = "horizontal"
>>> p.legend.orientation = "vertical"
```

## Legend Background & Border

```
>>> p.legend.border line color = "navv'
>>> p.legend.background fill color = "white"
```

# Rows & Columns Lavout

```
>>> from bokeh.layouts import row
>>> lavout = row(p1,p2,p3)
>>> from bokeh.layouts import columns
>>> layout = column(p1,p2,p3)
Nesting Rows & Columns
>>>layout = row(column(p1,p2), p3)
```

### Grid Lavout

```
>>> from bokeh.layouts import gridplot
>>> row1 = [p1,p2]
>>> row2 = [p3]
>>> lavout = gridplot([[p1,p2],[p3]])
```

#### **Tabbed Lavout**

```
>>> from bokeh.models.widgets import Panel, Tabs
>>> tab1 = Panel(child=p1, title="tab1")
>>> tab2 = Panel(child=p2, title="tab2")
>>> layout = Tabs(tabs=[tab1, tab2])
```

### Linked Plots

```
Linked Axes
>>> p2.x range = p1.x range
>>> p2.v range = p1.v range
 Linked Brushing
>>> p4 = figure(plot width = 100.
               tools='box_select,lasso_select')
>>> p4.circle('mpg', 'cyl', source=cds df)
>>> p5 = figure(plot width = 200,
               tools='box select, lasso select')
>>> p5.circle('mpg', 'hp', source=cds df)
>>> layout = row(p4,p5)
```

# Output & Export

#### Notebook

```
>>> from bokeh.io import output notebook, show
>>> output notebook()
```

#### HTML

#### Standalone HTML

```
>>> from bokeh.embed import file html
>>> from bokeh.resources import CDN
>>> html = file html(p, CDN, "my plot")
```

```
>>> from bokeh.io import output file, show
>>> output file('my bar chart.html', mode='cdn')
```

```
>>> from bokeh.embed import components
>>> script, div = components(p)
```

#### PNG

```
>>> from bokeh.io import export png
>>> export png(p, filename="plot.png")
```

#### SVG

```
>>> from bokeh.io import export sygs
>>> p.output backend = "svg"
>>> export svgs(p, filename="plot.svg")
```

# Show or Save Your Plots

| ~ | , <u> </u> |                                   |  |  |
|---|------------|-----------------------------------|--|--|
|   |            | >>> show(layout) >>> save(layout) |  |  |

#### **DataCamp** Learn Python for Data Science Intera

![](_page_8_Picture_64.jpeg)