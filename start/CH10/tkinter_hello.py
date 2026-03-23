# First tkinter script
# Create by Diana Landon 3/22/26

# Import tkinter

# Create the GUI main window

# Add widgets

# Enter the main event loop

import tkinter

def greet_user():
  name= name_entry.get()
  result_label.config(text="Hello, + name + "Today will be a great day!")

root = tkinter.Tk()
root.title("Hello, Tkinter!")

tkinter.Label(root, text="What is your name?").pack()
name_entry = tkinter.Entry(root)
name_entry.pack()
tkinter.Button(root, text="submit", command=greet_user).pack()

result_label = tkinter.Label(root, text="")
result_label.pack()

root.mainloop()
