# A dictionary is an ordered collection of 'key':'value' pairs.

#The main operatins on a dictionary are storing a value with some key and 
# extracting the value given the key. it is also possible to delete a key:value pair with 'del'

#Example Dictionary:

my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

# set key, value using subscript operator []

my_cat['age_years'] = 2

print(my_cat)

# get value using []
print(my_cat['size'])
# print(my_cat['eye_color']) # Key error : eye_color

# values() method gets the vlaues of the dictionary:

for value in my_cat.values():
    print(value)

#keys() The 'keys()' method gets the keys of hte dictionary:

for key in my_cat.keys():
    print(key)

# there is no need to use .keys() since by default you will loop through keys:

# items() method gets the items of a dictionary and returns them as Tuple 

for item in my_cat.items():
    print(item)

for key, value in my_cat.items():
    print(f'key: {key} value: {value}')


# The get() method returns the vlaue of an itme with given key. if the key doesn't exist, it returns 'None': 

wife ={ 'name': 'Rose', 'age': 34}

print(f'My Wife name is {wife.get('name')} \nShe is {wife.get('age')} years old.\nShe is deeply in love with {wife.get('husband')}')

# None value to one of your choice change .get('hunaband', 'lover')

# removing items using pop() removes and returns an item based on agiven key.

print(wife.pop("age"))

#popitem() removes the last item in a dictionary and returns it.

wife.popitem()

# del method reomves an item based on agiven key.capitalize

# clear() remove all the items in a dictionary. 
person = {'name': 'Rose', 'age': 33}
# checking keys in a dictionary  values()
'name' in person.keys()


# pprint.pprint(my_cat)

# meroge {**name, **name}

