# functions with more than one input
def greet_with(name,location):
    print(f"hello, {name}.")
    print(f"I see you are joining us from {location}.")

greet_with("Qam","India") # first argument gets assigned to first parameter and likewise for second. this is called positional arguments.

greet_with(location= "India",name=  "Qam") # in this order doesnot matter this is called keyword arguments.
