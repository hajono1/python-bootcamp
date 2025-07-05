time = input("time?:")
pmam_question = input("am or pm?:")

if time >= "6" and pmam_question == "pm":
    print("Good Evening!")
elif time >= "3" and pmam_question == "am" and time < "11":
    print("Good Morning!")
elif time >= "1" and pmam_question == "pjjllm" and time < "6":
    print("Good Afternoon!")

