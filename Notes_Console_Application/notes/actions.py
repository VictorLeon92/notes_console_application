import notes.note as model

class Actions:

    def create(self, user):
        title = input("Set the title of the note: ")
        descrption = input("Write the description: ")

        note = model.Note(user[0], title, descrption)
        save = note.save()

        if save[0] >= 1:
            print(f"\nPerfect! Your note {note.title} has been created correctly.")
        else:
            print(f"\nCouldn't save your note, {user[1]}. Please, try again later.")

    def view(self, user):
        note = model.Note(user[0])
        notes = note.list()

        for n in notes:
            print("\n*" * 30)
            print(n[2])
            print(n[3])
            print("\n*" * 30)

    def delete(self, user):
        title = input("\nWrite the title of the note you want to delete: ")

        note = model.Note(user[0], title)
        delete = note.delete()

        if delete[0] >= 1:
            print("\nThis note has been deleted correctly.")
        else:
            print("\nSomething happened. Please, try again later.")
