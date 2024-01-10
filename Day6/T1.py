#Functions
# name of a function follwed by parenthesis i.e, print()
#built in functions
print("hello")
num_char = len("hello")
print(num_char)
# own functions
def my_function():  # after def you can name it anything 
    print("hellooooo")
    print("byeeeee")

#calling the functions 
my_function()

def add(a,b):
    c = a+b
    print(c)

add(3,4)
'''example: you ask a robot to get the milk from shop then you have to give specific instructions to it like get out of house, 
go left 2 blocks, then rigth 5 blocks and so on but if you want milk everyday its very time consuming to give instruction its better to 
go and get it yourself but you can just put the instructions in a function like def get_milk() then you just have to run that function and the 
robot will do all the stuff without needing instructions from your side.
'''