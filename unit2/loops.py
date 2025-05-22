# looping Statements 
'''
python there are two main types of loops:
for and while. Python does not have a do-while loop, 
but the behavior of a do_while loop can be simulated using a while loop. 
'''

# list of loop 
'''     1..    for
        2..    while
'''

# for loop
# the for loop in python is used to iterate over a sequence like a list, tuple, string, or range 
'''
for variable in sequence:
    #code block to execute
'''

# example 
numbers = [1, 3, 4, 5, 6, 7]  # lsit sequence
for num in numbers:
    print(num)

# using range to iterate over numbers

for i in range(1, 19): # range(start, stop)
    print(i)



# while loop 
# The while loop continues to execute as long as the  spedified condition evaluates to true.
'''  
while condition:
    # code block to exectue 
'''
#simple example loop
count = 1
while count <= 5:
    print(count)
    count +=1

# break and continue 

# pass statement is often used in unfinished code to avoid syntax errors.
for i in range(5):
    if i == 3:
        pass #placeholder
    else:
        print(i)

#outpur : 0, 1, 2, 4