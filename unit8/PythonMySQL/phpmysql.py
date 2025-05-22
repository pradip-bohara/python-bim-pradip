import mysql.connector
# Create a connection object
connect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
)
if connect.is_connected():
    print("Connected to the database!")
else:
    print("Connection failed!")

# Create a cursor object
mycursor = connect.cursor()
mycursor.execute("Show databases")
for i in mycursor:
    print(i)

# Close connection
mycursor.close()
connect.close()

