"""Definition: Real-world OOP design models objects and relationships from the problem domain, such as Product, Cart, and Order.

Explanation:
In real software, OOP is used to model actual business concepts.
A Product represents an item, a Cart stores selected products, and an Order represents a completed purchase.
This design makes the code easier to understand and maintain.
"""


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


cart = Cart()
cart.add_item(Product("Laptop", 1000))
cart.add_item(Product("Mouse", 25))

print("Real-world OOP Design")
print(Order(cart).checkout())
