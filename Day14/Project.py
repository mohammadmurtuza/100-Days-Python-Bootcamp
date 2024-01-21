import random
from Game_data import data
from art import logo,vs
import os


def random_account():
    ''' generation a random account from the dictionary "data" which imported from Game_data.py'''
    return random.choice(data)

def format(account):
    ''' getting the values of keys of the account we randomly generated and returning the values'''
    name = account["name"]
    data = account["description"]
    country = account["country"]
    return f" {name}, a {data}, from {country}"

def check(guess, x, y):
    ''' checking if followers of account 'a' is greater than 'b' if yes then return 'guess = a ' i.e., user inputs 'a' and then go to check function
     where if input is 'a' then returns true only if followers of account a > b else returns false and exits the game '''
    if x > y:
        return guess == 'a'
    else:
        return guess == 'b'
            


def game():
    '''A simple game where two choices are given and the user is asked who has more instagram followers 'A' or 'B' if user guess correctly 
    then B becomes A and new B is generated and so on for every correct guess you get one point and when you make a wrong guess game exits with
    showing you final score'''
    print(logo)
    score = 0
    A = random_account()
    B = random_account()

    again_game = True
    while again_game:
        A = B
        B = random_account()

        while A == B:
            B = random_account()

        print(f"Compare A: {format(A)}")
        print(vs)
        print(f"Compare B: {format(B)}")
    
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        follower_a = A["follower_count"]
        follower_b = B["follower_count"]
        iscorrect = check(guess=choice,x=follower_a,y=follower_b)

        os.system("clear")
        print(logo)

        if iscorrect:
            score +=1
            print(f"That's correct, your current score is {score}")
        else:
            again_game = False
            print(f"Sorry that's wrong, final score {score}")

game()

