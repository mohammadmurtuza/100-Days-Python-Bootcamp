alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def caesar(old_text,shift_amount):
#     new_text = ""
#     for letter in old_text: # go through each letter of plain_text
#         position = alphabet.index(letter) # getting the index of each letter
#         if direction == "encode":
#             new_position = position + shift_amount # adding the shift amout to index
#         else:
#             new_position = position - shift_amount # adding the shift amout to index
#         new_letter = alphabet[new_position] #changing index back to alphabets
#         new_text += new_letter
#     if direction == "encode":
#                 print(f"The encoded text is {new_text}.")
#     else:
#                 print(f"The decoded text is {new_text}.")


    

# 

def caesar(old_text,shift_amount,process):
    new_text = ""
    if process == "decode":
            shift_amount *= -1 # for decrypting
    for letter in old_text: # go through each letter of plain_text
        position = alphabet.index(letter) # getting the index of each letter       
        new_position = position + shift_amount # adding the shift amout to index
        new_letter = alphabet[new_position] #changing index back to alphabets
        new_text += new_letter
    print(f"The {process}d text is {new_text}.")


caesar(old_text=text,shift_amount=shift,process=direction)





