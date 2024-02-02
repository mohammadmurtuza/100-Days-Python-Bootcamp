from prettytable import PrettyTable

table = PrettyTable() #table object prettytable class

table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"]) #table object add_column method
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l" #table object align attribute "l" left
print(table)