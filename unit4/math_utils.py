# math_utils.py

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("This is math_utils.py file.")

if __name__ == "__main__":
    # Test the factorial function
    print("Running directly:")
    print(f"Factorial of 5 is: {factorial(5)}")
