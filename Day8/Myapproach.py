print("Caesar CIpher!!!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice = input("Type \'encode\' to encrypt, type \'decode\' to decrypt:\n").lower()

def encode(en_message,en_shift):
    cipher_text = ""
    for letter in en_message: # go through each letter of plain_text
        position = alphabet.index(letter) # getting the index of each letter
        new_position = position + en_shift # adding the shift amout to index
        new_letter = alphabet[new_position] #changing index back to alphabets
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}.")

    
def decode(de_message,de_shift):
    print("Decoding")

def MessShift(option):
    message = input("Type your message: \n").lower
    shift = int(input("Type the shift number: \n"))
    if option == "encode":
        encode(en_message=message,en_shift=shift)
    elif option == "decode":
        decode(de_message=message,de_shift=shift)
    

    again = input("do you wana go again \'Yes\' or \'No\': \n").lower()
    if again == "yes":
        choice
    else:
        print("Bye!!")

if choice == "encode":
    MessShift(option=choice)
elif choice == "decode":
    MessShift(option=choice)

