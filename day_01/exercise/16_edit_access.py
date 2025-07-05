#
number = input("Enter role: ")

if number == "admin" or number == "editor":
    print("Edit access enabled")
else:
    print("Access Denied")