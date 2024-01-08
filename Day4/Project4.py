import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
images = [rock,paper,scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if player >=3 or player < 0:
    print("Invalid number, You Lose!!!")
else:
    print(images[player]) # this will fetch the list for index which is the number user input
    computer = random.randint(0,2)
    print("Computer Chose: \n")
    print(images[computer]) # this will fetch the list for index which is randomly generated


    if player == computer:
        print("TIE!!!")
    elif player == 0 and computer == 2:
        print("You Win!!!!")
    elif player == 2 and computer == 0:
        print("You Lose!!!")
    elif player > computer:
        print("You Win!!!")
    elif player < computer:
        print("You Lose!!!")
