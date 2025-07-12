import tkinter

root = tkinter.Tk()

label = tkinter.Label(
    root,
    text="Hello",
    fg="red",
    bg="black",
    font = ("Chiller", 100),
    width=1_000,
    height=450
)
label.pack()

root.mainloop()