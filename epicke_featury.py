# namedtuple
# tuple

# container

# je to odlehcena trida
#
# from collections import namedtuple
#
# User = namedtuple("User", "first_name last_name age password birthday")
#
# user = User("Tomas", "Svojanovsky", 10, "123456", "1991-01-01")
# user.name = "Jozka"


# def register(first_name, last_name, age, password, birthday):
# def register(user: User):
#     pass

# bez namedtuple

# from __future__ import annotations


# class User:
#     def __init__(self, first_name, last_name, age, password, birthday):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.password = password
#         self.birthday = birthday
#
#     def __repr__(self):
#         return f"Krasny a vonavy vystup {self.first_name}"
#
#     def __eq__(self, other: User):
#         return self.first_name == other.first_name
#
#
# user_1 = User("Tomas", "Svojanovsky", 10, "123456", "1991-01-01")
# user_2 = User("Tomas", "Svojanovsky", 10, "123456", "1991-01-01")
# print(user_1 == user_2)

# dataclass

# from dataclasses import dataclass

# @dataclass
# class User:
#     first_name: str
#     last_name: str
#     age: int
#     password: str
#     birthday: str  # 1991-01-01Z00:00:00T+01:01
#
#
# user_1 = User("Tomas", "Svojanovsky", 10, "123456", "1991-01-01")
# user_2 = User("Tomas", "Svojanovsky", 11, "123456", "1991-01-01")
# print(user_1 == user_2)

# user = User()
# user.map_to_user()

class User:
    def __init__(self, first_name, last_name, age, password, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        self.birthday = birthday

    @classmethod
    def user_from_dict(cls, user_dict):
        # first_name = user_dict["first_name"]

        return cls(
            user_dict["first_name"],
            user_dict["last_name"],
            user_dict["age"],
            user_dict["password"],
            user_dict["birthday"],
        )


data = {
    "first_name": "Tomas",
    "last_name": "Opicak",
    "age": 10,
    "password": "123456",
    "birthday": "100-01-10",
}

new_user = User.user_from_dict(data)
# print(new_user.__dict__)

# user = User(data["first_name"]...)

from datetime import datetime

class Task:
    @staticmethod
    def get_timestamp():
        now = datetime.now()
        return now.strftime("%")


print(Task.get_timestamp())
