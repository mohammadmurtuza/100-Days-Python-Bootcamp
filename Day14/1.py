import random
from Game_data import data
from art import logo,vs
import os


def random_account():
    return random.choice(data)

def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from{country}"

def check(guess,Fa,Fb):
    if Fa > Fb:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    account_a = random_account()
    account_b = random_account()

    again_game = True

    while again_game:

        account_a = account_b
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"COmpare B: {format_account(account_b)}")



        guess = input("Who do you think has more follower's, Type A or B. ").lower()
        f_a = account_a["follower_count"]
        f_b = account_b["follower_count"]
        iscorrect = check(guess,f_a,f_b)

        os.system("clear")
        print(logo)



        if iscorrect:
            score +=1
            print(f"that's correct, Current Score: {score}")
        else:
            print(f"That's wrong, Final Score: {score}")
            again_game = False





game()