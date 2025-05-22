#Introduction to numpy
""" - NumPy is a fowerful library for numerical computaions in Python.
    It provides support for large multi-dimensional arrays matrices, along with a collection of mathematical
    functions to operateon these arrays.
    
 -   NumPy (Numerical Python) is a Python library used for working with arrays. It is faster than Python lists and provides functions for mathematical, statistical, and logical operations
 
 
 It also has functions for working in domain of linear algebra, fourier transform, and matrices.
 
 
    Why is NumPy Faster Than Lists?
    NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

    This behavior is called locality of reference in computer science.

    This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures."""

# NumPy, need to install if hanen't already install

"""
pip install numpy
pip show numpy     
import numpy as np

"""
# import it in your python script: 
import numpy as np

#print numPy version
print(np.__version__) 

# o create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
arras = np.array((1, 2, 3, 4, 5))

print(arras)

#creating array 
'''NumPy provides the np.array() function to create arrays:'''
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(array)
print(type(array))

#Creating a 2d array
array2d = np.array([[1,2,3],[4,5,6]])
print(array2d)
print(type(array2d))

#creagin 3d array 
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3d)


#Define the number od dimensions by using the ndmin arrgument.
arr4d = np.array([1, 2, 3, 4], ndmin=5)

print(arr4d)
print('number of dimensions :', arr4d.ndim)
#Dimensions
"""numPy arrays cna have multiple dimesions. 
You cna check the number of dimensions of an array using the 'ndim' attribute:
        NumPy arrays can have different dimensions:

            0D (Scalar): np.array(42)
            1D (Vector): np.array([1, 2, 3])
            2D (Matrix): np.array([[1, 2], [3, 4]])
            3D and more: np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
"""
# To check the number of dimensions:
print(array.ndim)
print(array2d.ndim)

#Data Types 
'''Numpy arrays cna hold elements of a single data type.
    You can specify the data type when creating an array the data using the "dtype" attribute: 
    
NumPy arrays have specific data types:

int, float, complex, bool, str

        i - integer
        b - boolean
        u - unsigned integer
        f - float
        c - complex float
        m - timedelta
        M - datetime
        O - object
        S - string
        U - unicode string
        V - fixed chunk of memory for other type ( void )
'''

#Specifying data type
arra_float = np.array([1.1, 2.3, 4.0], dtype=float)
print(arra_float)
#check data type
print(arra_float.dtype)


# array Attributes
"""Numpy arrays have various attributes such as 'sape', 'size', and 'itemsize'. 

shape:  Returns the dimensions of the array
size:   Returns the total number of elements
dtype:  Returns the data type
"""

print(array.shape)   # Output: (10,)
print(array2d.size)    # Output: 6
print(array2d.itemsize)  # Output: size of each element in byte 8