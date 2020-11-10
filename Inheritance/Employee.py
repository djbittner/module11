"""
Author:  Derek Bittner
Program:  Overriding class methods assignment

"""
from datetime import date


class Employee:
    """Employee Class"""

    #Constructor
    def __init__(self, lname, fname):
        self.last_name = lname
        self.first_name = fname

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    def display(self):
        return "{}, {}".format(self.last_name, self.first_name)
"""

    def display(self):
        if self._salaried:
            return str(self.first_name) + " " + str(self.last_name) + "\n" \ 
                + str(self.address)+ "\n" + str(self.phone_number) + "\n" \
                + "Salaried Employee: $" + str(self.salary) + "\n" \
                "Start date:  " + str(self.start_date)
        else:
            return str(self.first_name) + " " + str(self.last_name) + "\n" \
                + str(self.address) + "\n" + str(self.phone_number) + "\n" \
                + "Hourly employee: $" + str(self.salary) + "/hour\n" \
                + "Start date:  " + str(self.start_date)

     def __str__(self):
        return 'Employee: first name = ' + str(self.first_name) + " " + str(self.last_name) + "\n"\
                + str(self.address) + "\n" + str(self.phone_number) + "\n"\
                + "Salaried employee: $" + str(self.salary) + "/year" + "\n" + str(self.start_date)

"""
