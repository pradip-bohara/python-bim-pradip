# File handling
#File handling enables you to store data permanently and owrk with it by 
#performing operations such as reading, writing or appending content.
"""
Reading: Access and retrieve content form a file
Writing: Create a new file or overwrite an existing file with new content.
Appending: Add new data to the end of a existing file without deleting its content.

Types of all files
text files : .txt, .docs, .log etc

binary files: mp4, .mov, png, jpeg etc.
"""
# file opening modes 
'''  mode               Desciption

    'r'                 Read mode. opens a file for reading (default)
    'w'                 Write mode. opens file for writing creates or overwrites the file
    'a'                 Append mode. opens a file for appending; creates the fiel if it doesn't exist.
    'rb'                Read in binary mode
    'wb'                Write in binary mode.
    'x'                 Exclusive creation. fails if the file already exist.
'''

file = open("file.txt","r") # open in read mode
data = file.read()  #Read the files's content
print(data)     #print 
print(type(data))   #

file.close() #  Close the file

abc = open("file.txt", "a")
abc.write("\nHello this is without cahge by with statement")

abc.close()

oo = open("file.txt", "r")
print(oo.read())
oo.close()

""" Reading and Writing files 
read() reads the entire file.
readline() reads a single line.
readlines() reads all lnes and returns a list.
"""
"""
The with statement ensure propr handling of resources like file streams by
automatically closing teh file when the block is exited, even in the event of an exception.
"""

with open("file.txt", "r") as file:
    f = file.readline()
    print(f)
# no need to close the file; it is done automatically.

# Writing files
# write() writes a string to the file.
# writelines() writes a list of string to the file.

with open("file.txt", "w") as f:
    f.write("hello, World!\n")
    f.writelines("hello this is write a file ")
  
# appending Files
with open("file.txt", "a") as ab:
    ab.write("\nAppending a new line.")
 
#print read file agin

with open("file.txt", "r") as rea:
   d =  rea.read()
   print(d)


"""" The os Module and common functions
     The os module provides functions for interacting with the operating system, including file and directory management.

os.rename(old_name, new_name):             Renames a file.
os.remove(file_name):                      Delets a file.
os.mkdir(directory_name)                   Creates a new directory.
os.rmdir(directory_name)                   Removes an empty directory.
os.listdir(directory_name)                 Lists files and directories.
Os.path.exists(path)                       Checks if a file or directory exists.
"""
# import os
# print("Current Directory: ", os.getcwd())
# print("File in directory: ", os.listdir())
# print(os.getcwd())

import os
#check if a file exists

if os.path.exists("file.txt"):
    print("file exists")
else:
    print("file does not exist")
