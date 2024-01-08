# this program marks the X on given user input and replaces the item which is on the corresponding index with the X.

line1 = ["⬜","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# we are using if else to map each index with a keyboard which user can input like A1, B2 etc..
if position == "A1":
  map[0][0] = 'X'
elif position == "A2":
  map[1][0] = 'X'
elif position == "A3":
  map[2][0] = 'X'
elif position == "B1":
  map[0][1] = 'X'
elif position == 'B2':
  map[1][1] = 'X'
elif position == 'B3':
  map[2][1] = 'X'
elif position == "C1":
  map[0][2] = 'X'
elif position == "C2":
  map[1][2] = 'X'
elif position == "C3":
  map[2][2] = 'X'
else:
  print("")
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")