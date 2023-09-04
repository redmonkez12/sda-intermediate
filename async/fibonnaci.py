import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n < 2:
            return n

        return fib(n - 1) + fib(n - 2)

    result = fib(number)
    print(f"fib({number}) je {result}")


def main():
    print_fib(37)
    print_fib(38)


start = time.time()
main()
end = time.time()

print(f"Trvalo to {end - start:.3f} sekund")