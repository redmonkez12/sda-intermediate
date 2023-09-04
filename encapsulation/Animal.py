# class UserEntity:
#     def __init__(self) -> None:
#         self._hobbies = []
#
#     def



# class Animal:
#     def __init__(self, favorite_food: list[str]) -> None:
#         self._name = name
#
#     @property  # getter
#     def name(self):
#         return self._name.lower()
#
#     # setter
#     @name.setter
#     def name(self, value: str) -> None:
#         if len(value) < 5:
#             raise Exception("toto nejde")
#
#         self._name = value

# Encapsulation - Access control
# setter, getter
# readonly property


# dog = Animal("Luna")
# print(dog.name)
# dog.name = "Star"
# print(dog.name)



# class Dog(Animal):
#     def __init__(self):
#         self._name

# __name -> _Animal__name name dangling

#
# _name -> protected
# __name -> private = tento attribute budu pouzivat jenom na tride na ktere je to definovane

# Reflection

# dog = Animal("Sunny")
# print(dog.__name)  # name dangling
# print(dog.__dict__)
# print(dog._Animal__name)
# print(dog.get_name())
# dog.__name = "Luna"
# print(dog.__name)
