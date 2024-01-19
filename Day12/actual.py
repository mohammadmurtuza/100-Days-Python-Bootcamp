from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
global again
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!!")
        return turns - 1
    else:
        print(f"You got it!, the number was {answer}")


def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    answer = randint(1,100)
    print(answer)
    print("I'm thinking of a number between 1 and 100.")
    turns = difficulty()
    guess = 0
    while guess != answer:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            turns = check_answer(guess, answer, turns)
            if check_answer == 0:
                print("You have no more guesses, you lose!")
            elif check_answer != answer:
                print("Guess again!")

game()