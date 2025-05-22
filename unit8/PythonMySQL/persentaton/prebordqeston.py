import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",    # Change if needed
    user="root",         # Change to your MySQL username
    password="password", # Change to your MySQL password
    database="StudentDB" # Ensure the database exists
)
cursor = conn.cursor()

# Create a table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(10) NOT NULL
)
""")
conn.commit()

# Function to add a student
def add_student(name, age, grade):
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(sql, values)
    conn.commit()
    print(f"Student {name} added successfully!")

# Function to update a student's details
def update_student(student_id, name=None, age=None, grade=None):
    query = "UPDATE students SET"
    params = []
    
    if name:
        query += " name = %s,"
        params.append(name)
    if age:
        query += " age = %s,"
        params.append(age)
    if grade:
        query += " grade = %s,"
        params.append(grade)
    
    query = query.rstrip(',')  # Remove the last comma
    query += " WHERE id = %s"
    params.append(student_id)

    cursor.execute(query, tuple(params))
    conn.commit()
    print(f"Student ID {student_id} updated successfully!")

# Function to delete a student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    print(f"Student ID {student_id} deleted successfully!")

# Function to display all students
def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    if students:
        print("\nStudent Database:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
    else:
        print("No student records found.")

# Sample Usage
add_student("Alice", 20, "A")
add_student("Bob", 22, "B")
display_students()
update_student(1, age=21, grade="A+")
delete_student(2)
display_students()

# Close the database connection
conn.close()
