import time
# import threading
import multiprocessing


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n < 2:
            return n

        return fib(n - 1) + fib(n - 2)

    result = fib(number)
    print(f"fib({number}) je {result}")


def main():
    first_thread = multiprocessing.Process(target=print_fib, args=(37,))
    second_thread = multiprocessing.Process(target=print_fib, args=(38,))

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print(f"Trvalo to {end - start:.3f} sekund")  # Trvalo to 7.766 sekund
