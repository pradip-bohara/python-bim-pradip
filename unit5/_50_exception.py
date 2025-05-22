#Python exception handling

# python has many built-in exception that are raised when a program encounter and error,

# Example 1 
#Divide by zero, that is a mathematical ture, 
#Built-in exception ZeroDivisionError:

def divide(dividend, divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError as abc:
        print('You can not divide by 0, ', abc)

divide(10, 20)

# Handling multiple exception using one exception block
def divide(dividend, divisor):
    try:
       
        print(dividend / divisor)
        var = 'str' +1 #can only concatenate str (not "int") to str
    except (ZeroDivisionError, TypeError )as abc:
        print(abc)
    finally:
        print('Executin finished')

divide(20, 10)

# custom exceptions
# Custome exception initialize by creating a 'class' that inherits form
#  the base 'Exception' class of python, and are raised using the 'raise' keyword: 

class MyCustomeException(Exception):
    pass

#Using the custom exception
try:
    raise MyCustomeException("This is a custom exception")
except MyCustomeException as a:
    print(a)

class InvalidAgeError(Exception):

    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def new_func(self):
        print(f"your age is normal: {self.age}")

try:
    user = int(input("Enter your age: "))
    if user < 0 or user > 120:
        raise InvalidAgeError(user)
    else:
        # No exception, age is valid
        exception_instance = InvalidAgeError(user)
        exception_instance.new_func()
    
except InvalidAgeError as e:
    print(e)
finally:
    print("Code turmenate")

# Custom Exception in a function 

class InsufficientBalanceError(Exception):
    """Exception raised when a withdrawal exceeds the account balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient balance. Available: {balance}, Requested: {amount}")

# A function using the custom exception
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

# Example usage
try:
    balance = 500
    amount = 600
    new_balance = withdraw(balance, amount)
    print(f"New balance: {new_balance}")
except InsufficientBalanceError as e:
    print(f"Error: {e}")
finally:
    "Thank you!"