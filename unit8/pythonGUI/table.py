import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Student Enrollment Form")
root.geometry("400x400")

# Variables
name_var = tk.StringVar()
email_var = tk.StringVar()
web_var = tk.StringVar()
img_var = tk.StringVar()
gender_var = tk.StringVar()
java_var = tk.BooleanVar()
html_var = tk.BooleanVar()
css_var = tk.BooleanVar()

# # Functions
# def enroll_student():
#     name = name_var.get()
#     email = email_var.get()
#     website = web_var.get()
#     image = img_var.get()
#     gender = gender_var.get()
#     skills = []

#     if java_var.get(): skills.append("Java")
#     if html_var.get(): skills.append("HTML")
#     if css_var.get(): skills.append("CSS")

#     if not name or not email or not website or not gender:
#         messagebox.showwarning("Missing Info", "Please fill all required fields!")
#         return

#     skill_str = ', '.join(skills)
#     print(f"Enrolled: {name}, {email}, {website}, {image}, {gender}, Skills: {skill_str}")
#     clear_form()

# def clear_form():
#     name_var.set("")
#     email_var.set("")
#     web_var.set("")
#     img_var.set("")
#     gender_var.set("")
#     java_var.set(False)
#     html_var.set(False)
#     css_var.set(False)

# Labels and entries
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=email_var).grid(row=1, column=1)

tk.Label(root, text="Website:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=web_var).grid(row=2, column=1)

tk.Label(root, text="Image Link:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=img_var).grid(row=3, column=1)

tk.Label(root, text="Gender:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=4, column=2, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=4, column=1)

tk.Label(root, text="Skills:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
tk.Checkbutton(root, text="Java", variable=java_var).grid(row=5, column=1, sticky="w")
tk.Checkbutton(root, text="HTML", variable=html_var).grid(row=6, column=1, sticky="w")
tk.Checkbutton(root, text="CSS", variable=css_var).grid(row=7, column=1, sticky="w")

# Buttons
tk.Button(root, text="Enroll Student").grid(row=8, column=0, pady=10)
tk.Button(root, text="Clear").grid(row=8, column=1)

# Run the application
root.mainloop()
