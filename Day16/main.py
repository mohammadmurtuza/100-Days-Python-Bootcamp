from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()



again = True
while again:
    options = menu.get_items()
    user = input(f"What would you like? {options}: ").lower()
    if user == 'off':
        again = False
    elif user == 'report':
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(user)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)





