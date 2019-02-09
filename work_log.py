import csv
import datetime
import re


def welcome():
    """
    Asks for their name to be repeated back to them in a personalized welcome
    """
    name = input("Welcome to work. What is your name? ")
    print("Hello, {}. Please choose a task: ".format(name))
    start_menu()


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
            add_entry()
        elif task.lower() == 'b':
            search_menu()
        elif task.lower() == 'c':
            print("Thanks for using the work log!")
            break
        else:
            print(red_err("That was not an option"))


def write_csv(entry):
    """
    Writes work log input to a csv file
    """
    with open('log.csv', 'a') as csvfile:
        entry_info = ['name', 'date', 'time', 'note']
        log_writer = csv.DictWriter(csvfile, fieldnames=entry_info)
        
        log_writer.writerow({
            'name': entry[0],
            'date': entry[1],
            'time': entry[2],
            'note': entry[3],
        })


def open_csv():
    """
    Pulls entries from CSV and returns a list of entries
    """
    with open('log.csv', 'r') as csvfile:
        entry_info = ['name', 'date', 'time', 'note']
        log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
        entries = list(log_reader)
        return entries


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


def entry_name():
    """
    Returns a task name and doesn't allow for empty
    """
    while True:
        entry_name = input("What is the title of the task? ")
        if entry_name == '':
            print(red_err("Please try again with a task name"))
        else:
            return entry_name


def entry_date():
    """
    Ask user for their desired date and if date does not match format an error is raised asking them to try again
    """
    fmt = '%Y-%m-%d'
    while True:
        try:
            date = input("What date was the task completed? Please use YYYY-MM-DD format. ")
            return datetime.datetime.strptime(date, fmt)
        except ValueError:
            print(red_err("Please try again using proper format"))


def entry_time():
    """
    Ask user for the time in minutes that their task took, sending back an error message if input is not an integer
    """
    while True:
        try:
            time = abs(int(input("How many minutes did the task take? ")))
            return time
        except ValueError:
            print(red_err("Please try again using an integer to represent minutes spent on task."))


def entry_note():
    new_note = []
    entry_notes = input("Would you like to add any additional notes? (optional) ")
    if entry_notes != '':
        new_note.append(entry_notes)
    else:
        new_note.append('')
    return new_note


def get_datetime(date):
    """
    Returns user given date as a datetime object
    """
    fmt = '%Y-%m-%d'
    return datetime.datetime.strptime(date, fmt)


def add_entry():
    """
    Takes user input from entry functions, put in list to be be written to CSV upon log completion
    """
    new_entry = [entry_name(), entry_date(), entry_time(), entry_note()]

    write_csv(new_entry)
    
    return None


def display_entries(rows):
    """
    Allows for multiple entries to be printed at once
    """
    for row in rows:
        display_entry(row)


def display_entry(row):
    """
    Prints entry in uniform format
    """
    print("\n" + blue_row("Task name: " + row['name']))
    print(blue_row("Task date: " + row['date'][:-9]))
    print(blue_row("Task minutes: " + row['time']))
    print(blue_row("Task notes: " + row['note']) + "\n")


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
    entries = open_csv()
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
        print(red_err("\nSorry, no entries took that amount of time. Please try again."))
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
        print(red_err("\nSorry, nothing found with that pattern. Please try again."))

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


if __name__ == '__main__':
    welcome()
