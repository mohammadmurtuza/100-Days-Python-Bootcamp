## nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# nesting a list in a dictionary
# for example you are making a dic called travel_log in which you write the names of countries and all the cities you have visited there

travel_log = {
   '''"France" : "Paris","lille", "dijon" # this is wrong you cannoit just separate the cities with comma and store then thats where list 
    comes in'''
    "France": ["Paris","Lille","Dijon"], # we made a list to store multiple values i.e multiple citites
    "USA": ["Nyc","Boston","Chicago"]
}
# you can also store list within lists
["A","B",["C","D"]] # here in the main list there are three items A, B, (C,D) and [C,D] are a another list within list.

#nesting dictionaries within dictionaries
travel_log = {
    "France": {"cities_visited" : ["Paris","Lille","Dijon"], "total visits" : 12 }, 
    "USA": {"Cities_to_cover": ["Nyc","Boston","Chicago"],"Budget": 3000},
}
# print(travel_log)

#nesting multiple dicts in list
#any data dype of things can be put together in a list but the "" of key : value must be respcted.
travel_log = [
    {"country": "France",  #string
     "cities_visited" : ["Paris","Lille","Dijon"],  #list
     "total visits" : 12  #int
     }, 
    {"country": "USA",
     "Cities_to_cover": ["Nyc","Boston","Chicago"],
     "Budget": 3000
     },
]
travel_log.append({"country":"Brazil","cities_visited" : ["sao paola","rio"],"total_visits":5})
print(travel_log)