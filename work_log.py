from entry import Entry


def start_menu():
    """
    Opens menu with user options
    """
    menu_active = True
    while menu_active:
        print("\na) Add New Entry"
              "\nb) Search Existing Entry"
              "\nc) Quit Program\n")
        task = input("> ")

        if task.lower() == 'a':
            pass
        elif task.lower() == 'b':
            search_menu()
        elif task.lower() == 'c':
            print("Thanks for using the work log!")
            menu_active = False
        else:
            print("That was not an option")


if __name__ == '__main__':
    start_menu()
