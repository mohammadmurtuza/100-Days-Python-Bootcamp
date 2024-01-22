MENU = {
    "espresso":{
        "ingredients": {
            "water": 50,
            "coffee": 18,
        }, "cost" : 1.50,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        }, "cost": 2.50,
    },
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        }, "cost": 3,
        
    }

}

money = 0
resource = { 
    "water":300,
    "milk": 200,
    "coffee": 100,
}
def coins():
    print("please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    value = (0.25*quarters)+(0.10 * dimes)+(0.05*nickels)+(0.01*pennies)
    print(f"You gave ${value}")
    return value

def check_resource(x):
    for item in x:
        if x[item] > resource[item]:
            print("Sorry there is not enough {item}")
            return False
        return True
def successful(payment_recieved,cost):
    if payment_recieved >= cost:
        bill = payment_recieved - cost
        print(f"here is ${round(bill,2)} in change.")
        global money
        money += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user, drink):
    for item in drink:
        resource[item] -= drink[item]
    print(f"Here is your {user} ☕️. Enjoy!")
     

again = True
while again:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user == 'off':
        again = False
    elif user == 'report':
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[user]
        if check_resource(drink["ingredients"]):
            payment = coins()
            if successful(payment,drink["cost"]):
                make_coffee(user,drink["ingredients"])
            

