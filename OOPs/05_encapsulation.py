"""Definition: Encapsulation hides internal data and exposes controlled access through methods.

Explanation:
Encapsulation keeps important data safe by restricting direct access from outside the class.
In Python, this is commonly done by using private attributes, such as __balance, and providing public methods like deposit() and get_balance().
This makes the object easier to manage and protects it from invalid changes.
"""


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
print("Encapsulation")
print(account.get_balance())
