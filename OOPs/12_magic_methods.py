"""Definition: Magic methods are special methods in Python that begin and end with double underscores, such as __str__ and __add__.

Explanation:
Magic methods allow objects to interact with Python syntax and built-in operations.
For example, __str__ controls how an object is printed, and __add__ defines what happens when two objects are added together.
They make custom classes behave more naturally.
"""


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} - ${self.price}"

    def __add__(self, other):
        return self.price + other.price


book1 = Book("Python Basics", 20)
book2 = Book("OOP Guide", 30)

print("Magic Methods")
print(book1)
print(book1 + book2)
