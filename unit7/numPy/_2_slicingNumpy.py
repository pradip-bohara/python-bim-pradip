#Indexing and Slicing in NumPY Arrays

#indexing : allows you to access specific elements of an array.
#Slicing :  is used to access a subset of elements form an array.

import numpy as np

arra = np.array([10, 20, 30, 40, 50, 60])

#indexing access
print(arra[2]) # access element at index 2 Output: 30

#slicing 
print(arra[1:4])
print(arra[:])
print(arra[:3])
print(arra[4:])
print(arra[::-2])

# Array Copy and view 
# view Returns a new array object that views the original data without copying it. 
# Copy: Creates a new array with a copy of the original data 

aara1 = np.array([1, 2, 3, 4, 5, 6, 6, 8])

view_arr = aara1[1:8]

copy_arr = aara1[2:5].copy() # this createa ture copy.

print(aara1)
print(view_arr)
print(copy_arr)

# Creating Arrays form Numerical Range 
# np.arange(start, stop, step) Generates arrays form a range of numbers 
# np. linspace(start, stop, num) Generates a specified number of evenly spaced numbers 

arr1 = np.arange(0, 10, 2)  # Output: [0 2 4 6 8]
arr2 = np.linspace(0, 10, 5)  # Output: [0.  2.5  5.  7.5 10.]


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

""""
  The Difference Between Copy and View
The main difference between a copy and a view of an array is that the 
copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not 
affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will 
affect the original array, and any changes made to the original array will affect the view."""

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# Joining NumPy Arrays

"""In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() 
function, along with the axis. If axis is not explicitly passed, it is taken as 0."""

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)