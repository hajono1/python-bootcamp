import tkinter
import json

root = tkinter.Tk()
from tkinter import messagebox
#NAME////
entry = tkinter.Entry(root)
entry.pack()


name_input = tkinter.StringVar(root, value="Name")
label = tkinter.Label(root, textvariable=name_input)
label.pack()
#AGE////
entry2 = tkinter.Entry(root)
entry2.pack()

age_input = tkinter.StringVar(root, value="Age")
label = tkinter.Label(root, textvariable=age_input)
label.pack()

#THEME////
theme_input = tkinter.StringVar(root, value="Preferred Theme")
label = tkinter.Label(root, textvariable=theme_input)
label.pack()

radio_var = tkinter.StringVar(value="Option A")
radio1 = tkinter.Radiobutton(
root, text="Light", variable=radio_var, value="Option A")
radio1.pack()

radio2 = tkinter.Radiobutton(
root, text="Dark", variable=radio_var, value="Option B")
radio2.pack()
#Subscribe to newsletter
check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
root,
text="Subscribe to newsletter",
variable=check_value
)
checkbox.pack()
#Rate us////
rate_us = tkinter.StringVar(root, value="Rate us!")
label = tkinter.Label(root, textvariable=rate_us)
label.pack()
slider_value = tkinter.IntVar(value=1)
slider = tkinter.Scale(
root,
from_=1,
to=5,
orient="horizontal",
variable=slider_value
)
slider.pack()
#BUTTON////
def submit():
    user={
        "Name": entry.get(),
        "Age": entry2.get(),
        "Theme": theme_input.get(),
        "Subscribe": check_value.get(),
        "Rating": slider.get(),
    }
    with open('people.json', 'w' ) as file:
        json.dump(user, file, indent=4)
button = tkinter.Button(root, text="Submit", command=submit)
button.pack()
root.mainloop()