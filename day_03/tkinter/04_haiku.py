import tkinter

root = tkinter.Tk()

text = ("Loops within loops spin,"
        "A silent function retuns,"
        "The logic is clear.")
message = tkinter.Message(root, text=text)
message.pack()

root.mainloop()