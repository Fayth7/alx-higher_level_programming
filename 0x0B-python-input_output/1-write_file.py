#!/usr/bin/python3
"""
Module for writing a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to text file & returns number of characters written.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters = write_file(
        "my_first_file.txt",
        "This School is so cool!/n"
    )
    print(nb_characters)
