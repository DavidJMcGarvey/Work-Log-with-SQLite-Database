"""Main page of program where user menu is activated"""
import os
import datetime
import entry_functions
import search_functions

from peewee import *

db = SqliteDatabase('log_entries.db')


def red_err(message):
    """Return error message with red font """
    return "\33[91m" + message + "\33[0m"


class Entry(Model):
    """a subclass of Model that collects entry info"""
    user = CharField(max_length=180)
    task = CharField(max_length=180)
    date = DateTimeField(default=datetime.datetime.now)
    time = IntegerField(default=0)
    note = TextField()

    class Meta:
        database = db


def initialize():
    """Opens connection to database, creates table, and closes"""
    db.connect()
    db.create_tables([Entry], safe=True)
    db.close()


def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    """Welcome message asking user's desired task"""
    message = "Welcome, what would you like to do?"
    print(search_functions.blue_row("="*len(message)))
    print(message)


def start_menu():
    """Opens menu with user options"""
    active_entry = True

    while active_entry:
        clear_screen()
        welcome()
        print("\na) Add New Entry"
              "\nb) Search Existing Entry"
              "\nc) Quit Program\n")
        task = input("> ")
        if task.lower() == 'a':
            clear_screen()
            entries = {
                'user': entry_functions.entry_user(),
                'task': entry_functions.entry_name(),
                'date': entry_functions.entry_date(),
                'time': entry_functions.entry_time(),
                'note': entry_functions.entry_note(),
            }
            Entry.create(**entries)
        elif task.lower() == 'b':
            clear_screen()
            search_functions.search_menu()
        elif task.lower() == 'c':
            clear_screen()
            print("Thanks for using the work log!")
            active_entry = False
        else:
            print(red_err("\nThat was not an option"))


if __name__ == '__main__':
    initialize()
    start_menu()
