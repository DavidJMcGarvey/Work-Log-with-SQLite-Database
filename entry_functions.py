"""Functions used to create an Entry class"""
import datetime


def red_err(message):
    """Return error message with red font"""
    return "\33[91m" + message + "\33[0m"


def entry_user():
    """Returns user name and doesn't allow for empty string"""
    print("Hello, valued employee.")
    while True:
        username = input("What is your name? ")
        if username == '':
            print(red_err("Please try again."))
        else:
            return username


def entry_task():
    """Returns a task name and doesn't allow for empty string"""
    while True:
        task_name = input("What is the title of the task? ")
        if task_name == '':
            print(red_err("Please try again with a task name"))
        else:
            return task_name


def entry_date():
    """User input date, if does not match datetime, raise error"""
    fmt = '%Y-%m-%d'
    while True:
        try:
            date = input("What date was the task completed? Please use "
                         "YYYY-MM-DD format. ")
            return datetime.datetime.strptime(date, fmt)
        except ValueError:
            print(red_err("Please try again using proper format"))


def entry_time():
    """User input minutes, if not an integer, raise error"""
    while True:
        try:
            time = abs(int(input("How many minutes did the task take? ")))
            return time
        except ValueError:
            print(red_err("Please try again using an integer to represent "
                          "minutes spent on task."))


def entry_note():
    """User input optional notes"""
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()

