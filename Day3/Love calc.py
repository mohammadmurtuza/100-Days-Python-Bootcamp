print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

names = name1.lower() + name2.lower() # concating both the names to find the letters from them

# finding number of times "true love" appears in names
t = names.count("t")
t1 = names.count("r")
t2 = names.count("u")
t3 = names.count("e")

l = names.count("l")
l1 = names.count("o")
l2= names.count("v")
l3 = names.count("e")
#concating the score 
score = int(str(t+t1+t2+t3) + str(l+l1+l2+l3))
print(score)
#score according to different conditions
if score < 10 or score > 90 : #using logical operator for if score is less than 10 or greater than 90 then this statement will print.
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50: #using logical operator for if score is in between 40 and 50 then this will print
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


