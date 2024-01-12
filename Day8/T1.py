#functions again
#create a function called greet and add three print statements inside it and then call the greet function.
def greet():
    print("Hello")
    print("Hola")
    print("Ni Hao")

greet()

# now add persons name infront 
def greet_name(a): # here a is the parameter and 'Qam' from below is argument
    print("Hello",a)
    print(f"Hola, {a}")
    print(f"Ni Hao, {a}")

greet_name("Qam")
