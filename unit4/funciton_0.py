#IN PYTHON, Function
""" Construct is used to ensure that a block of code runs only when hte script is executed direclty,
    and not when it is imported as a module in another script.
"""

def main():
    print("This is the main function.")

# if theis file is being run directly not imported, then execute the main() function. 
# ensure modularity and clarity.
if __name__ =="__main__":
    main()

