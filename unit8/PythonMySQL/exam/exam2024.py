#question paper using sqllite3

import sqlite3 as sq


#step 1 connect databsed college
db_name = "college.db"

#connect thsi db
connect = sq.connect(db_name)

cursor = connect.cursor()


#create a student table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS student(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name varchar(50),
    Address Varchar(50),
    Phone int(10),
    Semester varchar(20),
    Faculty Varchar(20)
    )"""
)

# insert multiple data
student = [
    ("Pradip", "KTM", 1234567890, "first sem", "BIM"),
    ("Ram", "Dha", 1234567890, "second sem", "BBM"),
    ("NIta", "Pokhar", 1234567890, "third sem", "BBB"),
    ("Manu", "KTM", 1234567890, "first sem", "BIM"),
    ("Hari", "Suketah", 1234567890, "fifth sem", "BIT")
]

cursor.executemany("INSERT INTO student(Name, Address, Phone, Semester, Faculty) VALUES (?, ?, ?, ?, ?)", student)

#display  the student who studied in fifth semester

cursor.execute("SELECT Name, Address FROM student WHERE Semester = ?", ("fifth sem",))

row = cursor.fetchall()

#display thsorw loop

for i in row:
    print(i)


cursor.execute("SELECT * FROM student")
data = cursor.fetchall()

#display all data throw loop
for info in data :
    print(info)
cursor.close()
connect.close()