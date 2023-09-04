# # age = None
# #
# # while age is None:
# #     try:
# #         user_input = input("Your age:")
# #         age = int(user_input)
# #         raise Exception("Yaaay")  # Try uncommented this
# #     except ValueError:
# #         print("Please provide a valid number")
# #     except Exception:
# #         print("Ooops something really bad happened")
# #
# # print(age)
# #
#
# from __future__ import annotations
#
#
# class Todo:
#     def __init__(self, title: str, description: str, severity: str) -> None:
#         self.title = title
#         self.description = description
#         self.severity = severity
#         self._status = "created"
#
#     @classmethod
#     def todo_from_dict(cls, todo_dict: dict[str, str]) -> Todo:
#         title = todo_dict["title"]
#
#         desc = todo_dict["description"]
#         severity = todo_dict["severity"]
#         todo_obj = cls(title, desc, severity)
#         return todo_obj
#
#
# data = {"title": "Pets", "severity": 3, "description": "Walk a dog"}
#
# Todo.todo_from_dict(data)
#
#
#
#

import time


def timer(data: list[str]) -> tuple[float, str]:
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()

        yield delta, item


for data_with_time in timer(["todo_1", "todo_2", "todo_3"]):
    print(data_with_time)
    time.sleep(2)

# (0.0, 'todo_1')
# (2.0037454579724, 'todo_2')
# (2.004600666987244, 'todo_3'





