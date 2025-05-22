# Python sets
""" A 'set' is an unordered collectin with no duplicate elements.
Basic usese include membership testing and eliminaging duplicte entiers.
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference
"""
#initializing a set
set1 = set([1, 3, 5, 7, 9 , 0]) 

folwere = {"rose", "lily", "tulip", "daffodil"}

print(type(set1))
print(type(folwere))

# when creating set, be sure to not use empty curly braces '{}' or you will get an empty dictionary instead.

set3 ={}
print(type(set3))

print(set1)
print(folwere)

#set object does not support indexing.

#set add and update multiple onese .update([2, 5, 6, 8])

# set remove and discard 
set1.remove(7)
print(set1) # will raise a 'key error' if the value doesn't exist.

set1.discard(7) # won't raise any errors.
print(set1)

# set union set1 | set2 or s1.union(set2)

#set intersection & symbol or set1.intersection()

# set difference - s.difference() 

# will return all the elements that are not common between them.  s1 ^ s2 s1.symmetric_difference(s2) 