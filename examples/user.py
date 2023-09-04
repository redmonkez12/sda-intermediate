# Co je to trida?
# Trida je predpis, plan (blueprint)

class User:
    def __init__(self, name: str, age: int) -> None:  # initializer
        self.name = name
        self.age = age
        print(f"Toto je objekt {self}, adresa v pameti: {id(self)}")

    def __new__(cls, *args, **kwargs):
        new_user = object.__new__(cls)
        print(f"__new__ {id(new_user)}")
        return new_user

    # def tady(self):
    #     print(self.name)

# Co to je self?
# Je to klicove slovo?

# tohle se deje na pozadi - nepouzivat bezne
# bezne se pouziva User("tomas", 10)
# user = User.__new__(User)
# User.__init__(user, "tomas", 10)
# print(user.name)
# print(user.age)


# def person(name, age, hobbies):
#     print(name, age, hobbies)

# def person(*args, **kwargs):
#     if kwargs.get("hobbies", "vychozi hodnota pokud klic hobbies neexistuje"):
#         print("Oleee mam tu dost informaci!")

    # print(args, kwargs)

# person("tomas", 10)

# user_1 = User("Tomas", 10)
# print(user_1.__dict__)

# user_2 = User("Jozka")

# print(user_1.name)

# print(id(user_1))

# user_1.name = "Alfons"

# print(user_1.name)
# print(user_2.name)

# kdo uz videl hvezdicku?

# FastAPI - controller
# def hello(*, name):
#     print(name)
#
#
# hello(name="tomas")
#
#
# class User:
#     def get_food(self, *, name):
#         print(name)
#
#
# user = User()
# user.get_food(name="paprika")

# vratime se k self
# rikal jsem ze to neni klicove slovo

# for = "Ahoj"
# print(for)

# class = "cau"
# print(class)

# self = "Dobry den"
# print(self)

# import keyword
#
# check_keywords = ["for", "class", "def", "self"]
#
# for word in check_keywords:
#     if keyword.iskeyword(word):
#         print(f"Toto je klicove slovo {word}")
#     else:
#         print(f"Toto neni klicove slovo {word}")


# class attributes

# class User:
#     app_environment = "dev"
#
#     def __init__(this, name):
#         this.name = name
#
# User.app_environment = "prod"
#
# user_1 = User("Pepicek")
# user_2 = User("Anicka")
#
#
# # user_1.app_environment = "prod"
#
# print(user_1.app_environment)
# print(user_2.app_environment)

# GET
# POST

# [GET] https://kosik.cz/ovoce?q=paprika&sort=desc
# query params

# mam formular