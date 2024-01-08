#Randomisation
import random

a= 15
b = 160
print(random.randint(a,b)) #generate random integer between a and b inclusive.
print(random.random()) #floating point between 0 and 1 but not including 1.
print(random.uniform(a,b)) #floating point .
print(random.randint(0,1))
score = random.randint(1,100)
print(f"Your love score is {score}")

num = random.randint(0,1)
if num == 0:
  print('Tails')
else:
  print('Heads')