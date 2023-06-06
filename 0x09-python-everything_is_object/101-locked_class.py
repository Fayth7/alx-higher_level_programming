#!/usr/bin/python3
""" prevents the user from dynamically creating new instance attributes"""

class LockedClass:
    __slots__ = ["first_name"]
