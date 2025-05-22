# Witout function calculate factorial number
# 5 * 4 * 3 * 2* 1 = 120 
factroil = 1
num = 5
for i in range(1, 6):
    factroil *= i


print(factroil)

fact = 1
i = 1
while i <= num:
    fact *= i
    i +=1

print(fact)

# Fibonacci series 

n = 10
a, b = 0, 1

print("Fibonaci series:")
print(a, b, end =" ")

for i in range( 2, n):
    c = a + b
    print(c, end=" ")

    a,b = b,c

# prime number
nu = 29
print( nu)
if num > 1:
    is_prime = True
    for i in range(2, int(nu**0.5)+ 1):
        if nu % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{nu} is a prime number.")
    else:
        print(f"{nu} is not a prime number.")
else: 
    print(f"{nu} is not a prime number.")


# Generate prime numbers within a range
start = 10
end = 50

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")