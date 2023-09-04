import time
import requests
import threading


def io_example_func() -> None:
    response = requests.get("https://www.example.com")
    print(response.status_code)


def main():
    first_thread = threading.Thread(target=io_example_func)
    second_thread = threading.Thread(target=io_example_func)

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()


start = time.time()
main()
end = time.time()  # Trvalo to 1.031 sekund

print(f"Trvalo to {end - start:.3f} sekund")


# async await
