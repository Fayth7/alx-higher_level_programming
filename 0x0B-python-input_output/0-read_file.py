#!/usr/bin/python3
"""
Module for reading a text file and printing it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout.

    Args:
        filename (str): The name of the text file.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')


if __name__ == "__main__":
    read_file()
