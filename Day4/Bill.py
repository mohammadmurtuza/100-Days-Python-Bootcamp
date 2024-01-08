import random
names = input("names separated by, ").split(", ") # the split function is taking inout from the user and putting it in the list separated by a comma
length = len(names) # len() function is finding how many items are there in the list
print(names)
bill = names[random.randint(0,length-1)]
''' we are randomly genrating a number 
from the length function and here length is -1 beacuse the index starts from
0 so if we input 4 names the length would be 4 and genrating random between 0 and 4 gives 5 numbers bet list only
has 4 so we do length -1 to account for the indexing starting from zero'''
print(f"{bill} is going to buy the meal today!")