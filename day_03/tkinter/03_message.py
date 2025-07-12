import tkinter

root = tkinter.Tk()

text = ("A quick brown fox jumped over the lazy dog,"
        "A quick brown fox jumped over the lazy dog "
        "A quick brown fox jumped over the lazy dog ")
message = tkinter.Message(root, text=text)
message.pack()

root.mainloop()