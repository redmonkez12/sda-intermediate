import multiprocessing
import os


def krasna_funkce():
    print(f"Jsem jine idecko? {os.getpid()}")


if __name__ == "__main__":
    krasny_proces = multiprocessing.Process(target=krasna_funkce)
    krasny_proces.start()
    print(f"Jsem ja taky jine idecko? {os.getpid()}")
    krasny_proces.join()