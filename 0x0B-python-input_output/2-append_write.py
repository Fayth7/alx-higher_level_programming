#!/usr/bin/python3
"""
Module for appending a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write(
        "file_append.txt",
        "This School is so cool!\n"
    )
    print(nb_characters_added)
