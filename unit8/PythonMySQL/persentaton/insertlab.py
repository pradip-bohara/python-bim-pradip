
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
# Insert Sample Data
cursor.execute("""
    INSERT INTO students (name, age, email, course) VALUES
    ('John Doe', 25, 'john@example.com', 'Computer Science'),
    ('Alice Smith', 30, 'alice@example.com', 'Physics'),
    ('Bob Johnson', 28, 'bob@example.com', 'Mathematics')
""")
# Commit changes to the database 
connect.commit()
print("Data inserted successfully!")

cursor.close()
connect.close()