# sort lists 
# lsit objects have a sort() method that will sort the list 

# method that will sort the lsit alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()   # .sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort() #.sort(reverse = True)
print(thislist)

# reverse() method reverse the current sorting order of the elements.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# Customize sort function  
# you can also customize your own function by using the kewyword argument key = function.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# luckily we can use built-in function as key functions when sorting a lsit.
# so if you want a case-insensitive sort function use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)
