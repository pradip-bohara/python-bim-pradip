#polymorphism is the ability to use a common interface for multiple forms (data types).

# methods overriding is a type of polymorphism in which a child class provides a specific implementation of a method that is already provided by its parent class.
# it is claled runtime polymorphism. It is also known as method overriding. In method overriding, a subclass provides a specific implementation of a method that is already provided by its parent class.
# Example 1
# Method overriding also called runtime polymorphism
class Animal:
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def speak(self):
        return "Dog barks"
    
class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()
print(dog.speak()) # Output: Dog barks
print(cat.speak()) # Output: Cat me


# Mehod overloading is a type of polymorphism in which a single method has multiple definitions. also called compile-time polymorphism.
# Python does not support method overloading like other programming languages such as Java and C++. 
# However, you can achieve method overloading by using default arguments.
# Example 2
# Method overloading

#The Shape class is defined with an abstract area method, which is intended to be overridden by subclasses.
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    # The Rectangle class is defined with an __init__ method that initializes
    # width and height instance variables.
    # It also defines an area method that calculates and returns
    # the area of a rectangle using the width and height instance variables.
    def __init__(self, width, height):
        self.width = width  # Initialize width instance variable
        self.height = height  # Initialize height instance variable

    def area(self):
        return self.width * self.height  # Return area of rectangle


 # The Circle class is defined with an __init__ method
 # that initializes a radius instance variable.
 # It also defines an area method that calculates and
 # returns the area of a circle using the radius instance variable.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius instance variable

    def area(self):
        return 3.14 * self.radius ** 2  # Return area of circle using pi * r^2

# The shapes list is created with one Rectangle object and one Circle object. The for
# loop iterates over each object in the list and calls the area method of each object
# The output will be the area of the rectangle (20) and the area of the circle (153.86).
shapes = [Rectangle(4, 5), Circle(7)]  # Create a list of Shape objects
for shape in shapes:
    print(shape.area())  # Output the area of each Shape object
