# #local scope
# def drink_potion():
#     potion = 1
#     print(potion)

# drink_potion()
# print(potion) # this line gives error because the potion is defined within a function, it cannot be accessed outside so it can be only used within a function.

# # global scope:
player_health = 10

def drink():
    potion = 2 # this still amlocal variable
    print(player_health) # this get sprinted because player-health has been defined globally and can be used inside functiopn asweel

drink()

'''If you crete a declare a variable within a function then it can only be used in its scope that is uts own indent. But if you declare a varible in 
a if or while then it can be accessed all over no need to worry about the scope '''

gam_level = 3
enemies = ["zombie","skeletons"," alien"]

if gam_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# if i put this within a function then it wont work beacuse then you have to look f0r scope.'

gam_level = 3
def play():
    enemies = ["zombie","skeletons"," alien"]
    if gam_level < 5:
        new_enemy = enemies[0]

print(new_enemy)

# global constants
#  put the constants you dont wanna change in capital letter so whenever you type those and they come in capital yo know to not change these
PI = 3.14
URL = ""
