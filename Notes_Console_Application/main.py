"""
This app opens an assistant that asks for different options, all related to notes, like if you want to create one note, 
or read all of them.
Includes a register and a login option.
"""
from argparse import Action
from users import actions


print("""
Available actions:
    - register
    - login
""")

do = actions.Actions()
action = input("What do you want to do?: ")

if action == "register":
    do.register()
elif action == "login":
    do.login()
else:
    print("\nThis is not a valid command...")