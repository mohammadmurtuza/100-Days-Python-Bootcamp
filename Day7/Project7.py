import random
import os
from Hangman_art import *
from hangman_words import word_list


print(logo + "\n")
words = ["inception"]#,"divergent","titanic","transformers","jurrasicpark","gameofthrones","bigbangtheory","up","nemo","cars"]
word = random.choice(words)
display = []
for _ in range(len(word)):
    display += "_"
print(display)

lives = 6
end = False
while not end:
    char = input("\nGuess a word: ").lower()
    os.system("clear")

    if char in display:
        print("You already Guessed it.")

    for position in range(len(word)): 
        letter = word[position] # here "letter" is assigned the character at the index position of word for eg inception[3] will be e. 
        if letter == char: #if it matches with user input then its put in the display .
            display[position] = letter

    if char not in word:
        print(f"You enterd {char}, thats a wrong letter, you lose a life.")
        lives -= 1
                   
        if lives == 0:
            end = True
            print("You Lose.!!")

                
    
    print(display) 
    if "_" not in display:
        end = True
        print("You Won!!")
        
   
    print(stages[lives])
