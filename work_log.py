from entries import Entry


def start_menu():
    """
    Opens menu with user options
    """
    while True:
        print("\na) Add New Entry"
              "\nb) Search Existing Entry"
              "\nc) Quit Program\n")
        task = input("> ")

        if task.lower() == 'a':
            new_entry = Entry()
            # add_entry()
        elif task.lower() == 'b':
            search_menu()
        elif task.lower() == 'c':
            print("Thanks for using the work log!")
            break
        else:
            print("That was not an option")


if __name__ == '__main__':
    start_menu()
