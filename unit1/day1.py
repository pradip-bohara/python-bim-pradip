# -------- Python Unit 1: Introduction --------

#  Single-line comment: Used to describe what's happening in the next line
print("Hello, this is the first Python code")

#  Why comments?
# Comments improve readability, document functionality,
# and aid collaboration among developers.

#  Multi-line comment example using triple quotes
'''
This is a multi-line comment.
It spans across multiple lines.
Useful for longer descriptions.
'''

# Comments in code is essential for improving readability documenting funcionality and aiding collaboration among developers
# use clear concise language
# comment frequently
# follow a consistent style
# use inline comments sparingly
# Document function and classes
# update comments regularly
# use comments to temporarily disable code
# Avoid redundant comments
# Use comments for TODOs and FIXMEs
# --------------------------------------------
# Python Indentation
# Indentation defines the structure and block of code in Python.
# Improper indentation will cause an error.

x = 10
if x < 5:
    print("x is less than 5")
else:
    print("x is greater than or equal to 5")

# --------------------------------------------
# Tokens in Python
# Tokens are the smallest building blocks of a Python program.

# Keywords example:
# 'if', 'else', 'import', 'print', 'def', etc.

# Identifiers:
name = "Prem"       # 'name' is an identifier
age = 22            # 'age' is another identifier

# Literals:
height = 172.5      # float literal
is_student = True   # boolean literal

# Operators:
year_of_birth = 2025 - age   # Subtraction operator used

# --------------------------------------------
#  id() Function
# Shows the memory location (identity) of a variable
print("ID of variable 'age':", id(age))

# --------------------------------------------
# Importing Standard Libraries
import sys

print("Python is running from:", sys.executable)

# --------------------------------------------
# 🔌 Third-Party Libraries and Virtual Environment

# To use third-party libraries like 'requests' or 'numpy',
# you must install them using pip. Example:
# pip install requests

# It's best practice to use a virtual environment:
# 1. Create virtual environment:
#    python -m venv venv
#
# 2. Activate it:
#    On Windows: venv\Scripts\activate
#    On Mac/Linux: source venv/bin/activate
#
# 3. Install libraries inside virtual environment:
#    pip install library_name

# Example (commented because 'requests' may not be installed yet):
# import requests
# response = requests.get("https://example.com")
# print(response.status_code)

# --------------------------------------------
#  Summary of Unit 1 Concepts
# - Python Introduction: Simplicity, readability
# - Comments: Single-line and multi-line
# - Indentation: Defines code blocks
# - Tokens: Keywords, Identifiers, Literals, Operators
# - Variables and Constants
# - id() Function
# - Operators
# - Third-party libraries
# - Virtual environments

