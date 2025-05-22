# Lists loop
# loop through a list you can loop through the list items by usng a for loop:

# Example 
thislsit =  ["apple", "banana", "cherry"]

for i in thislsit:
    print(i, end=", ")


# loop through the index numbers 
# use the range() and len() functin to create a suitable iterable. 

for i in range(len(thislsit)):
    print(thislsit[i])


# Using a while loop 

i = 0
while i< len(thislsit):  # len() return list length 1-n
    print(thislsit[i])
    i +=1

# Looping using list comprehension 

[print(x) for x in thislsit]

# List comprehension  
#list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


# Example 
# Based on a list of fruits, you wnat a new list, containing only the fruits with the letter "a" in the name. 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
    if "a" in i:
        newlist.append(i)

print(newlist)


newlist = [ x for x in fruits if "a" in x] # short 

# Syntex 
# newlist = [expression for item in iterable if condition == true]


newlist = [ x for x in fruits if x != "apple"]

print(newlist)


newlist =[x for x in range(10)]
print(newlist)

# accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]  # set all values in the new list to Hello:
print(newlist)

# ============================== Copy lists ============ 

# copy a list 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list()
mylist = list(thislist)
print(mylist)

# use slice operator 
mylist = thislist[:]
print(mylist)


# ===========================  Join lists ========== 
# join  one of the easiest ways are by using the + operator:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#  using appending all the items for on by one; 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)

# using extend() mehtod, wher 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

""" 
    Python has a set of built-in methods that you can use on lists.

Method	                Description
append()	            Adds an element at the end of the list
clear()             	Removes all the elements from the list
copy()	                Returns a copy of the list
count()	                Returns the number of elements with the specified value
extend()	            Add the elements of a list (or any iterable), to the end of the current list
index()	                Returns the index of the first element with the specified value
insert()	            Adds an element at the specified position
pop()	                Removes the element at the specified position
remove()	            Removes the item with the specified value
reverse()	            Reverses the order of the list
sort()	                Sorts the list
"""