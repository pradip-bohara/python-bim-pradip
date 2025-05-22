#Exception handling
""" Exception handling is a mechanism to handle runtime errors. 
It is mainly used to handle the exceptions that can occur in the code during the execution of the program. """
# Types of exceptions
# There are two types of exceptions in Python:
# 1. Built-in exceptions: These exceptions are defined in 
# the Python language and are raised when a specific error occurs.
# 2. User-defined exceptions: These exceptions are defined 
# by the user and are raised when a specific error occurs in the code.

# Example 1
# Built-in exceptions
# ZeroDivisionError: Raised when division or modulo by zero occurs.
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
# Output: Error: division by zero

# Example 2
# Built-in exceptions
# FileNotFoundError: Raised when a file is not found.
try:
    file = open("file.txt", "r")
except FileNotFoundError as e:
    print("Error:", e)
# Output: Error: [Errno 2] No such file or directory: 'file.txt



# Example 3
# User-defined exceptions
# Custom exception class

class MyError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyError("This is a custom error")
except MyError as e:
    print("Error:", e.message)
# Output: Error: This is a custom error
# In this example, we have defined a custom exception class MyError that inherits from the base Exception class.





# ================================== Modules and packages in python =================== 

# Modules and packages  in Python
""" A module is a file that contains Python code. It can define 
functions, classes, and variables that can be used in other Python 
files. A package is a collection of modules that are organized in a directory structure. """

'''
package is a collection of modules that are organized in a directory structure.
'''
# Example 1
# Creating a module
# Create a file named mymodule.py and add the following code:


# ====================== Enumeration in Python  ========================

# Enumerations are a set of symbolic names bound to unique constant values. 
# In Python, enumerations are created using the Enum class from the enum module.
# Example 1

# Creating an enumeration

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE =  3
# Accessing enumeration members
print(Color.RED) # Output: Color.RED
print(Color.RED.value) # Output: 1
# # In this example, we have created an enumeration Color with three members: RED, GREEN, and BLUE. 
# Each member is bound to a unique constant value. We can access the members of 
# the enumeration using the dot notation (Color.RED) and get the value of the 
# members using the value attribute (Color.RED.value).