# soubory a databaze

# SQLAlchemy - Python knihovna

# file = None

# try:
#     file = open("randomfile.txt", "w")
#     file.write("Ahoj lidi!")
#     # tady nekde nastane chyba
# except Exception as e:
#     print("O joj neco se stalo spatne", e)
# finally:
#     file.close()

# context manager

# try:
#     with open("randomfile.txt", "w") as file:
#         file.write("AHoj lidi!")
# except Exception:
#     print("O joj neco se stalo spatne")

class File:
    def __init__(self, filename: str, method: str):
        print("Ted se vola __init__")
        self.file = open(filename, method)

    def __enter__(self):
        print("Zaciname!!!")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Koneeeeeeec")
        self.file.close()
        print(exc_type, exc_val, exc_tb)

#
# with File("randomfile.txt", "w") as file:
#     file.write("Pepicek a Manicka")
#     raise Exception("Ouch co to je?")


from contextlib import contextmanager

# generator

# eager pristup
# lazy pristup


@contextmanager
def File(filename: str, mode: str):
    print("Ted se vola __init__")
    file = open(filename, mode)

    try:
        yield file  # generator
    except Exception as e:
        print("Error", e)
        # raise e
        # print("tady uz nic")
    finally:
        file.close()


with File("randomfile.txt", "w") as file:
    file.write("Pepicek a Manicka")
    raise Exception("Ouch co to je?")
