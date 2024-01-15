#docstrings
# the comment below are doc strings
def fromat_name(f_name,l_name):
    """take first and last names and format it to return the title case version
    """
    fname = f_name.title()
    lname = l_name.title()
    return f"{fname} {lname}"

x = input("first name: ")
y = input("last name: ")
fromat_name() # when you hover here at the parentheis you can see the docstring we made
    