"""Functions used to create an Entry class"""
import datetime


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
    entry_notes = input("Would you like to add any additional notes? (optional) ")
    if entry_notes != '':
        new_note = entry_notes
    else:
        new_note = '(No notes)'
    return new_note


def get_datetime(date):
    """
    Returns user given date as a datetime object
    """
    fmt = '%Y-%m-%d'
    return datetime.datetime.strptime(date, fmt)

