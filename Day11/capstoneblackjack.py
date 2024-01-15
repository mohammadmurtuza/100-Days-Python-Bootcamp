from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = []
computer_cards = []
def calculate_score(x,y):
        score_player = sum(x)
        score_dealer = sum(y)
        if 11 in player_cards and 10 in player_cards or 11 in computer_cards and 10 in computer_cards:
                return 0 
        
        elif 11 in player_cards or computer_cards:
               if score_player > 21:
                      player_cards.remove(11)
                      player_cards.append(1)
                      score_player = sum(x)

               elif score_dealer > 21:
                      computer_cards.remove(11)
                      computer_cards.append(1)
                      score_dealer = sum(y)
               return score_dealer and score_player
        else: 
            return score_player 

        
def deal_cards():
        a = 2
        b = 2
        user_cards = (random.sample(cards,a))
        player_cards.append(user_cards)
        dealer_cards = (random.sample(cards,b))
        computer_cards.append(dealer_cards)
        score_player = calculate_score(user_cards,dealer_cards)
        print(f"Your cards: {user_cards}, score: {score_player}")
        print(f"Computer\'s first card: {dealer_cards[0]}")


play = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
if play == 'y':
        print(logo + "\n")
        again = True
        while again:
            deal_cards()
            another = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()
            if another == 'y':
                   ""
            else:
                again = False



elif play == 'n':
        print("")


