"""
Author:  Derek Bittner
Program:  Overriding class methods assignment
"""
from Inheritance.Employee import Employee
from datetime import date


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, start_date, hourly_pay):
        super().__init__(lname, fname)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def hourly_pay(self):
        return self._hourly_pay

    @hourly_pay.setter
    def hourly_pay(self, value):
        if not isinstance(value, float):
            raise ValueError("not a valid hourly wage")
        self._hourly_pay = value

    def give_raise(self, value):
        if value <= self.hourly_pay:
            raise ValueError("pay rate needs to be greater than current pay rate")
        self.hourly_pay = value

    def display(self):
        return Employee.display(self) + ", " + str(self.start_date) + ", $" + str(self.hourly_pay) + "/hr"

"""

    Creates a SalariedEmployee object (select a meaningful name) with your name, start date today, starting salary $40,000.
    Displays the Employee object
    Changes salary to $45,000
    Displays the Employee object
    Performs garbage collection

"""
#Driver
try:
    h_employee = HourlyEmployee("Bittner", "Derek", date.today(), 10.00)
    print(h_employee.display())
    h_employee.give_raise(9.00)
    print(h_employee.display())
except ValueError as err:
    print(err)
finally:
    print(h_employee.display())
    del h_employee





