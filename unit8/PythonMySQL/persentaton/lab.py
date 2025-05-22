import mysql.connector
# Create a connection object
connect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Pream@142',
    port=3307,
)
# Create a cursor object
cursor = connect.cursor()
# create a new database
cursor.execute("CREATE DATABASE StudentDB")
print("Database created successfully?")
#close connection.
cursor.close()
connect.close() 