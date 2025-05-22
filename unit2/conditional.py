#Control Statements  are fundamental constructs in programming that allow developers to control the flow of exectution within a program. 

# this statements include selection looping and otehr flow control mechanisms

#selection statements
# if statements


age = 18
if age >= 18:
    print("You ar eligible to vote.")

# match-case statement 
#The match-case statement introduced in python 3.10 it handle multiple conditons similar to a switch statement in other language.

# The match-case statement introduced in Python 3.10 handles multiple conditions, similar to a switch statement in other languages.
def get_day_type(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case "Saturday" | "Sunday":
            return "Weekend"
        case _:
            return "Invalid day"

print(get_day_type("Sunday"))


#if else statement
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult


#nested if statement
age = 18
if age >= 18:
    if age == 18:
        print("You just became an adult.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")



