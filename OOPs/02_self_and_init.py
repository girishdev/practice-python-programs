"""Definition: self refers to the current object, and __init__ is the constructor used to initialize object attributes.

Explanation:
self is a reference to the object that is currently being used.
It allows methods to access and modify the object's own data.
__init__ is called automatically when an object is created so that its initial state is set up.
"""


class Student:
    def __init__(self, name, age):
        # __init__ runs automatically when an object is created
        self.name = name
        self.age = age

    def introduce(self):
        # self allows access to the object's data
        return f"Hi, I am {self.name} and I am {self.age} years old."


student = Student("Asha", 21)
print("self and __init__")
print(student.introduce())
