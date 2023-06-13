#!/usr/bin/python3
"""
    Module for class Student.
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        json_dict = {}

        # Iterate over the public instance attributes
        for attr, value in self.__dict__.items():
            # Exclude private and special attributes
            if not attr.startswith("__"):
                # Check if the attribute value is of a serializable type
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[attr] = value

        return json_dict
