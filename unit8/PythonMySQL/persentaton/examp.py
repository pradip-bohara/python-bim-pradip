import mysql.connector
import os

# 🧭 Step 1: Connect to MySQL database
connect =  mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Pream@142',
    database = "my_database",
    port=3307
)

cursor = connect.cursor()

# 🏗️ Step 2: Create the student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    greade VARCHAR(5)
)
""")

# 🌱 Step 3: Insert multiple student records
students = [
    ("Ram", 23, "A"),
    ("Sita", 22, "B"),
    ("Gita", 24, "A"),
    ("Hari", 21, "C")
]

# 👇 Use executemany here
cursor.executemany("INSERT INTO student (name, age, greade) VALUES (%s, %s, %s)", students)

# 📊 Step 4: Display records before update/delete
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print("\n🎓 Before update & delete:")
for row in rows:
    print(row)

# ✏️ Step 5: Update Ram's age
cursor.execute("UPDATE student SET age = %s WHERE name = %s", (24, "Ram"))

# ❌ Step 6: Delete a record (e.g., Hari)
cursor.execute("DELETE FROM student WHERE name = %s", ("Hari",))

# 📊 Step 7: Display records after update/delete
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print("\n🔁 After update & delete:")
for row in rows:
    print(row)

# 🎯 Step 8: Select and save A-grade students
cursor.execute("SELECT * FROM student WHERE greade = %s", ("A",))
rows = cursor.fetchall()
print("\n🌟 Students with grade A:")
for row in rows:
    print(row)

file_path = "A_grade_students_mysql.txt"
with open(file_path, "w") as file:
    file.write("ID | Name | Age | Grade\n")
    file.write("-------------------------\n")
    for student in rows:
        file.write(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}\n")

print(f"\n📁 A-grade student list saved to: {os.path.abspath(file_path)}")

# ✅ Step 9: Commit and close
connect.commit()
cursor.close()
connect.close()
