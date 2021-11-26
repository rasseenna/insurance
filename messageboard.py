""" This is an entity, MessageBoard"""
import datetime


# GoF mediator pattern ------------------------------
class MessageBoard(object):  # a static class

    @staticmethod
    def show_message(name, content):  # a static method
        now = datetime.datetime.now()
        # message = now.strftime("%Y-%m-%d %H:%M:%S") + " from " + name + ": " + content
        message = "Smart Insurance System Welcomes you !!!!! " + name + ": " + content
        print("Welcome message: " + message)
        return message