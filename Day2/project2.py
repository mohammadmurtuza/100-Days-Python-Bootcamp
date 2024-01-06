print("Welcome to the tip calculator.")
total_bill = float(input('What was the total bill? $'))
tip = int(input("What percentage tip would you like to give? 10, 12, 0r 15?"))
person = int(input("How many people to split the bill? "))
bill_tip = tip / 100 * total_bill + total_bill
per_person_bill = round(bill_tip/person,2)
print(f"Each Person should pay: ${per_person_bill}")