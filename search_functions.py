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
        print(blue_row("="*36))
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
            clear_screen()
            return None
        else:
            print(red_err("That was not an option"))


def list_entries(entries):
    """Takes search query and provides list of dates associated with entries"""
    print("\nPlease choose from the following:")
    print("\n" + blue_row(" > "*3) + "\n")
    for entry in entries[:]:
        print(blue_row(" > " + entry.user + " --> " + str(entry.date)[:-9]))
    print("\n" + blue_row(" > "*3))
    list_search(entries)


def list_search(entries):
    """Takes list of entries and compares against """
    action = input("\n(Enter 'Q' anytime to QUIT)"
                   "\nType Employee Name AND Date from "
                   "list separated by a space: ")
    results = []
    for entry in entries:
        if action.upper() == 'Q':
            clear_screen()
            return None

        elif action == entry.user + " " + str(entry.date)[:-9]:
            results.append(entry)
            result = entry
            clear_screen()
            print("Your search: {}".format(action))
            print_entries(results)
        elif action != entry.user + " " + str(entry.date)[:-9] and results == []:
            result = entry

    if not result:
        print(red_err("Please select entry from list by typing "
                      "name and date separated by a space."))


def print_entry(entry):
    """Prints entry in readable format"""
    print("\n" + blue_row(" > "*3) + "\n")
    print(blue_row("User Name: " + entry.user))
    print(blue_row("Task Name: " + entry.task))
    print(blue_row("Task Date: " + str(entry.date)[:-9]))
    print(blue_row("Task Minutes: " + str(entry.time)))
    print(blue_row("Task Notes: " + entry.note))
    print("\n" + blue_row(" > "*3) + "\n")


def print_entries(entries):
    """Prints all entries"""
    for entry in entries:
        print_entry(entry)


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
        list_entries(results)
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
        if search.lower() in entry.task.lower():
            result = entry
            results.append(entry)
        elif search.lower() in entry.note.lower():
            result = entry
            results.append(entry)
        elif search.lower() != entry.task.lower() and results == []:
            result = None
        elif search.lower() != entry.note.lower() and results == []:
            result = None

    if result:
        print_entries(results)
    else:
        print(red_err("\nSorry, no keyword found. Please try again.\n"))

    return None
