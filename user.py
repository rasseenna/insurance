""" This is the entity, Staff"""


class User:

    def __init__(self):  # a method to create objects
        self.__username = ""
        self.__email = ""
        self.__password = ""
        self.__phone = ""
        self.__subordinates = []  # GoF composite pattern

    def get_user_name(self):  # get method
        return self.__username

    def set_user_name(self, name):  # set method
        self.__username = name

    def get_email(self):  # get method
        return self.__email

    def set_email(self, mail):  # set method
        self.__email = mail

    def get_pass_word(self):  # get method
        return self.__password

    def set_pass_word(self, pswd):  # set method
        self.__password = pswd

    def get_mobile_number(self):  # get method
        return self.__phone

    def set_mobile_number(self, mobile):  # set method
        self.__phone = mobile
        
    # GoF composite pattern ------------------------------
    def add_subordinate(self, people):
        self.__subordinates.append(people)

    def remove_subordinate(self, people):
        self.__subordinates.remove(people)

    def get_subordinates(self,):
        return self.__subordinates

    def get_subordinate_names(self):
        names = ""
        for person in self.__subordinates:
            names = names + " " + person.get_user_name()
        return names
    # ----------------------------------------------------


