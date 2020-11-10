"""
Author:  Derek Bittner
Program:  Overriding Class methods assignment

"""

from Inheritance.Employee import Employee
from datetime import date


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, start_date, salary):
        super().__init__(lname, fname)
        self.start_date = start_date
        self.salary = salary

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, float):
            raise ValueError("not a valid salary")
        self._salary = value

    def give_raise(self, value):
        if value <= self.salary:
            raise ValueError("salary raise needs to be greater than current salary!")
        self.salary = value

    def display(self):
        return Employee.display(self) + ", " + str(self.start_date) + ", $" + str(self.salary) + "/year"


#Driver
try:
    s_employee = SalariedEmployee("Bittner", "Derek", date.today(), 40000.00)
    print(s_employee.display())
    s_employee.give_raise(45000.00)
    print(s_employee.display())
except ValueError as err:
    print(err)
finally:
    print(s_employee.display())
    del s_employee



