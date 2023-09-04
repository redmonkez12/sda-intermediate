import functools


@functools.lru_cache
# @functools.cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


result = fibonacci(50)
print(result)

# 0 1 1 2 3 5 8 13 21...
