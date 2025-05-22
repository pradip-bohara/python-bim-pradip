# In python  Data Types is an importent concept.
# Variables can store data of different type

'''
    Text type:              str
    Numeric Types:          int, float, complex
    Sequence Types:         list, tuple, range
    Mapping types:          dict
    Set Types:              set, frozenset
    Boolean types:          bool
    Binary Types:           bytes, bytearray, memoryview
    None types:             NoneType

''' 

# Getting the data type 

p = 5
print(type(p))

pa = 20.45 # this is a float data type
print(type(pa))

ab = 1j  #complex data type
print(type(ab))
 
name = ["apple", "banna", "cherry"]

print(type(name), name)   #list data type

x = range(6)    # range data type
print(type(x), x)


#dict data type
info = {"name": "pradip", "age" : "20"}

print(type(info), info)


# Specific data type  if you want to specify the data type

names = str("Maya maya")
a = float(20.203)
abc = list(("apple", "banna", "cherry"))

#etc...........

# Python Numbers int float and complex
c,b,d = 1, 2.3, 1j

print(c, b, d)



#=================================== ===== type Conversion ======
# type conversion
e = 5
ed = 4.24

sum = e + ed # type conversion this is add python 5.0 + 4.24 = 9.24


# type casting 
''''
y = "2"
u = 4.2

print(y + u) #typeError can only concatenate str not 

'''

y =int("2")
u = 4.23
print(y + u)