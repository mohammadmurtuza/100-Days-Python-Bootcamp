from art import logo
import os

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul, 
    "/": div, 
    }


print(logo + "\n")
def calculator(): # this thing when we want to call the following code again is called recursion.
    again = True
    num_1 = float(input("What\'s the first number?: "))

    while again:
        for i in operations:
            print(i)
        operation = input("Pick an operation: ")
        num_2 = float(input("What's the next number?: "))
        cal = operations[operation]
        result = cal(num_1,num_2)

        print(f"{num_1} {operation} {num_2} = {result}")

        choice = input(f"Type \'y\' to continue calculating with the {result}, or type \'n\' to start a new calculation: ").lower()
        if choice == 'n':
            again = False
            os.system("clear")
            calculator()
        elif choice == 'y':
            num_1 = result

calculator() #to start the recursion function


