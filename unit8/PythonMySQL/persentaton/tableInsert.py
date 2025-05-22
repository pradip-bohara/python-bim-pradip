import mysql.connector
# Create a connection object
connect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Pream@142',
    database = "StudentDB",
    port=3307,
)
# Create a cursor object
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE students(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        email VARCHAR(100) UNIQUE,
        course VARCHAR(50)
    ) 
""")
print("Table created successfully!")
# Close connection
cursor.close()
connect.close()