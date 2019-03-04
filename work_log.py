"""Main page of program where user menu is activated"""

import os
import entry_functions
import search_functions

from peewee import *

db = SqliteDatabase('work_entries.db')


class Entry(Model):
    """a subclass of model that collects entry info"""

    def __init__(self):
        super().__init__(name=entry_functions.entry_name(),
                         date=entry_functions.entry_date(),
                         time=entry_functions.entry_time(),
                         note=entry_functions.entry_note()
                         )

    # name = entry_functions.entry_name()
    # date = entry_functions.entry_date()
    # time = entry_functions.entry_time()
    # note = entry_functions.entry_note()

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)
    db.close()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_menu():
    """
    Opens menu with user options
    """
    active_entry = True

    while active_entry:
        print("\na) Add New Entry"
              "\nb) Search Existing Entry"
              "\nc) Quit Program\n")
        task = input("> ")
        if task.lower() == 'a':
            Entry()
        elif task.lower() == 'b':
            search_functions.search_menu()
        elif task.lower() == 'c':
            print("Thanks for using the work log!")
            active_entry = False
        else:
            print("\nThat was not an option")


if __name__ == '__main__':
    initialize()
    start_menu()
