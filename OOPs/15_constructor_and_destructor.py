"""Definition: A constructor initializes an object when it is created, and a destructor cleans up resources when it is destroyed.

Explanation:
The constructor __init__ runs automatically when a new object is created.
It sets initial values for the object so it is ready to use.
The destructor __del__ runs when the object is removed and can be used to release resources, although Python does not guarantee immediate cleanup in every situation.
"""


class Laptop:
    def __init__(self, brand):
        self.brand = brand
        print(f"{self.brand} laptop created")

    def __del__(self):
        print(f"{self.brand} laptop destroyed")


print("Constructor and Destructor")
laptop = Laptop("Dell")
del laptop
