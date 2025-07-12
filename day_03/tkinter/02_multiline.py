import tkinter

root = tkinter.Tk()
root.title("HELLO WORLD")
root.geometry("1920x1080")
message = """
Hello
World
"""

label = tkinter.Label(root, text=message)
label.pack()

root.mainloop()