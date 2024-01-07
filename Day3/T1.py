#conditional statements
#if/else
#either a or b
'''
if condition:
    do this
else:
    do this
'''
water_level = 50
if water_level > 80:
    print("draining the tub")
else:
    print("continue filling the tub")

#Rollercoaster ride eligiblity:
print("Welcome to the rollercoaster!!!!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("Yes, you can ride the rollercoaster.")
else:
    print("Sorry, you are a midget, you cannot go on this ride, go drink some complan.")

#costco:
print("Welcome to costco.")
member = input("Please enter your membership number: ")
if member.startswith("cos"): #checking starts with a particular string
    print("thank you sir for validating your identity.")
else:
    print("sorry, you are not a costco member")

#statements
    # > -- greater than
    # < -- less than
    # >=  greater than equal to
    # <=  less than equal to
    # != not equal to

print("welcome, to enter you must be only 18 years old, not younger not older!!!")
age = int(input("Age???"))
if age != 18:
    print("get lost from here")
else:
    print("welcome to the eden.")

#with boolean:
print("welcome, to enter you must be only 18 years old, not younger not older!!!")
age = bool(input("18??, yes or no?"))
if age == False:
    print("get lost from here")
else:
    print("welcome to the eden.")