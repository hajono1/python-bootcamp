import tkinter
from tkinter import simpledialog

root = tkinter.Tk()

def ask_all():
    name = simpledialog.askstring("Name", "Enter your name")
    age = simpledialog.askinteger("Age", "Enter your age")
    score = simpledialog.askfloat("Score", "Enter your score")

    print(name, age, score)

button = tkinter.Button(root, text="Start", command=ask_all).pack()
root.mainloop()

root.mainloop()