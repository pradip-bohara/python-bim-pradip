import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Pream@142',
    database = "my_database",
    port=3307
)

cursor = conn.cursor()
# Insert data into the table
query = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
values = [
    ("John Doe", 25, "john@example.com"),
    ("Alice Smith", 30, "alice@example.com"),
    ("Bob Johnson", 28, "bob@example.com")
]

cursor.executemany(query, values)  # Insert multiple records at once
conn.commit()  # Save changes commit() is needed to save the changes permanently.

print(cursor.rowcount, "records inserted successfully!")

# Close connection
cursor.close()
conn.close()