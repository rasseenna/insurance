

class MotorInsurance:

    def __init__(self):  # a method to create objects
        self.__username = ""
        self.__policyname = ""
        self.__manufacturer = ""
        self.__model = ""
        self.__colour = ""
        self.__registrationyear = ""
        self.__registrationnumber = ""
        self.__premiumselected = ""

    def get_user_name(self):  # get method
        return self.__username

    def set_user_name(self, name):  # set method
        self.__username = name

    def get_policy_name(self):  # get method
        return self.__policyname

    def set_policy_name(self, policy):  # set method
        self.__policyname = policy

    def get_manufacturer(self):  # get method
        return self.__manufacturer

    def set_manufacturer(self, manufacturer):  # set method
        self.__manufacturer = manufacturer

    def get_model(self):  # get method
        return self.__model

    def set_model(self, model):  # set method
        self.__model = model

    def get_colour(self):  # get method
        return self.__colour

    def set_colour (self, colour):  # set method
        self.__colour = colour

    def get_registration_year(self):  # get method
        return self.__registrationyear

    def set_registration_year (self, ryear):  # set method
        self.__registrationyear = ryear

    def get_registration_number(self):  # get method
            return self.__registrationnumber

    def set_registration_number(self, rnum):  # set method
            self.__registrationnumber = rnum

    def get_premium_selected(self):  # get method
        return self.__premiumselected

    def set_premium_selected(self, premium):  # set method
        self.__premiumselected = premium