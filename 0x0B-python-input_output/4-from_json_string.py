#!/usr/bin/python3
"""
Module for returning an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)


if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {
        "is_active": true,
        "info": {
            "age": 36,
            "average": 3.14
        },
        "id": 12,
        "name": "John",
        "places": ["San Francisco", "Tokyo"]
    }
    """

    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

    try:
        s_my_dict = """
        {"is_active": true, 12 }
        """
        my_dict = from_json_string(s_my_dict)
        print(my_dict)
        print(type(my_dict))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
