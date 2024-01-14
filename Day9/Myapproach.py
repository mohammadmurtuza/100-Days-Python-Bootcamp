import os
from art import logo

print(logo + "\n")
print("Welcome to the secret auction program. \n")

def winner(contestant):
    highest_bid = 0
    for key in contestant:
        a = key
        b = contestant[key]
        

        if user > 1:
            if b > highest_bid:
                highest_bid = b
        else:
                highest_bid = b

    os.system("clear")   
    print(f"The Winner is {a} with a bid of ${highest_bid}")

user = int()
players = {}
more_bid = True
while more_bid:
    name = input("What is your Name?  \n").lower()
    bid = int(input("What is your Bid?  \n$"))
    
    players[name] = bid
    next = input("Are there any more bidders, Type Yes or No.\n").lower()
    if next == "no":
        more_bid = False
        print("Thankyou for bidding. winner will be announced soon.")
        winner(players)
    elif next == 'yes':
        user += 1
        os.system("clear")
        print("")
