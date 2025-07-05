from random import choice
options = ["rock", "paper", "scissors"]
random_option = choice(options)

#USER CHOICE
try:
    user_choice = input("Pick and choice (rock/paper/scissors): ")
    if not (user_choice == "rock" or user_choice == "paper" or user_choice == "scissors"):
        raise ValueError()
    #IF ANSWERS
    if random_option == "rock" and user_choice == "paper":
        print("PLAYER WINS")
    elif random_option == "paper" and user_choice == "scissors":
        print("PLAYER WINS")
    elif random_option == "scissors" and user_choice == "rock":
        print("PLAYER WINS")
    elif random_option == "scissors" and user_choice == "scissors":
        print("NOONE WINS")
    elif random_option == "rock" and user_choice == "rock":
        print("NOONE WINS")
    elif random_option == "paper" and user_choice == "paper":
        print("NOONE WINS")
    else:
        print("CPU WINS")

    #CPU ANSWER
    print(random_option)
except:
    print("NOT AN OPTION")