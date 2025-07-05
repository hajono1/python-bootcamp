correct_password = "pass"

#enter user password
password_input = input("Please provide password: ")

correct_password_given = password_input == correct_password
if password_input == correct_password:
    print("Access Granted")
else:
    print("Access Denied")
