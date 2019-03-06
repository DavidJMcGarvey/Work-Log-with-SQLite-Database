"""Main page of program where user menu is activated"""

import os
import entry_functions
import search_functions

from peewee import *

db = SqliteDatabase('work_entries.db')


def red_err(message):
    """Return error message with red font """
    return "\33[91m" + message + "\33[0m"


class Entry(Model):
    """a subclass of Model that collects entry info"""
    user = CharField()
    task = CharField()
    date = DateTimeField()
    time = IntegerField()
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
    print("="*len(message))
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
            initialize()
        elif task.lower() == 'b':
            clear_screen()
            search_functions.search_menu()
        elif task.lower() == 'c':
            clear_screen()
            print("Thanks for using the work log!")
            active_entry = False
        else:
            print("\nThat was not an option")


if __name__ == '__main__':
    start_menu()
