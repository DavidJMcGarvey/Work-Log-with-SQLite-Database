"""Main page of program where user menu is activated"""
import entry
import search_functions


def start_menu():
    """
    Opens menu with user options
    """
    active_entry = True

    while active_entry:
        print("\na) Add New Entry"
              "\nb) Search Existing Entry"
              "\nc) Quit Program\n")
        task = input("> ")
        if task.lower() == 'a':
            entry.Entry()
        elif task.lower() == 'b':
            search_functions.search_menu()
        elif task.lower() == 'c':
            print("Thanks for using the work log!")
            active_entry = False
        else:
            print("\nThat was not an option")


if __name__ == '__main__':
    start_menu()
