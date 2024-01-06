#tip calculator
print("Welcome to tip calculator.")
total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?"))
tip= int(input("Enter the tip 10,12 or 15? :"))
amount = float()
if tip == 10:
    amount = 10%total
elif tip == 12:
    amount = 12%total
elif tip == 15:
    amount = 15%total
else:
    print("enter a valid tip")
a=total/people
b=amount/people
per_person = a + b
print("Each person should pay: $",per_person)
print(f"per person share is {a}, and total tip is {amount}, per person tip is {b}")

