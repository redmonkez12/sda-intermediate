# Syntax error

# def hello()
#     pass
#

# hello()

# der hello():
#     pass

# name = "Tomas"
# print(name)

# Name error

# def hello():
#     pass
#
# hell()

# name = "Tomas"
# print(name)

# Value Error, Type Error

# age = input()
# print(int(age))

# age = "20"

# if age > 10:
#     print("Toto je ok")

# total_age = 10 + 20 + 30
# print(total_age / "slunicko")

# pydantic

age = "10"
age = float(age)

if not isinstance(age, float):
    print("fgdfg")
    # zpracovani -> vyhodim vlastni vyjimku nebo
    pass


# print(isinstance(10.1, float))

# Index error
# iterable
# list, string nebo tuple

# name = "Tomas"

# nums = [1, 2, 3]  # 0 -> 1, 1 -> 2, 2 -> 3
# print(nums[3])
#
# for num in [1, 2, 3]:
#     print(num)
#
# while i < 10:
#     list[i]

# Attribute error


# auth = Auth()
# auth.user_name

# kdyz budete posilat spatne udaje do databaze, tak chcete efektivne rozpoznat
# rozdil mezi tim kdyz je duplicitni email a mezitim kdyz duplicitni username

class Auth:
    def __init__(self):
        self.username = "fdfsdfds"
        # tady neco
        pass

    def login(self, username: str, password: str):
        if username != "tomas" or password != "123456":
            raise ZeroDivisionError("Spatny email nebo heslo")

        print("Prihlasuji te")


auth = Auth()

# try:
#     # do try davate bezny kod, ktery muze vyhodit nejakou vyjimku
#     auth.login("jozka", "pepicek123")
# except Exception as e:
#     if isinstance(e, ZeroDivisionError):
#         print("Vyjimka typu zero division")
#     else:
#         print("Spatny email nebo heslo")

# loading = False

try:
    # loading = True
    # do try davate bezny kod, ktery muze vyhodit nejakou vyjimku
    auth.login("tomas", "123456")
except (ZeroDivisionError, ValueError):
    print("Vyjimka typu zero division")
# except ValueError:
#     print("Vyjimka typu zero division")
except Exception:
    print("Spatny email nebo heslo")
else:  # else je volitelne, probehne jenom kdyz v try bloku nenastane zadna vyjimka
    print("Presmerovani na dashboard")
finally:  # finally je volitelne, probehne vzdy bez ohledu na to jestli vyjimka nastane nebo ne
    print("Ja se zavolam jako posledni, haha!")
    # loading = False

print("Sem uz se nedostanu")
