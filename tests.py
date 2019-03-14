"""Script to test program using a TestCase"""
import datetime
import display
import unittest
import entry_functions
import search_functions
import work_log

from unittest import mock


class EntryTests(unittest.TestCase):
    def setUp(self):
        self.entry = work_log.Entry()
        self.clear_work = display.clear_screen()
        self.welcome = work_log.welcome()
        self.initialize = work_log.initialize()
        self.print_entry = search_functions.print_entry(self.entry)
        self.print_entries = search_functions.print_entries([self.entry])
        self.dates = entry_functions.get_datetime(str(self.entry.date)[:-16])
        self.red = display.red_err("Test")
        self.blue = display.blue_row("Test")

    def test_create_unique(self):
        self.assertNotEqual(self.entry, work_log.Entry())

    def test_user(self):
        self.assertIn(self.entry.user, work_log.Entry.user)

    def test_user_not_task(self):
        self.assertIsNone(self.entry.user, self.entry.task)

    def test_user_not_date(self):
        self.assertIsNone(self.entry.user, self.entry.date)

    def test_user_not_time(self):
        self.assertIsNone(self.entry.user, self.entry.time)

    def test_user_not_note(self):
        self.assertIsNone(self.entry.user, self.entry.note)

    def test_task(self):
        self.assertIn(self.entry.task, work_log.Entry.task)

    def test_task_not_user(self):
        self.assertIsNone(self.entry.task, self.entry.user)

    def test_task_not_date(self):
        self.assertIsNone(self.entry.task, self.entry.date)

    def test_task_not_time(self):
        self.assertIsNone(self.entry.task, self.entry.time)

    def test_task_not_note(self):
        self.assertIsNone(self.entry.task, self.entry.note)

    def test_date(self):
        self.assertIn(self.entry.date, work_log.Entry.date)

    def test_date_not_user(self):
        self.assertIsNot(self.entry.date, self.entry.user)

    def test_date_not_task(self):
        self.assertIsNot(self.entry.date, self.entry.task)

    def test_date_not_time(self):
        self.assertIsNot(self.entry.date, self.entry.time)

    def test_date_not_note(self):
        self.assertIsNot(self.entry.date, self.entry.note)

    def test_time(self):
        self.assertIn(self.entry.time, work_log.Entry.time)

    def test_time_not_user(self):
        self.assertIsNot(self.entry.time, self.entry.user)

    def test_time_not_date(self):
        self.assertIsNot(self.entry.time, self.entry.date)

    def test_time_not_note(self):
        self.assertIsNot(self.entry.time, self.entry.note)

    def test_note(self):
        self.assertIn(self.entry.note, work_log.Entry.note)

    def test_note_not_user(self):
        self.assertIsNone(self.entry.note, self.entry.user)

    def test_note_not_task(self):
        self.assertIsNone(self.entry.note, self.entry.task)

    def test_note_not_date(self):
        self.assertIsNone(self.entry.note, self.entry.date)

    def test_note_not_time(self):
        self.assertIsNot(self.entry.note, self.entry.time)

    def test_clear_screen(self):
        self.assertEqual(self.clear_work, display.clear_screen())

    def test_welcome(self):
        self.assertIs(self.welcome, work_log.welcome())

    def test_initialize(self):
        self.assertIs(self.initialize, work_log.initialize())

    def test_print_entry(self):
        self.assertIs(self.print_entry, search_functions.print_entry(
            self.entry))

    def test_print_entry_not_entries(self):
        self.assertIsNone(self.print_entry, self.print_entries)

    def test_print_entries(self):
        self.assertIs(self.print_entries, search_functions.print_entries(
            [self.entry]))

    def test_dates(self):
        self.assertIsNot(self.dates, entry_functions.get_datetime(
            str(self.entry.date)[:-16]))

    def test_red(self):
        self.assertEqual(self.red, display.red_err("Test"))

    def test_blue(self):
        self.assertEqual(self.blue, display.blue_row("Test"))


class InputTests(unittest.TestCase):
    def setUp(self):
        self.entry = work_log.Entry()

    @mock.patch('builtins.input', side_effect=['[self.entry]'])
    def test_list_entries(self, mock_input):
        result = search_functions.list_entries([self.entry])
        self.assertNotEqual(result, '[self.entry]')

    @mock.patch('builtins.input', side_effect=['Q'])
    def test_list_search(self, mock_input):
        result = search_functions.list_search([self.entry])
        self.assertNotEqual(result, "Please try again with a task name")

    @mock.patch('builtins.input', side_effect=['Jeanie'])
    def test_entry_user(self, mock_input):
        result = entry_functions.entry_user()
        self.assertEqual(result, 'Jeanie')

    @mock.patch('builtins.input', side_effect=['Python'])
    def test_entry_task(self, mock_input):
        result = entry_functions.entry_task()
        self.assertEqual(result, 'Python')

    @mock.patch('builtins.input', side_effect=['2011-01-01'])
    def test_entry_date(self, mock_input):
        result = entry_functions.entry_date()
        self.assertEqual(result, datetime.datetime(2011, 1, 1, 0, 0))

    @mock.patch('builtins.input', side_effect=['(No Notes)'])
    def test_entry_note(self, mock_input):
        result = entry_functions.entry_note()
        self.assertEqual(result, '(No Notes)')

    @mock.patch('builtins.input', side_effect=['12'])
    def test_search_time(self, mock_input):
        result = search_functions.search_time()
        self.assertNotEqual(result, '12')

    @mock.patch('builtins.input', side_effect=['python'])
    def test_search_exact(self, mock_input):
        result = search_functions.search_exact()
        self.assertNotEqual(result, 'python')


if __name__ == '__main__':
    unittest.main()
