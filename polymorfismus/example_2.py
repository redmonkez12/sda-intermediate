# abstract class Employee():
#     public Employee():

from abc import ABC, abstractmethod
from dataclasses import dataclass
#
#
# # Abstraktni tridy -> Spise se tvari jako interface (rozhrani)
#
# @dataclass  # dekorator
# class Employee(ABC):
#     # def __init__(self, name: str, id: int):
#     #     self.name = name
#     #     self.id = id
#     # name: str
#     # id: int
#
#     @abstractmethod
#     def compute_pay(self) -> float:
#         pass


class Employee(ABC):
    @abstractmethod
    def compute_pay(self):
        pass


class HourlyEmployee(Employee):
    def compute_pay(self) -> float:
        pass


class Accountant:

    def pay_employee(self, employee: Employee) -> float:
        return employee.compute_pay()


alfons = Accountant()
alfons.pay_employee(HourlyEmployee())

# class HourlyEmployee(Employee):
#     def compute_pay(self) -> float:
#         return 1000
#
#
# class SalaryEmployee(Employee):
#     def compute_pay(self) -> float:
#         return 1000
#
#
# employee = HourlyEmployee(name="Tomas", id=1)
#
# employees = [
#     HourlyEmployee(name="Tomas", id=1),
#     SalaryEmployee(name="Borek", id=2),
# ]
#
# for employee in employees:
#     value = employee.compute_pay()
#     print(value)
#


# @dataclass
# class Employee:
#     name: str
#     id: int
#
#
# tomas_2 = Employee("Tomas", 1)
# tomas_1 = Employee("Tomas", 1)
# print(tomas_1)
# print(tomas_1 == tomas_2)

#
#
# # employee = Employee(name="Tomas", id=1)
# # print(employee)
