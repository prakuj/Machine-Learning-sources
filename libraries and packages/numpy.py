# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
#	a powerful N-dimensional array object
#	efficient multi-dimensional container of generic data. 
#	tools for integrating C/C++ and Fortran code
#	useful linear algebra, Fourier transform, and random number capabilities

#package name
import numpy as np

# attributes 
# a is array object
a.ndim 	  #dimensions
a.shape   # n*m
a.size    # the total number of elements of the array
a.dtype
	# an object describing the type of the elements in the array. 
	# One can create or specify dtype’s using standard Python types. 
	# Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.
a.itemsize
	# the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). 
	# **It is equivalent to ndarray.dtype.itemsize.
a.data
	# the buffer containing the actual elements of the array.

#creating Array:

a = np.array([2,3,4])    # created by passing a sequence
a = np.array(1,2,3,4)    # WRONG
a = np.array([1,2,3,4])  # RIGHT

# array transforms sequences of sequences into two-dimensional arrays
b = np.array([(1.5,2,3), (4,5,6)])

#dtype:
 c = np.array( [ [1,2], [3,4] ], dtype=complex )

np.zeros( (3,4) )   # creates an array full of zeros, 
np.ones(3,4) 		# creates an array full of ones, 
np.empty()   		# creates an array whose initial content is random and depends on the state of the memory. 
# By default, the dtype of the created array is float64.

np.arange( 10, 30, 5 )
# output : array([10, 15, 20, 25])

b = np.arange(12).reshape(4,3)           # 2d array

# let a and b are arrays, then 
a-b 						# elementwise subtraction
b**2  						# each element squared
10*np.sin(a)				# elementwise operation
a<35						# elementwise comparison
A * B                       # elementwise product
A @ B                       # matrix product
A.dot(B)                    # another matrix product

# += and *=, act in place to modify an existing array rather than create a new one.

# let a is an array object
a.sum()						# sum of all array elements
a.min()
a.max()

# let b is 2-D array
b.sum(axis=0)                           # sum of each column
b.min(axis=1)                           # min of each row
b.cumsum(axis=1)                        # cumulative sum along each row

# Indexing, Slicing and Iterating
# a is 1-D, b is 2-D
a = np.arange(10)**3					# 0,   1,   8,  27,  64, 125, 216, 343, 512, 729
a[2]									# accessing via index
a[2:5]									# slicing - index 5 excluded
a[:6:2] = -1000    						# equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000

b[2,3]									# row = 2, col = 3
b[0:5, 1]                       		# each row in the second column of b
b[ : ,1]                        		# equivalent to the previous example
b[1:3, : ]                      		# each column in the second and third row of b
b[-1]                                  	# the last row. Equivalent to b[-1,:]
										# When fewer indices are provided than the number of axes, the missing indices are considered complete slices
# iterating array
# 1- D
for x in a:								# iterating each element
	print(x)
# 2- D
for row in b:							# iterating each row
	print(row)
for element in b.flat: 					# iterate each element
	print(element)

# changing shape of array
# Note that the following three commands all return a modified array, but do not change the original array:
b.ravel()  								# returns the array, flattened
a.reshape(6,2)  						# returns the array with a modified shape
a.T  									# returns the array, transposed
 
a.resize((2,6)) 					    # this modifies the array itself


# Stacking together different arrays
np.vstack((a,b))
np.hstack((a,b))
np.column_stack((a,b))     				# returns a 2D array
										# column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to hstack only for 2D arrays.
										
np.hsplit(a,3)   						# Split a into 3
np.hsplit(a,(3,4))   					# Split a after the third and the fourth column

#array copy
# Python passes mutable objects as references to a function, so function calls make no copy. 
>>> a = np.arange(12)
>>> b = a            # no new object is created
>>> b is a           # a and b are two names for the same ndarray object
True

# The view method creates a new array object that looks at the same data.
>>> c = a.view()
>>> c is a
False
>>> c.base is a                        # c is a view of the data owned by a
True

# The copy method makes a complete copy of the array and its data.
>>> d = a.copy()                          # a new array object with new data is created
>>> d is a
False
>>> d.base is a                           # d doesn't share anything with a
False

####################################################
# overview
####################################################
# Array Creation
	arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like
# Conversions
	ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat
# Manipulations
	array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
# Questions
	all, any, nonzero, where
# Ordering
	argmax, argmin, argsort, max, min, ptp, searchsorted, sort
# Operations
	choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum
# Basic Statistics
	cov, mean, std, var
# Basic Linear Algebra
	cross, dot, outer, linalg.svd, vdot