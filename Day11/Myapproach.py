import random

def blackjack_player():
    no_cards_player = 2
    player_card = random.sample(cards,no_cards_player)
    return player_card


def blackjack_computer():
    no_cards_computer = 2
    computer_card = random.sample(cards,no_cards_computer)
    return computer_card[0]

def calclation(player,dealer):

    sum_player = sum(player)
    sum_dealer = sum(dealer)
    limit= 21

    if sum_player > sum_dealer and sum_player < limit:
        return f"The winner is player with {sum_player} points."
    elif sum_player < sum_dealer and sum_dealer < limit:
        return f"The winner is dealer with {sum_dealer} points."
    
    

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards =[]
computer_cards = []

def blackjack():
    play = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()

    if play == 'y':
        print("logo" + "\n")
        status = True
        while status:
            your = print(f"Your Cards: {blackjack_player()}")
            computers = print(f"Computer\'s first card: {blackjack_computer()}")
            x = user_cards.append(your)
            y = computer_cards.append(computers)

            another_round = input("Type \'y\' to get another card, type 'n' to pass: ").lower()
            if another_round == 'y':
                print("")

            elif another_round == 'n':
                calclation(x,y)
                status = False

    elif play == 'n':
        print("Bye!!")


blackjack()
    
