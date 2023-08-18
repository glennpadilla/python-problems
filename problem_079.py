<<<<<<< HEAD
# Write a class that meets these requirements.
#
# Name:       ReceiptItem
#
# Required state:
#    * quantity, the amount of the item bought
#    * price, the amount each one of the things cost
#
# Behavior:
#    * get_total()          # Returns the quantity * price
#
# Example:
#    item = ReceiptItem(10, 3.45)
#
#    print(item.get_total())    # Prints 34.5

class ReceiptItem:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def get_total(self):
        return self.quantity * self.price

item = ReceiptItem(10, 3.45)

print(item.get_total())
=======
# Write a class that meets these requirements.
#
# Name:       ReceiptItem
#
# Required state:
#    * quantity, the amount of the item bought
#    * price, the amount each one of the things cost
#
# Behavior:
#    * get_total()          # Returns the quantity * price
#
# Example:
#    item = ReceiptItem(10, 3.45)
#
#    print(item.get_total())    # Prints 34.5

class ReceiptItem:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def get_total(self):
        return self.quantity * self.price

item = ReceiptItem(10, 3.45)

print(item.get_total())
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
