"""OOP concepts in Python with simple examples."""

from abc import ABC, abstractmethod


# 1) Class and Object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Corolla")
print("1) Class and Object")
print(my_car.info())
print()


# 2) What is self?
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"  # self refers to the current object


student = Student("Asha")
print("2) What is self?")
print(student.greet())
print()


# 3) What is __init__?
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Rahul", 22)
print("3) What is __init__?")
print(person.name, person.age)
print()


# 4) Instance variable vs class variable
class BankAccount:
    interest_rate = 0.05  # class variable

    def __init__(self, owner, balance):
        self.owner = owner          # instance variable
        self.balance = balance      # instance variable


account1 = BankAccount("Nina", 1000)
account2 = BankAccount("Sam", 2000)
print("4) Instance variable vs class variable")
print(account1.interest_rate)
print(account2.interest_rate)
print(account1.balance)
print()


# 5) Instance method vs class method vs static method
class Calculator:
    def instance_method(self, x, y):
        return x + y

    @classmethod
    def class_method(cls, x, y):
        return x * y

    @staticmethod
    def static_method(x, y):
        return x - y


calc = Calculator()
print("5) Methods")
print(calc.instance_method(3, 4))
print(Calculator.class_method(3, 4))
print(Calculator.static_method(10, 4))
print()


# 6) Encapsulation
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary


emp = Employee("Meera", 50000)
print("6) Encapsulation")
print(emp.get_salary())
emp.set_salary(55000)
print(emp.get_salary())
print()


# 7) Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


print("7) Inheritance")
print(Dog("Buddy").speak())
print()


# 8) Method overriding
class Cat(Animal):
    def speak(self):
        return "Meow"


print("8) Method overriding")
print(Cat("Milo").speak())
print()


# 9) Polymorphism
class Bird(Animal):
    def speak(self):
        return "Chirp"


def animal_sound(animal):
    return animal.speak()


animals = [Dog("Bruno"), Cat("Kitty"), Bird("Tweety")]
print("9) Polymorphism")
for animal in animals:
    print(animal_sound(animal))
print()


# 10) Abstraction
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentGateway):
    def pay(self, amount):
        return f"Paid {amount} via PayPal"


class Stripe(PaymentGateway):
    def pay(self, amount):
        return f"Paid {amount} via Stripe"


print("10) Abstraction")
print(PayPal().pay(100))
print(Stripe().pay(200))
print()


# 11) Composition vs inheritance
class Engine:
    def start(self):
        return "Engine started"


class CarWithEngine:
    def __init__(self):
        self.engine = Engine()  # composition

    def drive(self):
        return self.engine.start()


print("11) Composition")
print(CarWithEngine().drive())
print()


# 12) MRO (Method Resolution Order)
class A:
    def show(self):
        return "A"


class B(A):
    pass


class C(A):
    def show(self):
        return "C"


class D(B, C):
    pass


print("12) MRO")
print(D.__mro__)
print(D().show())
print()


# 13) Magic methods
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
print("13) Magic methods")
print(book1)
print(book1 + book2)
print()


# 14) Real-world OOP design
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.price for item in self.items)


class Order:
    def __init__(self, cart):
        self.cart = cart

    def checkout(self):
        return f"Order placed with total ${self.cart.total()}"


print("14) Real-world OOP design")
cart = Cart()
cart.add_item(Product("Laptop", 1000))
cart.add_item(Product("Mouse", 25))
order = Order(cart)
print(order.checkout())
print()

print("All OOP concepts demonstrated successfully.")