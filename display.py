"""Functions add color formatting to terminal outputs amd clears screen"""
import os


def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def blue_row(message):
    """To entries, adds a white font against blue background :)"""
    return "\33[37m\33[44m" + message + "\33[0m"


def red_err(message):
    """Return error message with red font"""
    return "\33[91m" + message + "\33[0m"


