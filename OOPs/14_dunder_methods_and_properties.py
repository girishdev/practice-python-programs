"""Definition: Properties and dunder methods make objects easier to use and help define custom behavior for built-in operations.

Explanation:
The @property decorator lets you access a value through a method-like interface while keeping the logic controlled.
It is useful when you want to expose data safely or convert values behind the scenes.
This example shows how a Celsius value can be read and updated through a Fahrenheit property.
"""


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


temp = Temperature(25)
print("Properties and Dunder-style Custom Behavior")
print(temp.fahrenheit)
temp.fahrenheit = 77
print(temp._celsius)
