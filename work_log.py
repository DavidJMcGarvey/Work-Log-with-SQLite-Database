"""Work Log w/ Database
Main page of program where menu is activated.
User can add an entry containing: user name, task name, date, time, and
optional notes and store it in a database.
User can search the database entries by all categories listed above.

Created: 2019-03-04
Updated: 2019-03-14
Author: David McGarvey"""

import datetime
import display
import entry_functions
import search_functions

from peewee import *

db = SqliteDatabase('log_entries.db')


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


def welcome():
    """Welcome message asking user's desired task"""
    message = "Welcome, what would you like to do?"
    print(display.blue_row("="*36))
    print(message)


def start_menu():
    """Opens menu with user options"""
    active_entry = True
    display.clear_screen()
    while active_entry:
        welcome()
        print("\na) Add New Entry"
              "\nb) Search Existing Entry"
              "\nc) Quit Program\n")
        task = input("> ")
        if task.lower() == 'a':
            display.clear_screen()
            entries = {
                'user': entry_functions.entry_user(),
                'task': entry_functions.entry_task(),
                'date': entry_functions.entry_date(),
                'time': entry_functions.entry_time(),
                'note': entry_functions.entry_note(),
            }
            Entry.create(**entries)
        elif task.lower() == 'b':
            display.clear_screen()
            search_functions.search_menu()
        elif task.lower() == 'c':
            display.clear_screen()
            print("\n" + display.blue_row("*"*7) +
                  " Thanks for using the work log! "
                  + display.blue_row("*"*7)+ "\n")
            active_entry = False
        else:
            display.clear_screen()
            print(display.red_err("\nThat was not an option"))


if __name__ == '__main__':
    initialize()
    start_menu()
