"""Script to test program using a TestCase"""
import unittest
import entry_functions
import search_functions
import work_log


class EntryTests(unittest.TestCase):
    def setUp(self):
        self.entry = work_log.Entry()
        self.clear_work = work_log.clear_screen()
        self.clear_search = search_functions.clear_screen()
        self.welcome = work_log.welcome()
        self.initialize = work_log.initialize()
        self.print_entry = search_functions.print_entry(self.entry)
        self.print_entries = search_functions.print_entries([self.entry])
        self.dates = entry_functions.get_datetime(str(self.entry.date)[:-16])
        self.red_work = work_log.red_err("Test")
        self.red_entry = entry_functions.red_err("Test")
        self.red_search = search_functions.red_err("Test")
        self.blue = search_functions.blue_row("Test")

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
        self.assertIsNot(self.entry.note, self.entry.user)

    def test_note_not_task(self):
        self.assertIsNot(self.entry.note, self.entry.task)

    def test_note_not_date(self):
        self.assertIsNone(self.entry.note, self.entry.date)

    def test_note_not_time(self):
        self.assertIsNot(self.entry.note, self.entry.time)

    def test_clear_screen_work_log(self):
        self.assertEqual(self.clear_work, work_log.clear_screen())

    def test_clear_screen_search_functions(self):
        self.assertEqual(self.clear_search, search_functions.clear_screen())

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

    def test_red_work(self):
        self.assertEqual(self.red_work, work_log.red_err("Test"))

    def test_red_entry(self):
        self.assertEqual(self.red_entry, entry_functions.red_err("Test"))

    def test_red_search(self):
        self.assertEqual(self.red_search, search_functions.red_err("Test"))

    def test_blue(self):
        self.assertEqual(self.blue, search_functions.blue_row("Test"))


if __name__ == '__main__':
    unittest.main()
