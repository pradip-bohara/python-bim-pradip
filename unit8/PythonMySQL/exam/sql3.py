import sqlite3 as sq
import os

# 📌 Step 1: Connect to the database
db_name = "school.db"
connect = sq.connect(db_name)
cursor = connect.cursor()

# 📁 Step 2: Print the database path
db_path = os.path.abspath(db_name)
print("📂 Your database lives at:", db_path)

# 🏗️ Step 3: Create the student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
     greade TEXT
)
""")

# 🌱 Step 4: Insert multiple student records (safe and elegant)
students = [
    ("Ram", 23, "A"),
    ("Sita", 22, "B"),
    ("Gita", 24, "A"),
    ("Hari", 21, "C")
]

cursor.executemany(" INTO student(name, age, greade) VALUES (?, ?, ?)", students)

# 📊 Step 5: Display records before update/delete
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print("\n🎓 Before update & delete:")
for row in rows:
    print(row)

# ✏️ Step 6: Update Ram's age
cursor.execute("UPDATE student SET age = ? WHERE name = ?", (24, "Ram"))

# ❌ Step 7: Delete a record (example: remove Hari)
cursor.execute("DELETE FROM student WHERE name = ?", ("Hari",))

# 📊 Step 8: Display records after update/delete
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print("\n🔁 After update & delete:")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM student WHERE greade = ?", ("A",))
rows = cursor.fetchall()
print("\n🎯 Students with grade A:")
for row in rows:
    print(row)

# 📁 Step 3: Save to a new file
file_path = "A_grade_students.txt"
with open(file_path, "w") as file:
    file.write("ID | Name | Age | Grade\n")
    file.write("-------------------------\n")
    for student in rows:
        file.write(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}\n")

print(f"\n📁 A-grade student list saved to: {os.path.abspath(file_path)}")


# ✅ Step 9: Commit changes and close everything cleanly
connect.commit()
cursor.close()
connect.close()
