"""
Author:  Derek Bittner
Program:  Derived Class assignment

"""
from Inheritance.Person import Person


class Student(Person):
    def __init__(self, s_id, lname, fname, major='Computer Science', gpa=0.0):
        super().__init__(lname, fname)
        self._s_id = s_id
        self._major = major
        self._gpa = gpa

    def display(self):
        return Person.display(self) + "(" + str(self._s_id) + ") " + self._major + " gpa:  " + str(self._gpa)


#Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student

