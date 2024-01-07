#rollercoater
print("Welcome to roller coaster!")
height = int(input("What is your height in cm? "))
if height > 125:
    print("yes you can go on the ride.")
    age = int(input("What is your age? "))
    photo = bool(input("Do You want a picture of you in the ride, which will cost extra $3? "))
    if age < 12:
        ticket = 5
        if photo == "yes" or "Yes" or "YES":
            print(f"Your ticket price is {ticket + 3}.")
        else:
            print("Your ticket is $5")      
    elif age <= 18:
        ticket = 7
        if photo == "yes" or "Yes" or "YES":
            print(f"Your ticket price is {ticket + 3}.")
        else:
            print("Your ticket is $7")
    else:
        #
        ticket = 12
        if photo == "yes" or "Yes" or "YES":
            print(f"Your ticket price is {ticket + 3}.")
        else:
            print("Your Ticket is $12")
else:
    print("Sorry, you are not tall enough!!")
    


