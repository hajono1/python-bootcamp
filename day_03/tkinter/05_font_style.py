import tkinter

root = tkinter.Tk()

label = tkinter.Label(
    root,
    text="Hello",
    font=("Blogger Sans", 14, "bold italic")
)
label.pack()

root.mainloop()