
#Encapsulation: A class that represents a single abstraction in the game of chess.
"""
Encapsulation is the process of wrapping the data (variables) and code (methods) together in a single unit called a class.
Encapsulation helps in data hiding and data protection.
Data hiding is the process of restricting the access to the data members of a class.
Data protection is the process of preventing the data members of a class from being modified by external code.
Encapsulation can be achieved by using access specifiers such as public, private, and protected.
Public members are accessible from outside the class.
Private members are accessible only from within the class.
Protected members are accessible from within the class and its subclasses.
"""
# Example 1
class Person:
    def __init__(self, name, age):
        self._name = name # Protected member
        self.__age = age # Private member

    def display(self):
        return f"Name: {self._name}, Age: {self.__age}"
    
# Creating an instance of Person
person = Person("John", 30)
print(person.display()) # Output: Name: John, Age: 30
print(person._name) # Output: John
# print(person.__age) # Error: 'Person' object has no attribute '__age'

# access modifiers: public, private, protected
# this called data hiding or data protection 

# Encapsulation is the process of wrapping the data (variables) and code (methods) together in a single unit called a class.
# Encapsulation helps in data hiding and data protection.
'''
Public: Public members are accessible from outside the class.
Private: Private members are accessible only from within the class.
Protected: Protected members are accessible within the class and its subclasses. inherate class.
'''
class Circle:
    def __init__(self, radius):
        self.__radius = radius   # Private member defined using double underscore

    def get_radius(self):   # Getter method to get the value of the private member defined using double underscore
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

# Creating an instance of Circle
c = Circle(5)    # Output: 5
print(c.get_radius()) # Output: 5
c.set_radius(10)    # Output: 10

# Example 2
# Using protected members
class A:
    def __init__(self):
        self._x = 10    # Protected member defined using a single underscore

class B(A):
    def display(self):
        return self._x

# Creating an instance of B
b = B()
print(b.display()) # Output: 10


# Example 3
# Using public
class A:
    def __init__(self):
        self.x= 10     # Public member defined without an underscore

class B(A):
    def display(self):
        return self.x
    
# Creating an instance of B
b = B()
print(b.display()) # Output: 10
'''
In the above example, the x variable is a public member of the A class.
The B class inherits from the A class, so it can access the x variable.
'''

# method access modifiers
'''
Public: Public methods are accessible from outside the class.
Private: Private methods are accessible only from within the class.
Protected: Protected methods are accessible within the class and its subclasses.
'''
class A:
    def __init__(self):
        self.x = 10

    def public_method(self):
        return "Public method"

    def _protected_method(self): # Protected method defined using a single underscore
        return "Protected method"

    def __private_method(self):     # Private method defined using double underscore
        return "Private method"

# Creating an instance of A
a = A()
print(a.public_method())    # Output: Public method
print(a._protected_method())    # Output: Protected method
print(a._A__private_method())    # Output: Private method
'''
In the above example, the public_method() method is a public method of the A class.
The _protected_method() method is a protected method of the A class.
The __private_method() method is a private method of the A class.
'''