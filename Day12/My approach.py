from random import randint
from art import logo

def number_guesser():

    def check(x):
        if x > answer:
            print("Too High!!")
        elif x < answer:
            print('Too Low!!')

    def calculate(attempts):
        again = False
        while not again:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == answer:
                print(f"You got it! the answer was {answer}")
                again = True
            else:
                attempts -= 1
                if attempts == 0:
                    print("You ran out of guesses, You Lose!!")
                    again =True
                else:
                    check(x=guess)
                    print("Guess again!")


    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        attempts = 10
        calculate(attempts=attempts)
    elif level == 'hard':
        attempts = 5
        calculate(attempts=attempts)
    

print(logo)
print("Welcome to the Number Guessing Game")
answer = randint(1,100)
print(answer)
print("I'm thinking of a number between 1 and 100.")

number_guesser()
    





