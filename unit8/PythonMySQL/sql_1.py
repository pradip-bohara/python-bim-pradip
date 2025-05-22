"""" Working with Databases and Using SQL statements in Python"""

'''Databases is a collection of data in a organized way that can be easily
accessed. managed, and updated. or CRUD operatoin'''

# Python provide built-in support ofr databases, with sqlite3 as a lightweight database option.

# import mysql.connector # Importing the mysql.connector module
# mydb = mysql.connector.connect(
#     host='localhost',   # Hostname of the database
#     user='root',         # Username for the database
#     passwd='Pream@142', # Password for the database
#     port=3307,          # Default port is 3306
# )
# print("Connected successfully!") 
# # If the connection is successful, this message will be printed


# # print(mydb.connection_id)

import mysql.connector
# Create a connection object
connect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database = 'hotels',
)

if connect.is_connected():
    print("Connected to the database!")
else:
    print("Connection failed!")
    
# Create a cursor object
mycursor = connect.cursor()
mycursor.execute("SELECT * FROM hotel")
for i in mycursor:
    print(i)

