#lists
#list is a data structure
fruits = ["apple","Grape","orange","pineapple"] #syntax
print(fruits)
# order in the list is as you enter it in like below you entered apple first so you get apple at index [0]. and for coders numbers start at 0. 
print(fruits[0]) #item in list at index 0
print(fruits[-1]) # use -negative index to start from from end.
fruits[3] = "banana" # chnaging something at a particular index 
print(fruits)

fruits.append("strawberry") # adding an item at the end of the list
print(fruits)

fruits.extend(["guava","apricot","cranberry","blueberry"]) # adding multiple items at the end of the list
print(fruits)

print(fruits.index('banana')) #finding at what index is the particular item

fruits.pop() #removes the item at the end of the list
print(fruits)

print(len(fruits))
#print(fruits[8]) # we get index at out of range error because although items in list are 8 but indexing starts from 0 

length = len(fruits)
print(fruits[length-1]) # while printing this i am getting the last item in my list beacuse length does not start from 0 but indexing does so we do - 1

if fruits[2] == 'grapes': # checking if lists are case senitive or not, yes they are.
    print(True) 
else:
    print(False)