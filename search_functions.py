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
    while True:
        print("\nWhat would you like to search by?")
        print("\na) By Employee"
              "\nb) By Date"
              "\nc) By Time Spent"
              "\nd) By Keyword"
              "\ne) Return to Menu\n")
        search_task = input("> ")
        if search_task.lower() == 'a':
            display_entries(search_employee())
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


def display_entries(search_query=None):
    """Take entry from database and display it"""
    entries = Entry.select().order_by(Entry)
    if search_query == Entry.user:
        for entry in entries:
            print("\n" + blue_row("User Name: " + entry.user))
            print(blue_row("Task Name: " + entry.task))
            print(blue_row("Task Date: " + str(entry.date)[:-9]))
            print(blue_row("Task Minutes: " + str(entry.time)))
            print(blue_row("Task Notes: " + entry.note))
            print(blue_row("="*34))


def search_employee():
    """Search database by employee name"""
    return input("Please type employee's name: ")


def search_date():
    """Search database by date"""


def search_time():
    """Search database by time in minutes"""


def search_exact():
    """Search database by an exact keyword"""



