# Operator overloading in Python
# what is operator overloading?
# Operator overloading is a feature in Python that allows you to define the behavior of an operator for user-defined objects. In other words, you can define how an operator should behave when applied to objects of a class.
# Python provides special methods that you can define in your class to implement operator overloading. These special methods are called magic methods or dunder methods (double underscore methods).
# Example 1
# # Operator overloading for the addition operator (+)
# simple example of operator overloading for the addition operator (+).

# Magic methods  are special methods that are defined by double underscores. They are also called dunder methods.
# Magic methods are used to define the behavior of objects in Python. For example, you can define how an object should be represented, compared, or added using magic methods.
# Magic methods are always surrounded by double underscores. For example, __init__, __str__, __add__, etc.
# Magic methods are automatically called when certain operations are performed on objects. For example, the __add__ method is called when the + operator is used to add two objects.
# Example 1
# # Operator overloading for the addition operator (+)
# simple example of operator overloading for the addition operator (+).

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator (+)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"
# Creating instances of Point

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: (4, 6)
# In this example, we have defined the __add__ method in the Point class to overload
# the addition operator (+). When we add two Point objects using the + operator,
# the __add__ method is called, and the x and y coordinates of the two points are added together.
# The result is a new Point object with the sum of the x and y coordinates.
