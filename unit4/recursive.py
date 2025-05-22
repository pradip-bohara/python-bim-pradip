#Recursive Solution some example

#Fibonacci numbers in range 1 to 100

def fibonacci(a, b, n):
    if a > n:
        return 0
    if a > 0:
        print(a, end=" ")

    c = a + b
    
    fibonacci(b , c , n ) # recursiv call

# call
a = 0
b = 1
n = 100
fibonacci(a, b, n)


# Example 2  Sum of Natural Numbers

def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n-1)

print(f"The sum of natural number 30 is: {sum_natural(10)}")


# Example 3 
# factorial of a number
def factorial(n):
    if n == 0 or n == 1: # Base Case
        return 1
    return n*factorial(n-1) # Recursive case

print(factorial(5)) # output 120

# Example 4  
# Calculate GCD Greatst Common Divisor



def gcd(a, b):
    if b == 0:  # Base case
        return a
    return gcd(b, a % b)  # Recursive case

print(gcd(28, 72))
# print(gcd(2, 4))
# Three number
def gcd_three_numbers(a, b, c):
    return gcd(gcd(a, b), c)

# Example usage
a, b, c = 48, 18, 30
print(gcd_three_numbers(a, b, c))  # Output: 6





# Example 5
# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:  # Base case
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, target)  # Move n-1 disks to auxiliary
#     print(f"Move disk {n} from {source} to {target}")  # Move nth disk to target
#     tower_of_hanoi(n - 1, auxiliary, target, source)  # Move n-1 disks to target

# Example usage
# tower_of_hanoi(3, "A", "C", "B")


# ================ Lambda funciton

# number is Even
is_even = lambda x : x % 2 == 0

print(is_even(30)) # output true

# Filter Even numbers form a lsit
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]


#Map Function to
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]


# Anonymous Function Inside Another Function 

def multiply_by(n):
    return lambda x: x * n

double = multiply_by(2)
triple = multiply_by(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

abc = input("Enter the string :")
cont = 0
vowels = "aeiou"
for i in abc:
    if i.lower() in vowels:
        cont += 1

print(cont)

