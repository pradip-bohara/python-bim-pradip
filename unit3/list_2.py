# PYthon add list items 
#  Append Items 

# to add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")

print(thislist) # output: add list orange 

#insert itmes 
# to insert alist item at a specified index, use the insert() method.
thislist.insert(2, "orange")

#Extend list 
#To append elements form another list to the current list, use the extend() method. and other set, tupple di etc.

tolist = ["mango", "pineapple", "papaya"]
thislist.extend(tolist)
print(thislist[6])
print(len(thislist))

thislist.extend(["hello", "melo", "chilo"]) # add each character as an item in the list
print(thislist)     # output: ['apple', 'banana', 'orange', 'cherry', 'orange', 'mango', 'pineapple', 'papaya', 'a', 'p', 'p', 'l', 'e']



# ================== Remove list items ====================================

#remove() mehtod removes the specified itme.
thislist.remove("banana")
print(f'The remove lsit itme after {thislist}')
# print(thislist)

#pop() method index besd and simple pop() which last element pop

thislist.pop(2)
print(thislist)
thislist.pop()
# del keyword also removes the specigied index
del thislist[0] # remove index o item form list thislist
print(thislist)


 
# del use to delete the list completly by using del keyword  or list index number 
person = ["pradip", "Hari", "Sita", "Gita", "Ram"]
print(person)
del person[2]
print(person)  # remove index 2 item Sita

#clear() method empties the list
person.clear()
print(person) # output: []


# ================== Loop Through a List ================================
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop through the index numbers
for i in range(len(thislist)):
    print(f" index: {i} : {thislist[i]}")

#using desctructing to loop through the list
thislist = ["apple", "banana", "cherry"]
for i, x in enumerate(thislist):
    print(f" index: {i} : {x}")

# ================== List Comprehension ================================
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
#  Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:

newlist = [x for x in fruits if "a" in x]
print(newlist)


