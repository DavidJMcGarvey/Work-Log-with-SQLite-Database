"""A class that creates a user's work log entry"""
import entry_functions


class Entry:
    def __init__(self):
        self.name = entry_functions.entry_name()
        self.date = entry_functions.entry_date()
        self.time = entry_functions.entry_time()
        self.note = entry_functions.entry_note()

    # def entry_name(self):
    #     """
    #     Returns a task name and doesn't allow for empty
    #     """
    #     while True:
    #         self.name = input("What is the title of the task? ")
    #         if self.name == '':
    #             print("Please try again with a task name")
    #         else:
    #             return self.name
    #
    # def entry_date(self):
    #     """
    #     Ask user for their desired date and if date does not match format an error is raised asking them to try again
    #     """
    #     fmt = '%Y-%m-%d'
    #     while True:
    #         try:
    #             self.date = input(
    #                 "What date was the task completed? Please use YYYY-MM-DD format. ")
    #             return datetime.datetime.strptime(date, fmt)
    #         except ValueError:
    #             print("Please try again using proper format")
    #
    # def entry_time():
    #     """
    #     Ask user for the time in minutes that their task took, sending back an error message if input is not an integer
    #     """
    #     while True:
    #         try:
    #             time = abs(int(input("How many minutes did the task take? ")))
    #             return time
    #         except ValueError:
    #             print(red_err(
    #                 "Please try again using an integer to represent minutes spent on task."))
    #
    # def entry_note():
    #     entry_notes = input(
    #         "Would you like to add any additional notes? (optional) ")
    #     if entry_notes != '':
    #         new_note = entry_notes
    #     else:
    #         new_note = '(No notes)'
    #     return new_note
