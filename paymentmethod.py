""" This is the interface, PaymentAPI"""


#  GoF bridge pattern interface -------------------
class PaymentMethod:

    def __init__(self, api):
        #  GoF bridge pattern interface -------------------
        self._payment_api = api

    def pay_out(self):
        pass
