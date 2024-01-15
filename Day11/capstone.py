from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def player():
        a = 2
        player_cards = random.sample(cards,a)
        score_player = sum(player_cards)
        print(f"Your cards: {player_cards}, score: {score_player}")
        if player_cards == ["11","10"]:
              print("User has Blackjack the user wins!!")
        else:

            print(f"Your cards: {player_cards}, score: {score_player}")


def dealer():
        b = 2
        dealer_cards = random.sample(cards,b)
        score_dealer = sum(dealer_cards)
        print(f"Computer\'s first card: {dealer_cards[0]}")
        if dealer_cards == ["11","10"]:
               print("User has Blackjack the user wins!!")
        else:
            print(f"Computer\'s first card: {dealer_cards[0]}")


play = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
if play == 'y':
        print(logo + "\n")
        user = player()
        computer = dealer()
        print(user)
        print(computer)
elif play == 'n':
        print("")