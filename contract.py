""" This is the entity, Contract"""


class Contract:

    def __init__(self):  # a method to create objects
        self.__username = ""  # private attribute
        self.__pay = 0.0  # private attribute

    def get_username(self):  # get method
        return self.__username

    def set_username(self, name):  # set method
        self.__username = name

    def get_pay(self):  # get method
        return self.__pay

    def set_pay(self, amount):  # set method
        self.__pay = amount





