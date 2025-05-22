# Tupples 

# tuples are used to store multiple items in a single variable. 
# a tuple is a collection which is orderd and unchangeable.
# Tuples are written with round breckets. 

thisTuple = ("apple", "banana", "cherry")

print(thisTuple)

# Tuple items are ordered, unchangeable, and allow duplicate values. 

#ORDERED 
# when we say that tuples are ordered, it menas that the items have a defined order, and that order will not chang

#UNCHANGEABLE
# Tuples are unchangealbe, meaning that we cannot change, add or remove items after teh tuple has been created. 

# allow duplicates 

tp = ("apple",)
print(type(tp))

#not a tuple 
tp = ("apple")
print(type(tp))  # output is string. 

# a tuple with strings, integers and boolean values:


#============== The tuple() constructor ==============
thistup = tuple(("apple", "banana", "cherry")) # double round brackets 
print(thistup)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5) # returns the number of times a specified value appears in the tuple.
print(x)