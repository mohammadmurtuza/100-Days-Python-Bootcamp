from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

print(menu.get_items())
choice = input("WHAT DO YOU WANT? ").lower() 
print(menu.find_drink(choice))