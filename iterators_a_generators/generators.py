# chain
# from itertools import chain
#
#
# for item in chain("chicken", [1, 2, 3], {"name": "Tomas", "age": 10}):
#     print(item)

import time

# def custom_chain(*args):
#     result = []
#
#     for arg in args:  # chicken [1, 2, 3] {"name": "Tomas", "age": 10}
#         for item in arg:
#             time.sleep(0.5)
#
#             result.append(item)
#
#     return result
#
#
# for item in custom_chain("chicken", [1, 2, 3], {"name": "Tomas", "age": 10}):
#     print(item)

# def custom_chain(*args):
#     for arg in args:  # chicken [1, 2, 3] {"name": "Tomas", "age": 10}
#         for item in arg:
#             # tady muzu delat cokoliv
#             time.sleep(0.5)  # simulace sloziteho vypoctu
#
#             yield item
#
#
# for item in custom_chain("chicken", [1, 2, 3], {"name": "Tomas", "age": 10}):
#     print(item)

# zip
ids = [1, 2, 3, 4, 5, 6]
names = ["Sunny", "Luna", "Black", "Oliver"]

# for item in zip(ids, names, ["a", "b", "c"]):
#     print(item)

# print(list())
# coroutines, asynchronni programovani
# asyncio


# def custom_zip(*args):
#     iterators = [iter(it) for it in args]  # list comprehensions
#
#     # iterators = []
#     # for it in args:
#     #     iterators.append(it)
#
#     while True:
#         try:
#             yield tuple(next(it) for it in iterators)
#         except Exception:
#             break
#
#
# for item in custom_zip(ids, names):
#     print(item)

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

# def my_range(start, end):
#     while start < end:
#         yield start
#         start += 1
#
#
# for item in my_range(1, 10):
#     print(item)

# import sys
# import time

# result = [1, time.sleep(1), time.sleep(1)]  # eager
#
# print(result[0])

# numbers = [i ** 2 for i in range(100000000)]

# print(sys.getsizeof(numbers))


# def square_numbers():
#     for i in range(100000000):
#         yield i ** 2
#
# generator = square_numbers()
#
# print(sys.getsizeof(next(generator)))
# print(sys.getsizeof(next(generator)))
# print(sys.getsizeof(next(generator)))
# print(sys.getsizeof(next(generator)))
print(sys.getsizeof(next(generator)))
