# Input in Python 
# input() statement is used to accept values (using keyboard) form user 

name = input("Enter your name:")
print("Welcome", name)

# input() is always a str
# for example 
valu = input("enter value: ")

print(type(valu), valu)  # this is always string 

#use type casting for correct input

val = int(input("Enter value: "))
print(type(val), val)


# your information inter

name = input("Enter name: ")
age = int(input("Enter your age:"))
marks = int(input("Enter your marks"))

print("The name is :", name,"Age is: ", age, "marks is:",marks)