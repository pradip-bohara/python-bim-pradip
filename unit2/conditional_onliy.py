# All statement in one program with definition and examples or syntax 
# list 
'''     
        1..     if Statement
        2..     if...esle statement
        3..     if...elif...else Statement
        4..     match/ switch case Statement
'''

# Conditional Statements
# Conditional statements are used to execute different code blocks based on different conditions.

# if Statement
# The if statement is used to execute a block of code only if a specified conditon evaluates to ture 
'''  
    if conditon:
        #code to execute if condition is true
'''

# if Statemetn
# The if statement is used to execute a block of code only if a specified conditon evaluates to ture 
'''  
    if conditon:
        #code to execute if condition is true
'''
num = 18
if num > 10:
    print("num is greater than 10")

# if... else Statement
# The if... else statement adds an alternative block of code that executes if the if condition is false

'''
    if condition:
        #code if true
    else:
        #code if false
'''
n = 5 
if n > 10:
    print("n is greater than 5")
else:
    print("x is not greater than 10")

# if...elif...else statement
#used when multiple conditions need to be checked sequentially like switch

''''
    if condtion1:
        #code if true
    elif condition2:
        #code if true
    else:
        #code if true
'''
a = 5
b = 10
if a > b:
    result = a - b
    print("Result of subtrracion is ", result)
elif a < b:
    result = b - a
    print("Result of subtraction is ", result)

else:
    print("Both vaue")


# switch /match Statement ( introduced in ptyhon 3.10)
# The match statement is a new feature. it allows pattern matching similar to a switch statement in other languages. 

'''
    match expression:
        case pattern1:
            #code to ececute
        case pattern2:
            #code to execute
        case _:
            #code to execute if no patterns match (default case)

'''
status = 404
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")
 

 #=================================================== 
 #================= Using a single- line Ternary Operatero ==================
#  A shorthand way to write if...else statements for simple conditions. 

#syntax:
'''
variable = value_if_treu if condtion else value_if_false

'''

age = 18
states = "Adult" if age >= 18 else "minor"
print(states) # output = adult


na = 27
result = "Even" if na % 2 == 0 else "Odd"
print(result) # output = odd