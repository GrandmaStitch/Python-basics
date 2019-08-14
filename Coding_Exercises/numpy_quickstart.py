"""
NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes.
NumPy’s array class is called ndarray. It is also known by the alias array. Note that numpy.array is not the same as the Standard Python Library class array.array, which only handles one-dimensional arrays and offers less functionality.
"""
import numpy

# we have 3 arrays
# x has 1 axis and that axis has 3 elements in it
x = numpy.array([1, 2, 1] )
# y has 2 axes. the first axis has a length of 2, the second axis has a length of 3.
y = numpy.array([[ 1., 0., 0.],[0., 1., 2.]])
# z has 2 axes. the first axis has a length of 3, the second axis has a length of 4.
z = numpy.arange(12).reshape(3,4)


# important properties

# 1. ndarray.ndim
# returns the number of axes (dimensions) of the array.
print(x.ndim, y.ndim, z.ndim)

# 2. ndarray.shape
# returns the dimensions of the array. for a matrix with n rows and m columns, shape will be (n,m).
print(x.shape, y.shape, z.shape)

# 3. ndarray.size
# returns the total number of elements of the array
print(x.size, y.size, z.size)

# 4. ndarray.dtype
# an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.
# in the example, the elements' type is int64, it means the range of storage capacity is -(2**64/2) to (2**64/2)
print(x.dtype, y.dtype, z.dtype)

# 5. ndarray.itemsize
# the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.
print(x.itemsize, y.itemsize, z.itemsize)

# 6. ndarray.data
# the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.
print(x.data, y.data, z.data)





