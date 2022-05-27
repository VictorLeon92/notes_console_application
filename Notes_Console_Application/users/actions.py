import users.user as model
import notes.actions

class Actions:
    
    def register(self):
        print("\nLet's start with your register!")
        name = input("What's your name?: ")
        surname = input("And your surname?: ")
        email = input("Tell me an email address: ")
        password = input("You need a password too, tell me one: ")

        user = model.User(name, surname, email, password)
        register = user.register()

        if register[0] >= 1:
            print(f"Perfectt, {register[1].name}, you have a new user account. Try login with your data.")
        else:
            print("Something happenned and i couldn't register your data. Please, try again.")

    def login(self):
        print("\nPerfect. Insert your user credentials.")

        try:
            email = input("What's your email address?: ")
            password = input("I need your password too: ")

            user = model.User('', '', email, password)
            login = user.identify()

            if email == login[3]:
                print(f'\nWelcome {login[1]}, today is {login[5]}.')
                self.nextActions(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f'Invalid email or password. Try again later.')

    def nextActions(self, user):
        print("""
        Available actions:
        - Create note (create)
        - View all (view)
        - Delete note (delete)
        - Exit application (exit)
        """)

        action = input("\nWhat do you want to do? ")
        doThis = notes.actions.Actions()

        if action == 'create':
            print("\nLet's create a note!")
            doThis.create(user)
            self.nextActions(user)
        elif action == 'view':
            print("\nHere you have all your notes:")
            doThis.view(user)
            self.nextActions(user)
        elif action == 'delete':
            print("\nTime to delete a note.")
            doThis.delete(user)
            self.nextActions(user)
        elif action == 'exit':
            print("\nSee you soon!")
            exit()
        else:
            print("\nThat is not a valid command...")
            self.nextActions(user)
