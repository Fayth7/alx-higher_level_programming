#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        json_dict = {}

        if attrs is None:
            attrs = self.__dict__.keys()

        for attr in attrs:
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[attr] = value

        return json_dict

    def reload_from_json(self, json):
        """Replace student attributes instance with values from dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
