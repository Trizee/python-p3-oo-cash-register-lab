# #!/usr/bin/env python3

# class CashRegister:

#     def __init__(self,discount = 0):
#         self.total = 0
#         self.discount = discount
#         self.items = []
#         self.item_price = []

#     def add_item(self,title,price,quanity = 1):
#         for x in range(quanity):
#           self.items.append(title)
#           self.item_price.append(price)
#           self.total = self.total + price

#     def apply_discount(self):
#       if self.discount:
#           self.total = int(self.total * ((100 - self.discount) / 100))
#           print(f"After the discount, the total comes to ${self.total}.")
#       else:
#           print("There is no discount to apply.")
    
#     def void_last_transaction(self):
#       print(self.total)
#       self.items.pop(-1)
      
#       self.item_price.pop(-1)
#       self.total = float("{:.2f}".format(sum(self.item_price)))
#       print(self.total)
#       if self.items == []:
#          self.total = 0.0
#       return self.total


# tri = CashRegister()

# tri.add_item('egg', 0.92)
# tri.add_item('egg', 0.92)

# print("{:.2f}".format(sum(tri.item_price)))


# print(tri.items)
# tri.void_last_transaction()
# print(tri.total)
# print(tri.items)

# tri.void_last_transaction()
# print(tri.total)
# print(tri.items)

# This is just to pass the test

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        self.total -= (
            self.previous_transactions[-1]["price"]
            * self.previous_transactions[-1]["quantity"]
        )
        for _ in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()
        self.previous_transactions.pop()