"""Definition: Polymorphism means the same interface can behave differently for different objects.

Explanation:
Polymorphism allows different classes to use the same method name while behaving differently.
This is helpful when writing code that can work with many object types without needing to know their exact class.
Both Dog and Cat respond to speak(), but each returns a different result.
"""


class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


def make_sound(animal):
    return animal.speak()


print("Polymorphism")
print(make_sound(Dog()))
print(make_sound(Cat()))
