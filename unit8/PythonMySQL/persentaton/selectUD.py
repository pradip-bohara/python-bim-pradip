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

# Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Display results
print("Before Update & Delete:")
for row in rows:
    print(row)

# Corrected UPDATE Query
cursor.execute("UPDATE students SET age = %s WHERE name = %s", (40, "Alice Smith"))
connect.commit()
print("Updated Alice Smith's age to 30.")

# Corrected DELETE Query
cursor.execute("DELETE FROM students WHERE name = %s", ("Bob Johnson",))
connect.commit()
print("Deleted user Bob Johnson.")

# Fetch updated data
cursor.execute("SELECT * FROM students")
updated_rows = cursor.fetchall()

# Display updated results
print("\nAfter Update & Delete:")
for row in updated_rows:
    print(row)

# Close connection
cursor.close()
connect.close()