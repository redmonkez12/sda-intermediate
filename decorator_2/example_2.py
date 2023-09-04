from collections import defaultdict


#
#
# # def check_user(username):
# #     if username != "admin":
# #         raise Exception("Tento uzivatel nema pristup do zasob")
#
def check_user(username):
    print(username)

    def check_user_wrapper(func):
        print(func)

        def wrapper(*args, **kwargs):
            print(args)

            current_username = kwargs.get("username")

            if current_username is None:
                raise Exception("Missing positional parameter")

            if current_username != "admin":
                raise Exception(f"Tato akce neni povolena pro uzivatele {current_username}")

            return func(*args, **kwargs)

        return wrapper

    return check_user_wrapper


class Store:
    def __init__(self):
        self.storage = defaultdict(int)

    # @check_user("test")  # Reference na funkci
    def get_food(self, username, food):
        # check_user(username)

# command + 1
# alt + 1
# command + N
# alt + insert
# control + tab
# ctrl + tab
        return self.storage[food]

    # @check_user("admin")  # -> Volani funkce
    def get_food(self, username, food):
        # check_user(username)

        return self.storage[food]

    # @check_user("admin")
    def put_food(self, username, food):
        # check_user(username)

        self.storage[food] += 1


store = Store()

admin_checker = check_user("admin")
wrapper = admin_checker(store.put_food)

wrapper(username=" admin", food="rohlik")

# store.put_food(username="tomas12", food="rohlik")

# storage = {}
# storage = defaultdict(int)
# if "apple" not in storage:
#     storage["apple"] = 0

# storage["apple"] += 1
# print(storage)

# ctrl + shift + L
# def hello(greet):
#     def wrapper_2(ptakovina):
#         def wrapper():
#             print(greet)
#
#         return wrapper
#
#     return wrapper_2
#
# def cool_function(fn):
#     fn()
#
# greeter = hello("hello my friend")
#
#
# cool_function(greeter("dalsi parameter"))
