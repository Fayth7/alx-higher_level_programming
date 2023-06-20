#!/usr/bin/python3
"""Defines a base model class."""


import json
import csv


class Base:
    """
    Base class for managing id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
            id (int, optional): If provided, assign the value to id attribute.
                Otherwise, increment __nb_objects and assign new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by json_string.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return [
            cls.create(**dictionary)
            for dictionary in cls.from_json_string(json_string)
        ]

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None.
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )

        with open(filename, "w") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
        **dictionary: Double pointer to a dictionary.

        Returns:
        Instance with attributes set.
        """
        if dictionary is None or len(dictionary) == 0:
            dummy = cls()
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [
                    cls.create(**dictionary)
                    for dictionary in dictionaries
                ]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes and saves instances to a CSV file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from a CSV file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    dictionary = cls.from_csv_row(row)
                    instance = cls.create(**dictionary)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    def to_dictionary(self):
        """
        Returns the dictionary representation of the instance.

        Returns:
        dict: Dictionary representation of the instance.
        """
        return {
            'id': self.id,
        }

    def update(self, *args, **kwargs):
        """
        Updates the instance attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None.
        """
        if args and len(args) != 0:
            attr_names = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attr_names, args):
                setattr(self, attr, value)
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_csv_row(self):
        """
        Returns the CSV row representation of the instance.

        Returns:
        list: CSV row representation of the instance.
        """
        return [self.id, self.width, self.height, self.x, self.y]

    def from_csv_row(row):
        """
        Returns the dictionary representation of a CSV row.

        Args:
            row (list): CSV row.

        Returns:
            dict: Dictionary representation of the CSV row.
        """
        raise NotImplementedError(
            "The from_csv_row() method must be implemented."
        )
