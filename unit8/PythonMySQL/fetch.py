import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Pream@142',
    database = "my_database",
    port=3307
)

cursor = conn.cursor()
# Fetch data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Display results
print("Before Update & Delete:")
for row in rows:
    print(row)

# Corrected UPDATE Query
cursor.execute("UPDATE users SET age = %s WHERE name = %s", (40, "Alice Smith"))
conn.commit()
print("Updated Alice Smith's age to 30.")

# Corrected DELETE Query
cursor.execute("DELETE FROM users WHERE name = %s", ("Bob Johnson",))
conn.commit()
print("Deleted user Bob Johnson.")

# Fetch updated data
cursor.execute("SELECT * FROM users")
updated_rows = cursor.fetchall()

# Display updated results
print("\nAfter Update & Delete:")
for row in updated_rows:
    print(row)

# Close connection
cursor.close()
conn.close()