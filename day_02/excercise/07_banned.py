banned_words = ["moist", "break", "raise"]

user_input = input("One word:")
if user_input in banned_words:
    print("BANNED")
else:
    print("not a valid response")