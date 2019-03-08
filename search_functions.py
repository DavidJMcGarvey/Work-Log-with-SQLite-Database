"""Search menu and search functions"""
import os
from work_log import Entry


def red_err(message):
    """Return error message with red font """
    return "\33[91m" + message + "\33[0m"


def blue_row(message):
    """To entries, adds a white font against blue background :)"""
    return "\33[37m\33[44m" + message + "\33[0m"


def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def search_menu():
    """Opens menu with different options for searching entries"""
    clear_screen()
    message = "What would you like to search by?"
    while True:
        print(blue_row("="*len(message)))
        print(message)
        print("\na) By Employee"
              "\nb) By Date"
              "\nc) By Time Spent"
              "\nd) By Keyword"
              "\ne) Return to Menu\n")
        search_task = input("> ")
        if search_task.lower() == 'a':
            search_employee()
        elif search_task.lower() == 'b':
            search_date()
        elif search_task.lower() == 'c':
            search_time()
        elif search_task.lower() == 'd':
            search_exact()
        elif search_task.lower() == 'e':
            return None
        else:
            print(red_err("That was not an option"))


def list_entries(entries):
    """Takes search query and provides list of dates asscoiated with entries"""
    print("\nHere are employees who have made an entry:\n")
    for entry in entries:
        print("> " + entry.user)
    action = input("What would you like to do next? Enter 'q' anytime to quit.")
    if action.lower() != 'q':
        print("Made it this far...")



def print_entry(entry):
    print("\n" + blue_row("User Name: " + entry.user))
    print(blue_row("Task Name: " + entry.task))
    print(blue_row("Task Date: " + str(entry.date)[:-9]))
    print(blue_row("Task Minutes: " + str(entry.time)))
    print(blue_row("Task Notes: " + entry.note))
    print(blue_row("=" * 34) + "\n")


def print_entries(entries):
    """Prints all entries"""
    for entry in entries:
        print_entry(entry)


# def display_entries(search_query=None):
#     """Take entry from database and display it"""
#     entries = Entry.select()
#
#     results = []
#     for entry in entries:
#         if entry.user == search_query:
#             results.append(entry)
#             print_entry(entry)
#
#         if entry.user != search_query:
#             print(red_err("Sorry, no match found."))


def search_employee():
    """Search database by employee name"""
    search = input("Please type desired employee: ")
    entries = Entry.select()

    results = []
    for entry in entries:
        if search == entry.user:
            result = entry
            results.append(entry)
        elif search != entry.user and results == []:
            result = None

    if result:
        list_entries(results)
    else:
        print(red_err("\nSorry, no match found. Please try again.\n"))

    return None


def search_date():
    """Search database by date"""
    search = input("\nPlease select desired date using YYYY-MM-DD format: ")
    search = (search + ' 00:00:00')
    entries = Entry.select()
    results = []

    for entry in entries:
        if str(search) == str(entry.date):
            result = entry
            results.append(entry)
        elif search != entry.date and results == []:
            result = None

    if result:
        print_entries(results)
    else:
        print(red_err("\nSorry, date not found. Please try again."))

    return None


def search_time():
    """Search database by time in minutes"""
    search = input("Please select task time in minutes: ")
    entries = Entry.select()

    results = []
    for entry in entries:
        if str(search) == str(entry.time):
            result = entry
            results.append(entry)
        elif search != entry.time and results == []:
            result = None

    if result:
        print_entries(results)
    else:
        print(red_err("\nSorry, no match found. Please try again.\n"))

    return None


def search_exact():
    """Search database by an exact keyword"""
    search = input("Please select desired keyword: ")
    entries = Entry.select()

    results = []
    for entry in entries:
        if search in entry.task:
            result = entry
            results.append(entry)
        elif search in entry.note:
            result = entry
            results.append(entry)
        elif search != entry.task and results == []:
            result = None
        elif search != entry.note and results == []:
            result = None

    if result:
        print_entries(results)
    else:
        print(red_err("\nSorry, no keyword found. Please try again.\n"))

    return None



