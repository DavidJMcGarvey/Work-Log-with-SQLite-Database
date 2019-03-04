"""Search menu and search functions"""
import work_log


def red_err(message):
    """
    Return error message with red font
    """
    red_start = "\33[91m"
    color_stop = "\33[0m"
    return red_start + message + color_stop


def blue_row(task):
    """
    To entries, adds a white font against blue background :)
    """
    return "\33[37m\33[44m" + task + "\33[0m"


def search_menu():
    """
    Opens menu with different options for searching entries
    """
    while True:
        print("\nWhat would you like to search by?")
        print("\na) By Date"
              "\nb) By Minutes"
              "\nc) By Exact Keyword"
              "\nd) By Regex Pattern"
              "\ne) Show All Entries"
              "\nf) Return to Menu\n")
        search_task = input("> ")
        if search_task.lower() == 'a':
            search_date()
        elif search_task.lower() == 'b':
            search_time()
        elif search_task.lower() == 'c':
            search_exact()
        elif search_task.lower() == 'd':
            search_pattern()
        elif search_task.lower() == 'e':
            show_all()
        elif search_task.lower() == 'f':
            return None
        else:
            print(red_err("That was not an option"))


def search_employee():
    """Search database by employee name"""


def search_date():
    """Search database by date"""


def search_time():
    """Search database by time in minutes"""


def search_exact():
    """Search database by an exact keyword"""



