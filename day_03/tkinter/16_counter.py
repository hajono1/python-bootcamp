import tkinter


root = tkinter.Tk()
count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()
def increment():
    new_value = count.get() + 1
    count.set(new_value)

def decrease():
        new_value = count.get() - 1
        count.set(new_value)


button = tkinter.Button(root, text=" + ", command=increment)
buttons = tkinter.Button(root, text=" - ", command=decrease)
button.pack()
buttons.pack()

root.mainloop()