# Indentation is a key aspect of Python syntax, defining the strukctue and scope of code blocks unlike manyk other programming language that use braces { }

# Example 
x = 5
if x > 0:
    print("Positive number") # Indented with 4 speaces


# Code Blocks

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


# lopes:


for i in range(5):
    print(i)            # Indented with 4 speaces


# Function Definitions:

def greet():
    print("Function for indentation")


# Nested Blocks

for i in range(4):
    if i % 2 == 0:
        print(f"{i} is evne")
    else:
        print(f"{i} is odd")


