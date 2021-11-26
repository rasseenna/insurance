from messageboard import MessageBoard


class Comment:

    def __init__(self):  # a method to create objects
        self.__name = ""

    def get_comment_name(self):  # get method
        return self.__name

    def set_comment_name(self,c_name):  # set method
        self.__name = c_name

    # GoF mediator pattern ------------------------------
    def send_message(self, message):
        text = MessageBoard.show_message(self.__name, message)
        return text
    # ----------------------------------------------------