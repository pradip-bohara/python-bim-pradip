# sets

myset = {"apple", "banana", "cherry"}

# A set is a collection which is unordered unchangeable* and unindexed. 
set1 = {"abc", 34, True, 40, "male"}

print(type(set1))

# the set() constructor 

# accesss items usng for loop

for x in set1:
    print(x)


# Once a set is created, you cannot chage its itmes, but you can  add new items.

# using add() mehtod 
# update(tropical)

#discard()
# pop()
# clear()

s = {1, 2, 5}
print(s)
print(type(s))

# A set automatically remove all the duplicate values.
# does not suport indexing in set


# ====================== set =============

# using the add() method we can add a singel element to the set 

s.add(5)

print(s)

# update() multiple ones:
s.update([4, 4, 6, 7, 9])
print(s)

# Both method will remove an element form the set but remove() will raise a key error if the value doesnt' exist.

s. remove(4)
print(s)

# discard() won't raise any errors.

s.discard(4) # it does not raise errors.
print(s)  

# set union 
# union() or | will create a new set with all the elements form the sets provided. 

s1 = {1, 3, 5}
s2 = {5,7,3,9}
print(s1.union(s2)) # s1 | s2

print(s1)

# set intersection 
# intersection() or & will return a set with the elements that are common to all of them.

print(s1 & s2) # s1.intersection(s2)

# set difference 
# symmetric_difference() or ^ will return all the elements that are not common between.

print(s1.symmetric_difference(s2))