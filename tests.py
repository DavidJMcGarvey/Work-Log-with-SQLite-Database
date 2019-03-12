"""Script to test program using a TestCase"""
import unittest

import work_log


class EntryTests(unittest.TestCase):
    def setUp(self):
        self.entry = work_log.Entry()

    def test_user(self):
        self.assertIn(self.entry.user, work_log.Entry.user)

    def test_task(self):
        self.assertIn(self.entry.task, work_log.Entry.task)

    def test_date(self):
        self.assertIn(self.entry.date, work_log.Entry.date)

    def test_time(self):
        self.assertIn(self.entry.time, work_log.Entry.time)

    def test_note(self):
        self.assertIn(self.entry.note, work_log.Entry.note)
