#Dictinary

# dictionaries are used to store data values in key:value pairs. 

# a dictionary is a collection which is ordered*, changeable and do nto allow duplicates. 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(type(thisdict))

# using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# Accessing items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


# get() that will give you the sma eresult:
x = thisdict.get("model")

# get keys 
# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()

info = {
    "key" : "value",
    "name" : "Pradip",
    "learning" : "coding",
    "age" : 20,
    "marks" : 96,
    "subjects" : ["tython", "html", "css", "js", "php"]
}

# Dictionary in python

student = {
    "anme" : "ram",
    "subjects" : {
        "c" : 83,
        "chem" : 92,
        "math" : 95
    }
}

print(student["subjects"]["c"])

#practice question  