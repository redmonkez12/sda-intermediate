import time


def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        value = func(*args, **kwargs)

        end = time.time()
        print(f"Ubehnuty cas: {end - start}")

        return value, end - start

    return wrapper


@timer
def main():
    # tady bude nejaka epicka logika
    value = fib(38)
    print(value)


if __name__ == "__main__":
    _, time = main()
    print(_, time)


# def funny_decorator(func):
#     def wrapper(*args, **kwargs):
#         value = func(5, 6)
#
#         return value
#
#     return wrapper
#
#
# @funny_decorator
# def sum(a, b):
#     return a + b
#
# value = sum(1, 2)
# print(value)