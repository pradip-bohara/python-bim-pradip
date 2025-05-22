#Multable sequences of items.
# List are used to store multiple items in a single variable. 
# Built-in data types in python used to store collections of data, the other are Tuple, set, and Dictionary, all with different qualities and usage. 

# create list using square brackets [] 

this_list = [ "apple", "banana", "cherry"]
print(this_list)

# list length 
print(len(this_list))

list1 = ["abc", 34, True, 40, 'Male'] # contain different data types
print(type(list1))

# The list() constructor creating a new list.append() method to add an item to the end of the list.
this_list = list(("apple", "bannana", "cherry"))
print(this_list)

# ======================= Access Items ========================

# Access items index number 
print(this_list[1])
print(this_list[-1]) #Negative indexing menas start form the end -1 -2 second last item etc...
print(this_list[-2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # range of index 2 to 5 


# check if item Exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list ")

#change the second item: laso change range of itmes vlaues [1:3]etch splict
thislist[1] = "blackcurrant"

print(thislist)

#Insert() itms

thislist.insert(2, "watermelon")
print(thislist)

furniture = ['table', 'chair', 'rack', 'shelf']

print(f'The {furniture[-1]} is bigger than the {furniture[-3]}')


# zip() function to combine two lists into a llt of tuples

furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]
for item, amount in zip(furniture, price):
    print(f'The {item} costs ${amount}')
# The table costs $100
# The chair costs $50
# The rack costs $80
# The shelf costs $40

# The in and not in opearators
if 'rack' in furniture:
    print('Yes, rack is in the list')
else:
    print('No, rack is not in the list')

if 'bed' not in furniture:
    print('yes, bed in not in the list')
else:
    print('No, bed is in the list')


