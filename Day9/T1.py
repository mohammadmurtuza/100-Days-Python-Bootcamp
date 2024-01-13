#dictionaries
'''
syntax:
key       | value
"Bug"     | "bug is something which makes your program run not in the intended way"
"function | "A piece of code which you can call over and over again"

{key : value}
dict = {"bug" : "bug is something which makes your program run not in the intended way", "function" : "A piece of code which you can call over and over again"}

'''

programming_dictionary = {
    "bug" : "bug is something which makes your program run not in the intended way", 
    "function" : "A piece of code which you can call over and over again", 
}



#retrieving items rom dict
print(programming_dictionary["function"])

#adding programitically
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create empty dictionary
empty_dictionary = {} #use curly

#edit an item in dictionary
programming_dictionary["bug"] = "wveve" #here assign the new value for bug and if there is no key named buf then it'll will create one

#wiping an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#loop through a dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) #using key to print the values