# def counter():
#     count = 0
#
#     def inner_function():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return inner_function
#
# epic_counter = counter()
# epic_counter()
# epic_counter()
# epic_counter()
# epic_counter()
# epic_counter()


# def greeter(func):
#     # closure
#
#     def wrapper(a):
#         print("Volam wrapper() zacatek")
#         func(a)
#         print("Volam wrapper() konec")
#
#     return wrapper


# hi_greeter = greeter("Hi!")

# def say_hi():
#     print("hi")

# def greeter(func):
#     # closure
#
#     def wrapper(*args, **kwargs):
#         print(args, kwargs)
#         # args = tuple pro normalni argument func(1, 2, 3, 4)
#         # kwargs = dictionary pro pozicni argument func(a=1, b=2, c=2)
#         print("Volam wrapper() zacatek")
#         value = func(*args, **kwargs)
#         print("Volam wrapper() konec")
#
#         return value
#
#     return wrapper

def greeter(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)

        # if not isinstance(value, Response):
        #     raise Exception("This framework works only with Response object")

    return wrapper


@greeter
def sum(a, b):
    return a + b

num = sum(1, 2)
print(num)


# @greeter
# def say_hello(greet_type: str):
#     print(greet_type)
#
#
# say_hello("Hello")

# def sum():

# hi_greeter = greeter(say_hi)
# hi_greeter()
#
# hello_greeter = greeter(say_hello)
# hello_greeter("hello")
