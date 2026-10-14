"""Definition: Instance variables belong to each object, while class variables belong to the class and are shared by all objects.

Explanation:
Instance variables store data that is unique to each object, such as name or salary.
Class variables store data that is common to all objects of the class, such as the company name.
This example shows how one class variable is shared by all Employee objects.
"""


class Employee:
    company = "ABC Corp"  # Class variable shared by all objects

    def __init__(self, name, salary):
        self.name = name          # Instance variable
        self.salary = salary      # Instance variable


emp1 = Employee("Nina", 50000)
emp2 = Employee("Sam", 60000)

print("Instance vs Class Variables")
print(emp1.company)
print(emp1.name, emp1.salary)
print(emp2.company)
print(emp2.name, emp2.salary)
