
from art import *
print(logo1 + "\n")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(old_text,shift_amount,process):
    new_text = ""
    if process == "decode":
            shift_amount *= -1 # for decrypting
    for char in old_text: # go through each char of plain_text
        if char in alphabet:
            position = alphabet.index(char) # getting the index of each char       
            new_position = position + shift_amount # adding the shift amout to index
            new_char = alphabet[new_position] #changing index back to alphabets
            new_text += new_char
        else:
             new_text += char
    print(f"The {process}d text is {new_text}.")

continue_run = True
while continue_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(old_text=text,shift_amount=shift,process=direction)
    again = input("Type \'yes\' if you wanna go again, Type \'no\' to exit.\n").lower()
    if again == "no":
        continue_run = False
        print("Bye!!")

