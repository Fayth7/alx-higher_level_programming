#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """
    Base class for managing id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
        id (int, optional): If provided, assign this value to the id attribute.
        Otherwise, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
