"""A class that creates a user's work log entry"""
import entry_functions
from peewee import *


db = SqliteDatabase('entry_log.db')


class Entry(Model):
    name = entry_functions.entry_name()
    date = entry_functions.entry_date()
    time = entry_functions.entry_time()
    note = entry_functions.entry_note()

    class Meta:
        database = db


db.connect()
db.create_tables([Entry], safe=True)
