import os
#get the current woking directory
print(os.getcwd())

# new create direc
os.mkdir("new_directory")

# list of crrrent direcory 
print(os.listdir())

# get the size fo a file 
file_size = os.path.getsize("file.txt")
print(file_size)