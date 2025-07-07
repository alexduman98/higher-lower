import random

from art import logo , vs
from game_data import data

print(logo)

def format_data(acc1):
    name = acc1["name"]
    description = acc1["description"]
    country = acc1["country"]
    return f"{name},a {description}, from {country}"

def correct_option(choice_of_user):
    global score
    score+=1
    return f"Congratulation your score is: {score}"

def wrong_option(choice_of_user):
    global lives, score
    lives = lives - 1
    return f"Sorry {choice_of_user}, you lost. Your score: {score} !"



lives = 1
score = 0
account_A = random.choice(data)
#account_A = random.choice(data)
#print(account_A)
#print(len(data))

while lives > 0:
    account_B = random.choice(data)
    print(f"Option A: {format_data(account_A)}")
    print(vs)
    print(f"Option B: {format_data(account_B)}")
    user_choice = input("Who has more followers A or B ?")
    if account_A["follower_count"] > account_B["follower_count"]:
        if user_choice == "A":
            print(correct_option(user_choice))
        else:
            print(wrong_option(user_choice))
    else:
        if user_choice == "B":
            print(correct_option(user_choice))
        else:
            print(wrong_option(user_choice))

    account_A = account_B




