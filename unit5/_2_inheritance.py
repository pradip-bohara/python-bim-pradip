# Inheritance in PYTHON
""" Inheritance is a fundamenta conept in object oriented programming(OOP) that allows a class to inherit attributes and methods from another class.
The class that inherits the attributes and methods is called the child class or subclass
       - The class whose attributes and methods are inherited is called the parent class or superclass.
       - Inheritance allows us to reuse the code and create a hierarchy of classes.
       - Inheritance is implemented using the class name in the class definition.
       - The child class can override the methods of the parent class.
       - The child class can also add new methods and attributes.
       - Types of Inheritance
            - Single Inheritance: A class inherits from only one parent class.
            - Multiple Inheritance: A class inherits from more than one parent class.
            - Multilevel Inheritance: A class inherits from a parent class, which in turn inherits from another parent class.
            - Hierarchical Inheritance: Multiple classes inherit from a single parent class.
            - Hybrid Inheritance: Combination of two or more types of inheritance.
"""
# Example 1
class Animal:
    def __init__(self, name): # Constructor
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal): # Dog class inherits from Animal class
    def spe(self):
        return f"{self.name} barks"

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.spe())  # Output: Buddy barks

# Example 2
# Multiple inheritance

class A:
    def method1(self):
        return "Method 1"
    
class B:
    def method2(self):
        return "Method 2"

class C(A, B): # C class inherits from A and B class it called multiple inheritance
    def method3(self):
        return "Method 3"
    
# Creating an instance of C
c = C()
print(c.method1()) # Output: Method 1

# Example 3
# Multilevel inheritances

""" supper() is used to call methods form a syperclass form subclass
    it is used to call parent class's __init__() method or other methods, 
    enabling code reuse and ensuring that the inherited functinality is properly extended or modified."""
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class student(person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age) # super() function is used to call the constructor of the parent class
        self.rollno = rollno

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}"
    
class marks(student): # marks class inherits from student class is called multilevel inheritance
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age, rollno) # super() function is used to call the constructor of the parent class
        self.marks = marks

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}, Marks: {self.marks}"

# Creating an instance of marks
m = marks("Ram", 20, 101, 90)
print(m.display()) # Output: Name: Ram, Age: 20, Roll No: 101, Marks: 90

m2 = student("pradip", 20, 101)
print(m2.display()) # Output: Name: pradip, Age: 20, Roll No: 101

# Multilevel inheritance is a type of inheritance in which a class inherits from a parent class, which in turn inherits from another parent class.
# Example 4
# Hierarchical inheritance
class car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display(self):
        return f"Name: {self.name}, Model: {self.model}"
    
class audi(car): # audi class inherits from car class
    def __init__(self, name, model, price):
        super().__init__(name, model) # super() function is used to call the constructor of the parent class
        self.price = price

    def display(self):
        return f"Name: {self.name}, Model: {self.model}, Price: {self.price}"
    
class bmw(car): # bmw class inherits from car class
    def __init__(self, name, model, price):
        super().__init__(name, model) # super() function is used to call the constructor of the parent class
        self.price = price

    def display(self):
        return f"Name: {self.name}, Model: {self.model}, Price: {self.price}"
class mercedes(car): # mercedes class inherits from car class
    def __init__(self, name, model, price):
        super().__init__(name, model) # super() function is used to call the constructor of the parent class
        self.price = price

    def display(self):
        return f"Name: {self.name}, Model: {self.model}, Price: {self.price}"
    
# Creating an instance of audi
a = audi("Audi", "A8", 100000)
print(a.display()) # Output: Name: Audi, Model: A8, Price: 100000

# Creating an instance of bmw
b = bmw("BMW", "X5", 90000)
print(b.display()) # Output: Name: BMW, Model: X5, Price: 90000

# Creating an instance of mercedes
m = mercedes("Mercedes", "C-Class", 80000)
print(m.display()) # Output: Name: Mercedes, Model: C-Class, Price: 80000

#  Hierarchical inheritance is a type of inheritance in which multiple classes inherit from a single parent class.
# In the above example, the audi, bmw, and mercedes classes inherit from the car class.


# # Example 5
# # Hybrid inheritance
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         return f"Name: {self.name}, Age: {self.age}"
    
# class marks(student): # marks class inherits from student class
#     def __init__(self, name, age, rollno, marks):
#         super().__init__(name, age) # super() function is used to call the constructor of the parent class
#         self.rollno = rollno
#         self.marks = marks

#     def display(self):
#         return f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}, Marks: {self.marks}"
    
# class sports:
#     def __init__(self, sport, rank):
#         self.sport = sport
#         self.rank = rank

#     def display(self):
#         return f"Sport: {self.sport}, Rank: {self.rank}"
    
# class result(marks, sports): # result class inherits from marks and sports class is called hybrid inheritance
#     def __init__(self, name, age, rollno, marks, sport, rank):
#         marks.__init__(self, name, age, rollno, marks)
#         sports.__init__(self, sport, rank)

#     def display(self):
#         return f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}, Marks: {self.marks}, Sport: {self.sport}, Rank: {self.rank}"
    
# # Creating an instance of result
# r = result("John", 20, 101, 90, "Football", 1)
# print(r.display()) # Output: Name: John, Age: 20, Roll No: 101, Marks: 90, Sport: Football, Rank: 1

# # Hybrid inheritance is a combination of two or more types of inheritance.
# # In the above example, the result class inherits from the marks and sports classes, which is an example of hybrid inheritance.

