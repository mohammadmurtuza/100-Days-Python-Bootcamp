#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# password = ""
# for i in range(1,20):
#     password += random.choice(letters)

# for i in range(1,7):
#     password += random.choice(numbers)

# for i in range(1,5):
#     password += random.choice(symbols)

# print("The pass is ", password)

password_list = []

for i in range(1,10):
    password_list.append(random.choice(letters))

for i in range(1,10):
    password_list += (random.choice(numbers))

for i in range(1,10):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)

pas = ""
for i in password_list:
    pas += i
print(pas)


