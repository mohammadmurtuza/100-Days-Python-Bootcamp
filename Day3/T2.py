#nested if else:
#roller coaster
print("Welcome to roller coaster!!")
height = int(input("What is your height in cm? "))
if height >=120:
    print("Yes, you are tall enough to go on this ride.")
    age = int(input("What is your age? "))
    if age > 18:
        print("your ticket price is $12 ")
    elif  age in range(12,18):
        print("your ticket is $7")
    else:
        print("your ticket price is $5")
else:
    print("sorry you need to grow more.")

# another way: without range() function
print("Welcome to roller coaster!!")
height = int(input("What is your height in cm? "))
if height >=120:
    print("Yes, you are tall enough to go on this ride.")
    age = int(input("What is your age? "))
    if age < 12:
        print("your ticket price is $5 ")
    elif  age <= 18:
        print("your ticket is $7")
    else:
        print("your ticket price is $12")
else:
    print("sorry you need to grow more.")
   