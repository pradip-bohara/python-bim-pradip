import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Pream@142',
    # database = "my_database",
    port=3307
)

# Create a cursor
cursor = conn.cursor()

# Execute query to show all databases
cursor.execute("SHOW DATABASES")

# Fetch and print databases
print("Available Databases:")
for db in cursor:
    print(db[0])  # Extract database name from tuple

# Check which database is in use
cursor.execute("SELECT DATABASE()")
current_db = cursor.fetchone()
print("Currently using database:", current_db[0])


# Close cursor and connection
cursor.close()
conn.close()