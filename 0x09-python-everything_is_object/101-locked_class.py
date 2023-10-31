#!/usr/bin/python3

class LockedClass:
    """This class represents a lockedclass"""
    def __init__(self, user_name):

        specified_name = "first_name"

        if user_name != specified_name:
            raise AttributeError("object has no attribute 'last_name'")
        self.__user_name = user_name
