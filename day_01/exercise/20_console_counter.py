count = 0
stop_program = False

while not stop_program:
    choice = input("Provide command: ")
    if choice == "add":
        count = count + 1
        print(count)
    elif choice == "sub":
        count = count - 1
        print(count)
    elif choice == "double":
        count = count * 2
        print(count)
    elif choice == "exit":
        stop_program = True