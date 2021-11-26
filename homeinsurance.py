from datetime import date
from contract import Contract


class HomeInsurance:

    def __init__(self):  # a method to create objects
        self.__username = ""
        self.__policyname = ""
        self.__address = ""
        self.__builtdate = ""
        self.__hometype = ""
        self.__homeage = ""
        self.__membershiptype = ""
        self.__premiumselected = ""
        self.__contract = Contract()

    def get_user_name(self):  # get method
        return self.__username

    def set_user_name(self, name):  # set method
        self.__username = name

    def get_policy_name(self):  # get method
        return self.__policyname

    def set_policy_name(self, policy):  # set method
        self.__policyname = policy

    def get_address(self):  # get method
        return self.__address

    def set_address(self, address):  # set method
        self.__address = address

    def get_built_date(self):  # get method
        return self.__builtdate

    def set_built_date(self, built):  # set method
        self.__builtdate = built

    def get_home_type(self):  # get method
        return self.__hometype

    def set_home_type(self, type):  # set method
        self.__hometype = type

    def get_home_age(self):  # get method
        return self.__homeage

    def set_home_age(self, age):  # set method
        self.__homeage = age

    def get_membership_type(self):  # get method
        return self.__membershiptype

    def set_membership_type(self, memtype):  # set method
        self.__membershiptype = memtype

    def get_premium_selected(self):  # get method
        return self.__premiumselected

    def set_premium_selected(self, premium):  # set method
        self.__premiumselected = premium

    def get_house_years(self):
        built_year = int(self.__homeage)
        today_year = date.today().year
        year = today_year - built_year
        return year

    def get_contract(self):  # get method
        return self.__contract

    def set_contract(self, pay):  # composition
        self.__contract.set_username(self.__username)
        self.__contract.set_pay(pay)

