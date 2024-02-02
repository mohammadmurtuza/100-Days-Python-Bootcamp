"""The thing an object has is called attributes and the things that an object has to do are called methods
lets take an example in a restaurant there are many staff one of them is a waiter and the waiter here is an object 
his 
attributes: is_holding_plate = True
            tables_responsible = [4,5,6]

his 
methods": def take_order(table,order):
              take orders to the chef

          def take_payment(amount):
              add money to restaurant
              

so if we have a generalized waiter now we can make many waiters this blue print of a generalized waiter
is called class. now the object are the new waiters we made from the class (blueprint).
"""

# import another_module 

# print(another_module.variable)

# import turtle
# timmy = turtle.Turtle() #here timmy is an object created from a Turtle class(blueprint)

# #another way of importing
from turtle import Turtle, Screen
timmy = Turtle() #here timmy is an object created from a Turtle class(blueprint)
print(timmy)
#giving shape
timmy.shape("turtle") #timmy object shape method


#setting color
timmy.color("OliveDrab4") # timmy object color method


#move turtle forward 100 paces
timmy.forward(100)  #timmy object forward method


#attributes
my_screen = Screen()
print(my_screen.canvheight) # my_screen here is the object and the canvheight is the attribute


#methods
my_screen.exitonclick() #exitonclick is a method pre defined in the turtle class.