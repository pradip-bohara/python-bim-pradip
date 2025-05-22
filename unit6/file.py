file = open('file.txt', 'r')

text =file.read()
print(text)

file.close()

#using with statement in file handling
with open('file.txt', 'r') as file:
    data = file.read()
    print(data)

#using with write file 
with open('file.txt', '+a') as f:
    f.write("hello this add line using append without deltet provius data")

""""
os.path.isfile(Path): check if a paht is afile.
os.chdir(path): chage the current working dicronary

"""
