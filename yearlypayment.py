""" This is the interface, MonthlyPayment"""
from paymentapi import PaymentAPI


#  GoF bridge pattern interface -------------------
class YearlyPayment(PaymentAPI):

    def pay(self, total):
        total_pay = (total - (total * .07))
        return total_pay
