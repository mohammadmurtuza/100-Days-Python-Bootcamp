#range
for number in range(1, 10): # in range starting from 1 to 10 but not inclusing 10 so 1 to 9.
    print(number)

for number1 in range(1, 11, 3): # in range starting from 1 to 11 but not inclusing 11 so 1 to 10 but with a step size of 3 to op would be 1 4 7 10
    print(number1)

sum = 0
for i in range(0,101): 
    sum += i
print(sum)

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
even = 0
for i in range(2,target,2):
  even += i
print(even)