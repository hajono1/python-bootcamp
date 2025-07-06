message = ("Mia Anderson","Ethan Roberts","Liam Johnson","Sophia Martinez", "Olivia Davis", "Noah Thompson")

with open("test.txt", "w") as file:
        file.write("New Line"+"\n")
        for person in message:
            file.write (person+"\n")