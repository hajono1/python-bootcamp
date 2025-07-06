word_bank = {
    "Fruits": ["apple", "banana", "cherry", "mango"],
    "Animals": ["cat","dog","elephant","lion"],
    "Countries":["India","Brazil","France","Japan"]
}

print("Current Categories: 1. Fruits 2. Animals 3. Countries")
user_choice = input("Choose a category: ")

from random import choice

possible_words = word_bank[user_choice]
word = choice(possible_words)

print(word)

user_answer = input("What letter?: ")

hidden = [True, True, True, True, True]

for index,letter in enumerate(word):
   if user_answer == hidden:
       hidden[index] = False

#hidden
