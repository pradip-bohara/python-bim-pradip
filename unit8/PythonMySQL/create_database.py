import mysql.connector

connect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Pream@142',
    port=3307,
)

cursor = connect.cursor()
# create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
print("Database created successfully?")
#close connection.
cursor.close()
connect.close()