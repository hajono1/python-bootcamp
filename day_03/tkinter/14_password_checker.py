import tkinter

root = tkinter.Tk()
from tkinter import messagebox
entry = tkinter.Entry(root)
entry.pack()


user_input = tkinter.StringVar(root, value="Enter your password")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input():
    if entry.get() == "pass":
        message = "correct password!"
        user_input.set(message)
    else:
        message = "Incorrect password, Try Again."
        user_input.set(message)
        messagebox.showerror(
            "Wrong Password",
            "Incorrect password!"
        )


button = tkinter.Button(root, text="Submit", command=show_input)
button.pack()
root.mainloop()