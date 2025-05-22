import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Pream@142',
    database = "my_database",
    port=3307
)
''''
A cursor is an object that allows you to interact with a 
MySQL database using Python. It helps execute SQL queries, 
fetch results, and manage transactions.
Imagine a cursor like a pointer that moves inside a database to perform actions such as: SELECT, INSERT, UPDATE, DELETE, 
Without a cursor, Python cannot communicate with the database.

'''
cursor = conn.cursor()
#cursor() is a method that creates a cursor object. it helps execute SQL queries, fetch results, and manage transactions. Imagine a cursor like a pointer that moves inside a database to perform actions such as: SELECT, INSERT, UPDATE, DELETE, Without a cursor, Python cannot communicate with the database. without a cursor, Python cannot communicate with the database.
# Create a table

# conn.cursor() creates a cursor object.
# execute() runs the SQL command.
# fetchall() retrieves all data.

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT,
        email VARCHAR(255) UNIQUE
    )
""")
print("Table created successfully!")

# Close connection
cursor.close()
conn.close()