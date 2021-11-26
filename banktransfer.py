""" This is the entity, BankTransfer"""
from paymentmethod import PaymentMethod


#  GoF bridge pattern interface -------------------
class BankTransfer(PaymentMethod):

    def __init__(self, contract, api):
        super().__init__(api)
        self.__payment_api = api
        self.__contract = contract

    def pay_out(self):
        return self.__payment_api.pay(self.__contract)
