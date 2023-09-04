import time
import requests


def io_example_func() -> None:
    response = requests.get("https://www.example.com")
    print(response.status_code)


def main():
    io_example_func()
    io_example_func()


start = time.time()
main()
end = time.time()

print(f"Trvalo to {end - start:.3f} sekund")