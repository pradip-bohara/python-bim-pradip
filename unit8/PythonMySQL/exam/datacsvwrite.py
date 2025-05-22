import csv

# File name
filename = "students_data.csv"

# Header
header = ['Name', 'Age', 'Grade']

# Sample data (30 students)
data = [
    ['Alice', 14, 'A'], ['Bob', 15, 'B'], ['Charlie', 14, 'A+'],
    ['David', 13, 'B+'], ['Eve', 14, 'A'], ['Frank', 15, 'C'],
    ['Grace', 13, 'B'], ['Heidi', 14, 'A-'], ['Ivan', 14, 'B+'],
    ['Judy', 15, 'A'], ['Kevin', 13, 'C+'], ['Liam', 14, 'B'],
    ['Mia', 15, 'A+'], ['Nina', 14, 'B-'], ['Oscar', 13, 'A'],
    ['Pam', 14, 'B+'], ['Quinn', 14, 'A'], ['Rita', 15, 'A-'],
    ['Sam', 13, 'B+'], ['Tina', 14, 'C'], ['Uma', 15, 'A'],
    ['Victor', 13, 'B'], ['Wendy', 14, 'B+'], ['Xavier', 15, 'A'],
    ['Yara', 14, 'A-'], ['Zane', 13, 'C+'], ['Lara', 15, 'A+'],
    ['Noah', 14, 'B+'], ['Olivia', 13, 'A'], ['Peter', 14, 'B']
]

# Write to CSV file
with open(filename, 'w') as file:
    writer =csv.writer(file)
    writer.writerow(header)  # write the header
    writer.writerows(data)   # write the data

print("🌟 CSV file 'students_data.csv' created successfully with 30 records!")
