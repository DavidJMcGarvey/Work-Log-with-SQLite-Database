"""Script to test program using a TestCase"""
import unittest
import entry_functions
import search_functions
import work_log


class EntryTests(unittest.TestCase):
    def setUp(self):
        self.entry = work_log.Entry()

    def test_create_unique(self):
        self.assertNotEqual(self.entry, work_log.Entry())

    def test_create_user(self):
        user = entry_functions.entry_user()
        self.assertNotEqual(self.entry.user, user)

    def test_create_task(self):
        task = entry_functions.entry_task()
        self.assertNotEqual(self.entry.task, task)

    def test_create_date(self):
        date = entry_functions.entry_date()
        self.assertNotEqual(self.entry.date, date)

    def test_create_time(self):
        time = entry_functions.entry_time()
        self.assertNotEqual(self.entry.time, time)

    def test_create_note(self):
        note = entry_functions.entry_note()
        self.assertNotEqual(self.entry.note, note)

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


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.search = work_log.Entry.select()

    def test_search(self):
        self.assertIn(work_log.Entry(), self.search)

    def test_employee_search(self):
        user = search_functions.search_employee()
        self.assertNotIn(self.search, user)

    def test_date_search(self):
        date = search_functions.search_date()
        self.assertNotIn(self.search, date)


if __name__ == '__main__':
    unittest.main()

