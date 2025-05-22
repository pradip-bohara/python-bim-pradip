# Abstraction: A class that represents a single abstraction in the game of chess.
""" 
Abstraction is the process of hiding the implementation details and showing only the functionality to the user.
Abstraction can be achieved by using abstract classes and interfaces.
Abstract classes are classes that contain one or more abstract methods.
Abstract methods are methods that are declared but not implemented.
Abstract classes cannot be instantiated.
Interfaces are similar to abstract classes, but they cannot contain any implementation.
Interfaces can be implemented by classes.
"""

# Example 1
# how to create an abstract class in Python using the abc module.
# Abstract class with abstract methods using the abc module in Python in not use abc module you can use pass keyword instead of abc module

from abc import ABC, abstractmethod # ABC is a metaclass that is used to create abstract classes

class Animal(ABC):
    def __init__(self, name): # Constructor
        self.name = name

    @abstractmethod
    def speak(self): # Abstract method
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks

# Example 2
# Abstract class with abstract methods

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating an instance of Circle
circle = Circle(5)
print(circle.area()) # Output: 78.5
print(circle.perimeter()) # Output: 31.400000000000002

# Example 3
# Interface
class A(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

class B(A):
    def method1(self):
        return "Method 1"

    def method2(self):
        return "Method 2"

# Creating an instance of B
b = B()
print(b.method1()) # Output: Method 1
print(b.method2()) # Output: Method 2

# Example 4
# Import the abc module to define abstract classes and methods
from abc import ABC, abstractmethod

# Define an abstract class called Shape that has an abstract method called area
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area method for Rectangles
    def area(self):
        return self.width * self.height

# Define a Circle class that also inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement the area method for Circles
    def area(self):
        return 3.14 * self.radius ** 2

# Create a list of shapes that includes both Rectangles and Circles
shapes = [Rectangle(4, 5), Circle(7)]

# Loop through each shape in the list and print its area
for shape in shapes:
    print(shape.area())