#!/usr/bin/python3
"""
Module for append_after method.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text after each line containing specific string in a file.
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Move the file pointer to the beginning

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()
