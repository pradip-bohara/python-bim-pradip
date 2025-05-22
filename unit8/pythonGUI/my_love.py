# waht is GUI
# GUI, or Graphical user interface  is the visual way we interact with softwere.
#instead of typing inot a black screen we click, tyupe, and see response in 
# windows, buttons, and input fields.

# Tkinter?
### - built-in with python  no installation needed.
## simple to start, yet powerful for most GUI needs.
## lightweight and ideral for desktop applications.

import tkinter as tk

#create main window
root = tk.Tk()
root.title("🌸 Hello GUI")
root.geometry("300x200")

#create a label widget
# label = tk.Label(root, text="Hello, Prem! Welcome to Tkinter 🌷", font=("Arial", 12), fg="darkblue", bg="lightyellow")

# label.pack(pady = 20)

# rund the app
root.mainloop()