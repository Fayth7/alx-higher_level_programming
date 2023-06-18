#!/usr/bin/python3
"""Defines unittests for base.py."""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class BaseTestCase(unittest.TestCase):

    def test_id_increment(self):
        # Create multiple instances of Base
        base1 = Base()
        base2 = Base()
        base3 = Base()

        # Check if the IDs are incremented correctly
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_custom_id(self):
        # Create an instance of Base with a custom ID
        base = Base(100)

        # Check if the custom ID is set correctly
        self.assertEqual(base.id, 100)

    def test_to_json_string(self):
        # Create an instance of Base
        base = Base(10)

        # Convert the instance to a JSON string
        json_string = Base.to_json_string([base.to_dictionary()])

        # Check if the JSON string is valid
        self.assertIsInstance(json_string, str)
        self.assertEqual(json_string, '[{"id": 10}]')

    def test_from_json_string(self):
        # Define a JSON string
        json_string = '[{"id": 5}, {"id": 6}, {"id": 7}]'

        # Convert the JSON string to a list of instances
        instances = Base.from_json_string(json_string)

        # Check if the instances are created correctly
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 3)
        self.assertEqual(instances[0].id, 5)
        self.assertEqual(instances[1].id, 6)
        self.assertEqual(instances[2].id, 7)

if __name__ == '__main__':
    unittest.main()
    
class TestBase(unittest.TestCase):
    """Unittests for Base class."""

    def test_id_increment(self):
        """Test that each instance of Base has a unique ID incremented correctly."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test that Base instances can be created with custom IDs."""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_negative_id(self):
        """Test that Base instances can handle negative IDs."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_zero_id(self):
        """Test that Base instances can handle zero as an ID."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_str_id(self):
        """Test that Base instances can handle string IDs."""
        b = Base("abc")
        self.assertEqual(b.id, "abc")

    def test_float_id(self):
        """Test that Base instances can handle float IDs."""
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

    def test_list_id(self):
        """Test that Base instances can handle list IDs."""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_dict_id(self):
        """Test that Base instances can handle dictionary IDs."""
        b = Base({"a": 1, "b": 2})
        self.assertEqual(b.id, {"a": 1, "b": 2})

    def test_none_id(self):
        """Test that Base instances can handle None as an ID."""
        b = Base(None)
        self.assertEqual(b.id, None)

    def test_unique_ids(self):
        """Test that Base instances have unique IDs even with custom IDs."""
        b1 = Base(10)
        b2 = Base()
        b3 = Base(20)
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b2.id, b3.id)

    def test_private_nb_instances(self):
        """Test that the __nb_instances attribute is private."""
        with self.assertRaises(AttributeError):
            print(Base.__nb_instances)

    def test_to_json_string(self):
        """Test the to_json_string method of Base class."""
        b = Base(10)
        json_string = b.to_json_string()
        self.assertEqual(json_string, '{"id": 10}')

    def test_from_json_string(self):
        """Test the from_json_string method of Base class."""
        json_string = '{"id": 10}'
        b = Base.from_json_string(json_string)
        self.assertEqual(b.id, 10)

if __name__ == '__main__':
    unittest.main()
