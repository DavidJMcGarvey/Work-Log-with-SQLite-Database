"""Search menu and search functions"""

import os
import work_log


def red_err(message):
    """Return error message with red font """
    return "\33[91m" + message + "\33[0m"


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


def search_employee():
    """Search database by employee name"""
    search = input("Please type employee's name. ")
    return work_log.Entry.select().where(work_log.Entry.user.contains(search))


def search_date():
    """Search database by date"""


def search_time():
    """Search database by time in minutes"""


def search_exact():
    """Search database by an exact keyword"""



