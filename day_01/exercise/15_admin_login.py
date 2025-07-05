#
correct_username = "admin"
correct_password = "admin"


username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

if username_input == "admin" and password_input == "admin":
    print("Access Granted")
else:
    print("Access Denied")