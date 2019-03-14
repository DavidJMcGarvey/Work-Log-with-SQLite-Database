"""Functions used to create an Entry class"""
import datetime
import display


def entry_user():
    """Continuous prompt, returns user name and rejects empty string"""
    print("Hello, valued employee.")
    while True:
        username = input("What is your name? ")
        if username == '':
            print(display.red_err("Please try again."))
        else:
            return username


def entry_task():
    """Continuous prompt, returns a task name and rejects empty string"""
    while True:
        task_name = input("What is the title of the task? ")
        if task_name == '':
            print(display.red_err("Please try again with a task name"))
        else:
            return task_name


def entry_date():
    """Continuous prompt, returns datetime and rejects non-datetime object"""
    fmt = '%Y-%m-%d'
    while True:
        try:
            date = input("What date was the task completed? Please use "
                         "YYYY-MM-DD format. ")
            return datetime.datetime.strptime(date, fmt)
        except ValueError:
            print(display.red_err("Please try again using proper format"))


def entry_time():
    """Continuous prompt, returns a time and rejects non-integer"""
    while True:
        try:
            time = abs(int(input("How many minutes did the task take? ")))
            return time
        except ValueError:
            print(display.red_err("Please try again using an integer to "
                                  "represent minutes spent on task."))


def entry_note():
    """Continuous prompt, returns note and adds '(No Notes)' if empty string"""
    entry_notes = input("Would you like to add any additional notes? "
                        "(optional) ")
    if entry_notes != '':
        new_note = entry_notes
    else:
        new_note = '(No notes)'
    return new_note


def get_datetime(date):
    """Returns user given date as a datetime object"""
    fmt = '%Y-%m-%d'
    return datetime.datetime.strptime(date, fmt)
