#ask user
user_input = input("Enter number: ").strip().replace(',', '')

valid_number = user_input.isnumeric()
if valid_number:
    user_input = int(user_input)
    print (user_input + 1)
else:
    print("Please enter a valid number!")
