# Logical operators
# A and B both has to be true for final true if either is flase then final is false
# A or B only one needs to be true for true. only if both are false then is result false
# not E this reverses condition it amkes true false and vice versa
a = 78
print(not a > 50) 

#rollercoater
print("Welcome to roller coaster!")
height = int(input("What is your height in cm? "))
ticket = int()
ticket = 0
bill = 0
if height > 125:
    print("yes you can go on the ride.")
    age = int(input("What is your age? "))
    if age < 12:
        ticket = 5
        print("Ticket is $5")
    elif age <= 18:
        ticket = 7
        print("Ticket is $7")
    elif age >= 45 and age <= 75:
        print("you ride for free")
    else:
        ticket = 12
        print("Ticket is $12")
    photo = input("Do You want a picture of you in the ride, which will cost extra $3? Y or N ")
    if photo == "Y":
        bill = ticket + 3
        print(f"Your final bill is {bill}")
    else:
        print("Your final bill is ",ticket)
else:
    print("Sorry, you are not tall enough!!")
    


