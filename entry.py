"""Entry class and database creation"""
import entry_functions
from peewee import *

db = SqliteDatabase('entry_log.db')


class Entry(Model):
    # import pdb; pdb.set_trace()
    """A subclass of model that takes entry info and stores in a database"""

    def __init__(self):
        super().__init__(name=entry_functions.entry_name(),
                         date=entry_functions.entry_date(),
                         time=entry_functions.entry_time(),
                         note=entry_functions.entry_note()
                         )

    def store_entry(self):
        entries = [
            {'name': self.name,
             'date': self.date,
             'time': self.time,
             'note': self.note},
        ]
        return entries

    class Meta:
        database = db


db.connect()
db.create_tables([Entry], safe=True)
db.close()

