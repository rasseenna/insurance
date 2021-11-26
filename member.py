from user import User


class Member(User):

    def __init__(self):
        super().__init__()
        self.__info = "Welcome New User"  # default company location

    def get_info(self):
        return self.__info

    def set_remote(self, content):
        self.__info = content

    def get_total_pay(self):
        pass
