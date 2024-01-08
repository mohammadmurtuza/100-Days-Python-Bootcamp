#NESTED LISTS
'''dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
print(len(dirty_dozen))'''
# instead of doing this putting veggies and fruits together we can do another thing

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits,vegetables] # now we have a list which keeps fruits and vegetables separated but together
print(dirty_dozen)

print(dirty_dozen[0][1]) # this first[] selects the sub-list , the second[] selects the item at index in the sub-list. here list 0 and index 1 is Nectarines

