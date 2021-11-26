""" CommentService to CommentAPI"""
import requests


class CommentService:
    @staticmethod
    def get_comments():
        response = requests.get('http://localhost:5001')
        comments = response.json()
        return comments

    @staticmethod
    def get_comment(key):
        response = requests.request(method="GET", url='http://localhost:5001/' + key)
        comment = response.json()
        return comment