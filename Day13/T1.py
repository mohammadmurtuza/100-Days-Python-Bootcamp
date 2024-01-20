############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21): # here we had (1,20) so i was not reaching 20 and printing the below line so we change it to 21 so now i reaches 20 and prints the line of code.
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug (In this we were getting index out of range bacuse indexing starts from 0 and the numbers were starting fro 1 so when computer generates 6 it has to print the +1 logo from the list which is not there).
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num-1])
# #OR
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# # for i in range(len(dice_imgs)):
# #     dice_num == i
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994: # here when user inputs 1994 the output was nothing so we added a = sign after the < sign so we now 1994 gets an output.
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors 
# age = int(input("How old are you?")) # here we add the int() so the input string which user enters is converted to int so it can be used in the below if statement to compare.
# if age > 18:
#     print(f"You can drive at age {age}.") #here f was not put there in the fstring.
# else:
#     print(f"You cannot drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # here instead of assigning using '=' there was '--' which compares two values i.e. check is a equal to b and returns true of false.
# total_words = pages * word_per_page
# print(f"total words in your book are: {total_words}")

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) # here we were appending out of the loop thats why it was calculating and doubling it and in last appending it once so now when we  put it in the loop so now each item when doubled gets appended then next item from list a is taken and doubled and appended and so on.
#   print(b_list)

# mutate(a_list=[1,2,3,5,8,13])