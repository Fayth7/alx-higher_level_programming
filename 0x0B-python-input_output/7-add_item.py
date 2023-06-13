#!/usr/bin/python3
"""
Script to add arguments to a Python list and save them to a file.
"""
import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Create an empty list or load existing list from file
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
