import pandas as pd

#read csv file
df = pd.read_csv("students_data.csv")

print(df)
print(df.head(10))

# calculate avarage age of student

age_list = df["Age"]
print(age_list)

print(age_list.mean())



#lsit teh naem of studetn who scord an A grad

a_grid_student = df[df['Grade']== "A"][["Name", "Grade"]]

print(a_grid_student)

