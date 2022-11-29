#!/usr/bin/python3


class Employee:

    "Commom base class for all employees"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):

        print("Name :", self.name, "Salary :", self.salary)


emp1 = Employee("Yeanoh", 2000)
emp2 = Employee("Aliyah", 4000)
emp3 = Employee("Ibrahim", 10000)
emp4 = Employee("Medisha", 15000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
print("Total Employee %d" % Employee.empCount)
