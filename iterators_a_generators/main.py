# generator x iterator
# iterator - imperativni zapis
# generator - deklarativni

animals = ["Chicken", "Dog", "Cat"]

# ctrl + b nebo cmd + b

# for index, item in enumerate(animals, start=2):
#     print(index, item)


class MyEnumerate:
    def __init__(self, data, start):
        self.data = data
        self.index = 0
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        index = self.index + self.start
        item = self.data[self.index]

        value = (index, item)
        self.index += 1

        return value


# enumerate - mam pristup na index i hodnotu + muzu si rict pocatecni hodnotu indexu
for index, item in enumerate(animals, start=2):  # built in enumerate
    print(index, item)

# for index, item in MyEnumerate(animals, start=2):
#     print(index, item)

# for index in range(0, len(animals)):
#     print(animals[index])
#
#
# for animal in animals:
#     print(animal)


# animals = ["Chicken", "Dog", "Cat"]
#
# iter_animals = iter(animals)
#
# while True:
#     try:
#         animal = next(iter_animals)
#         print(animal)
#     except StopIteration:
#         break

#
# print(next(iter_animals))
# print(next(iter_animals))
# print(next(iter_animals))
# print(next(iter_animals))  #

# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration()
#         # Musi byt StopIteration Error
#
#         current = self.start
#         self.start += 1
#
#         return current
#
#
# for item in MyRange(1, 10):
#     print(item)
#
#
# # list, tuple, string, dict
#
# # I nad jakoukoliv tridou, pokud...
#
# data = ["Pepicek", "Anicka", "Lojza"]
#
# for item in data:
#     print(item)
#
# for item in 10:
#     print(item)
#
# # int nema naimplementovany iterator protocol
#
# # __iter__ -> vraci iterator
# #
# # __next__ -> StopIterator error