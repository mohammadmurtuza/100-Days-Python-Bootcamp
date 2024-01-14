def fromat_name(f_name,l_name):
    fname = f_name.title()
    lname = l_name.title()
    print(f"{fname} {lname}")

x = input("first name: ")
y = input("last name: ")
fromat_name(x,y)
    
# fromat_name("ANGELA","mohammad")

def fromat_name1(f_name,l_name):
    fname = f_name.title()
    lname = l_name.title()
    return f"{fname} {lname}"

x = input("first name: ")
y = input("last name: ")
a = fromat_name1(x,y)
print(a)

def fromat_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide input"
    fname = f_name.title()
    lname = l_name.title()
    print(f"{fname} {lname}")

x = input("first name: ")
y = input("last name: ")
fromat_name(x,y)