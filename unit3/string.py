# String is sequences of unicode characters.
# Strings in python are surrounded by either single quotation marks, or double quotation marks 
'''
    'hello' is the smae as "hello" 
'''
# String are Arrays representing unicode characters. 
a = "Hello, world!"
print(a[1]) # outut is e index characters.

# looping through a string 

for i in  "Pradip":
    print(i, end=" ") #output = P r a d i p 


# string length 
print(len(a)) # find length of string

# check String 
print("free" in "free the best") #Ouptpu in boolen vlaue ( if "free" in txt)


# Check if NOT 
text = " Hello me pradip bohara"
print("pradip" not in text)   # if not in

#======================= PYTHON SLICING STRINGS ========================

#Slicing
ab = "IMS Pradip Bohara"
print(ab[2:5])
print(ab[2:])

# Negative indexing 

name = "pradip Boahra"
print(name[-5:-2])

# ======================= PYTHON STRING METHODS ========================

#Upper Case
n = 'pradip'
print(n.upper())
#  Lower Case
print(n.lower())

#Remove Whitespace 
nc = ' Hello this is ' # space before and / or after the actual text,
print(nc.strip())

#Replace String
x = "hello, World!"
print(x.replace("h", "P"))

# Split String method returns a list wher the text between the specified separatero
list = "Hello, World, Nmme"
print(list.split(","))

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
l = "Hello"
j = "world"

m = l + " " + j
print(m)




# ======================= String Format ========================

# % format 
# The % operator is used to format a string inserting the value in the placeholder.
# %s - String
# %d - Integer
# %f - Float
# %o - Octal
# %x - Hexadecimal
# %e - exponential
#  Example

name = "pradip"

print("my name is %s" % name)

# Format method
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are.

name = "pradip"

print("my name is {}".format(name))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

name = "pradip"

print("my name is {0}".format(name))


# You can use named indexes {name} to be sure the arguments are placed in the correct placeholders:

name = "pradip"

print("my name is {name}".format(name=name))

# You can also use double curly brackets {{ and }} to print the curly brackets:

name = "pradip"

print("my name is {{}}".format(name))

# String format() method takes unlimited number of arguments, and are placed into the respective placeholders:

# f-string format 
# Python 3.6 introduced f-strings. They are prefixed with 'f' and are useful for formatting strings.

name = "pradip"

print(f"my name is {name}")

# ======================= Escape Characters ========================
age = 36
# ta = "my name is ram, I am " + age
# print(ta)

# F- String 

# F-String was introduced in python 3.6 and is now the preferred way of formatting strings.
# simpley put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations. 

var = f"my name is pradip , I'm {age}"
print(var)


# Placeholders and modifiers include f" the place { in } dollars" 
# f"The price is{price:.2f} dollers"  menas fixed point number with 2 decimals
# perform a math operation  in the placeholder, and return the result

doc = r"""
Escape Characters
    Code                                Result 

    \'                                 Single quote
    \\                                 Backslash
    \n                                 New line
    \r                                 Carriage return
    \t                                 Tab
    \b                                 Backspace
    \f                                 Form feed
    \ooo                               Octal value
    \xhh                               Hex value
"""
print("hello this is \n \110\123\234 ")


texts = "Hello world"
print(texts[:])
print(texts[::])
print(texts[:6])
print(texts[::-1])