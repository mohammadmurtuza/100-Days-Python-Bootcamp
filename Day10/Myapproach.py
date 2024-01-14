from art import logo

def calculation(x,y,z):
    global result
    if y == '+':
        result = x + z
        return f"{x} + {z} = {result}"
    elif y == '-':
        result = x - z
        print(f"{x} - {z} = {result}")
    elif y == '*':
        result = x*z
        print(f"{x} * {z} = {result}")
    elif y == '/':
        result = x/z
        print(f"{x} / {z} = {result}")

print(logo + "\n")

num_1 = int(input("What\'s the first number?: "))
print("+")
print("-")
print("*")
print("/")
again = True
while again:
    operation = input("Pick an operation: ")
    num_2 = int(input("What's the next number?: "))
    calculation(x=num_1, y=operation, z=num_2)  

    choice = input(f"Type \'y\' to continue calculating with the {result}, or type \'n\' to start a new calculation: ")
    if choice == 'n':
        again = False
    elif choice == 'y':
        num_1 = result
        # again = False

        
