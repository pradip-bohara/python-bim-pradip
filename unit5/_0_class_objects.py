# Defining a class

class Animal:
    # Constructor
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method
    def speak(self):
        return f"{self.name} makes a sound."

    # Method to display details
    def details(self):
        return f"Name: {self.name}, Species: {self.species}"

# Creating an object of the class
dog = Animal("Dog", "Canine")
print(dog.speak())
print(dog.details())

""" Class is a bluprint or template for creating objects.it define the 
sturcture and behavior of objects. Objects are instances of class.

Object is an instance of a class. It is a real entity that has a state and behavior.
An object is created using the class constructor.


+9

"""
# Example 2
class car:

    # Constructor to initialize attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display details
    def display_info(self):
        return (f"car brand: {self.brand}, model: {self.model}, year: {self.year}")

# Creating an object of the class
my_car = car("Toyota", "Corolla", 2019)

# Accessing the attributes
print(my_car.brand) #output: Toyota

# call the object's method
print(my_car.display_info()) #output: car brand: Toyota, model: Corolla, year: 2019

# Example 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Creating an object of the class
person1 = Person("Aman", 35)

# Accessing the attributes
print(person1.name) #output: Aman

# call the object's method
print(person1.display_info()) #output: Name: Aman, Age: 35

# self
""" self is a reference to the current instance of the class. It is used to access the attributes and methods of the class within the class definition.
When we create an object of a class, the object is passed as the first argument to the methods of the class. This object is referred to as self.
"""
# Attributes and Methods in OOP Python
# attributes and methods are define the properties and behavior of the objects.
"""- Attributes
        -attributes are the properties of the object.
        -Attributes are defined inside the class using the self keyword.
        -Attributes are accessed using the object of the class.
        -Attributes can be public, protected, or private.
        -Public attributes can be accessed directly using the object.
        -they store data or inrormation about the object.
        -instance Attributes: Specific to each object and are defined inside the constructor using self.
        class Attributes: Shared by all objects of the class and are defined outside the constructor or any methods.

"""
"""
Methods
     - Methods are functions defined inside a class that describe the behavior or actions of the object.
     - Methods are defined using the def keyword followed by the method name and parameters.
     - The first parameter of a method is always self, which refers to the current instance of the class.
     - Methods can access the attributes of the object using self.
     - Methods can be called using the object of the class.
     - the can manipulate the attributes or perform specific tasks.
     - Methods can return values or perform some action.
     -Instance methods: Operate on instance attributes and use self parameter.
     -Class methods: Operate on class level data and use @classmethod decorator.and cls parameter.
     -Static methods: Do not operate on instance or class data and use @staticmethod decorator.
     """

# example: class attributes and mehtods
# Path: unit5/class_objects.py
"""
    A class method takes cls as its first parameter and can access and
      modify the class state. it is clled on the class itself, not
     an instance of the class. like pi given example
    A static method does not take sef or cls as a parameter and does
    not operate on instance or class data. it is used when a method
    logically belongs to the class but does not need to access or modify
    the instance or class state.
     """


class Circle:
    # Class attribute
    pi = 3.14

    # Constructor for instance attributes
    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    # Instance method to calculate area
    def calculate_area(self): # first parameter is self
        return Circle.pi * self.radius * self.radius

    # Class method to get the value of pi
    @classmethod
    def get_pi(cls): # first parameter is cls
        return cls.pi

    # Static method to display a message
    @staticmethod
    def display_message():
        return "This is a circle class"
# Create an object
circle = Circle(5)

#accesing the attributes
print(circle.radius) #output: 5

# Call the instance method
print(circle.calculate_area()) #output: 78.5

# Call the class method
print(circle.get_pi()) #output: 3.14

# Call the static method
print(circle.display_message()) #output: This is a circle class

#isinstance()
#Usage isinstance() is a built-in function, not a keyword, used in OOP for type checking.
#it checks if an object is an instance of a particular class or subclass.
print(isinstance(circle, Circle)) # True
