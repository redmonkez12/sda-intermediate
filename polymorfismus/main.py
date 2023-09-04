# God class
# parent class - rodicovska trida
# kompozice

# Muzete dedit vice nez 1 tridu
class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

        print("Ja jsem __init__ z employee")

    # def pay_me(self):
    #     print("Jdu ti poslat penize na ucet")

    def __repr__(self):
        return f"{self.name}"


# child class, derived class - potomek, dite
class Manager(Employee):
    def __init__(self, name: str, salary: int, report_list: list[str]) -> None:
        super().__init__(name, salary)
        self.report_list = report_list

        print("Ja jsem __init__ z managera")

    def pay_me(self):
        # super().pay_me()
        print("Manazer dostava penize")


# franta = Manager("Franta", 100, ["prezentace s jozkou..."])
# franta.pay_manager()
# print(franta)


class Contractor(Employee):
    def __init__(self, name: str, total_allocation: int, per_hour: int) -> None:
        salary = total_allocation * per_hour

        super().__init__(name, salary)

    def pay_me(self):
        print("KOntraktor dostava penize")


employees = [
    Manager("Franta", 100, ["prezentace s jozkou..."]),
    Contractor("Jozka", 160, 10),
    Contractor("Lojza", 160, 12),
    Manager("Ignac", 50, ["KOntrola kontraktoru"]),
]

# class RandomClass:
#     pass
#
# print(issubclass(Contractor, RandomClass))

for employee in employees:
    employee.pay_me()
    # if issubclass(employee, )
    # if isinstance(employee, Contractor):
    #     employee.pay_contractor()
    # elif isinstance(employee, Manager):
    #     employee.pay_manager()
    # elif

# polymorfismus
# mam stejne metody na vice tridach

# Ze si budete verit
# Abstraktni tridy -> Spise se tvari jako interface (rozhrani)
