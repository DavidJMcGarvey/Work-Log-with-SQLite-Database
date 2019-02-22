"""Search menu and search functions"""
import entry


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


def search_date():
    """
    Search based on exact date
    """
    search = input("\nPlease select desired date using YYYY-MM-DD format: ")
    search = (search + ' 00:00:00')
    entries = entry.db.select()
    results = []

    for row in entries:
        if search == row['date']:
            result = row
            results.append(row)
        elif search != row['date'] and results == []:
            result = None

    if not result:
        print(red_err("\nSorry, date not found. Please try again."))
    else:
        display_entries(results)

    return None


def search_time():
    """
    Search based on minutes spent on task
    """
    search = input("\nPlease type the minutes spent on desired task: ")
    entries = open_csv()
    results = []

    for row in entries:
        if search == row['time']:
            result = row
            results.append(row)
        elif search != row['time'] and results == []:
            result = None

    if not result:
        print(red_err("\nSorry, no entries took that amount of time. "
                      "Please try again."))
    else:
        display_entries(results)

    return None


def search_exact():
    """
    Search based on exact keyword
    """
    search = input("Please select desired keyword: ")
    entries = open_csv()

    results = []
    for row in entries:
        if search == row['name']:
            result = row
            results.append(row)
        elif search == row['note']:
            result = row
            results.append(row)
        elif search != row['name'] and results == []:
            result = None
        elif search != row['note'] and results == []:
            result = None

    if result:
        display_entries(results)
    else:
        print(red_err("\nSorry, no keyword found. Please try again."))

    return None


def search_pattern():
    """
    Search based on regex pattern
    """
    search = input("Please select desired regex pattern: ")
    entries = open_csv()

    search = r'' + search
    results = []
    for row in entries:
        if re.search(search, row['name']):
            result = row
            results.append(row)
        elif search == row['note']:
            result = row
            results.append(row)
        elif search != row['name'] and results == []:
            result = None
        elif search != row['note'] and results == []:
            result = None

    if result:
        display_entries(results)
    else:
        print(red_err("\nSorry, nothing found with that pattern. "
                      "Please try again."))

    return None


def show_all():
    """
    Shows all entries
    """
    entries = open_csv()
    results = []

    for row in entries:
        result = row
        results.append(result)
    display_entries(results)

    return None