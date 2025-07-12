import tkinter
from tkinter import messagebox

root = tkinter.Tk()

messagebox.showerror(
    "Wrong Password",
    "Incorrect password!"
)

root.mainloop()