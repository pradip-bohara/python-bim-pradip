"""
    Functions are reusable blocks of code designed to perform a single, specific
    Task. it provide 
    enabling code reusability
    Readability
    Modularity. By using funciton, 
    avoid redundant code and maintain a clean structure in their
    programs. 

    Befefits fo using functions
    Code Resuability, Modularity, improved readability, ease of maintenance, 
    Avoiding redundancy, Facilitates testing and debugging etc

"""
# Creating and calling functions
# Use teh def keyword 
def greet():
    print("This is funciton create")

greet() # calling function

#passing arguments
# Positional arguments:
def greets(name):
    print(f"hello, {name}!")
greets("Funciton")

# keyword arguments:
# send arguments with the key = value syntax.
def ga(n, m = "h"):
    print(f"{n}, {m}")
ga(n="hero", m="ess")

#default Arguments:
# def greet(n = "gesut"):
#     print(f"welcome, {n}")
# greet()

# Arbitrary arguments, *args  do not knwo how many arguments that will be 
# passed into your function 
# this way the function will receive a tuple of arguments, 
def my_funciton(*kids):
    print("The youngest child is "+ kids[2])

my_funciton("Emil", "Rabou", "linus") 

def display(*args):
    for item in args:
        print(item)
display(1, 2, 3, 4)


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=25)


#Unpacking: 
def add(a, b):
    return a + b
numbers = (5, 3)
print(add(*numbers))



# Recursive function 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Outputs: 120

#================== Lambda Functions  =================
#anonymous, single expression function.

# lambda arguments : expression 

square = lambda x: x*x
print(square(5)) 

