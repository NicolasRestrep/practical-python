# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name 
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.price*self.shares
    
    def sell(self, amt):
        self.shares -= amt
    
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
    