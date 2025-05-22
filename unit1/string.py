# String in python are surreounded by either single quotation marks or double quotation marks.

print("hello python")       # double quotation
print('hello python')       #single quotation

# Quotes inside quotes

print("It's alright")
print("He is called 'Rama' ")

# Assign String to a variable use = operater

a = "Python"
print(a)

# Multiline string double and single 3 quotes

str ="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
 
#string length
print(len(str))


# check string in given string

text = 'the best things in life are free!'

print("free" in text)

if "free" in text:
    print("Yes, 'free' is present. ")

# Check if NOT
print("expensive" not in text)