#Array Broadcasting 
"""Brodcasting allows Numpy to perform element-wise operations on arrays of different
shapes. Smaller arrasy are "broadcast" across larger arrays."""
import numpy as np
# Example Element-wise addition
arra1 = np.array([1, 2, 3])
arra2 = np.array([10, 20, 30])

#element-wise addition
result = arra1 + arra2  #output: [11, 22, 33]
print(result)



#Iterating Over Arrays 
# np.nditer() can be used to iterate over arrays efficiently 4
arr = np.array([[1, 2], [3, 4]])

for x in np.nditer(arr):
    print(x)  # Output: 1 2 3 4

"""
Sorting and Searching
Sorting: You can sort an array using np.sort() or np.argsort() to return the indices that would sort the array.
Searching: You can use np.searchsorted() to find where a value should be inserted into a sorted array."""


arr = np.array([30, 10, 20, 40])

sorted_arr = np.sort(arr)  # Output: [10 20 30 40]
indices = np.argsort(arr)  # Output: [1 2 0 3]

# Searching
index = np.searchsorted(sorted_arr, 25)  # Output: 2 (position to insert)


# Statistical Functions
"numpy provides a wide range of statistical functions like mean, median variance, standard deviation etc"

arr = np.array([1, 2, 3, 4, 5])

print("mean =", np.mean(arr))  # Output: 3.0
print("median =", np.median(arr))  # Output: 3.0
print("variance =", np.var(arr))  # Output: 2.0
print("std_dev =", np.std(arr))  # Output: 1.4142135623730951



#Searching Arrays

# you can search and array for a certain vlue and return the indexes that get a match. use the where() method.
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
# The example above will return a tuple: (array([3, 5, 6],)

# Which means that the value 4 is present at index 3, 5, and 6.


# Search Sorted
# There is a method called searchsorted() which performs a binary 
# search in the array, and returns the index where the specified 
# value would be inserted to maintain the search order.

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

# Sorting Arrays 
# The NumPy ndarray object has a function called sort(), that will sort a specified array.
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

 

 #Creating the Filter Array
 
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)