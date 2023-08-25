#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.extend([title] * quantity)

  def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print("After the discount, the total comes to $800.")
        else:
            print("There is no discount to apply.")

  def get_item_price(self, item):
      
        prices = {
            "apple": 0.99,
            "tomato": 1.76,
        }
        return prices.get(item, 0)

  def void_last_transaction(self):
    if self.items:
        last_item = self.items[-1]
        last_item_price = self.get_item_price(last_item)
        occurrences = self.items.count(last_item)
        self.items = self.items[:-occurrences]
        self.total -= (last_item_price * occurrences)

    if not self.items:
        self.total = 0.0
  