class Money:
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency

    def __add__(self,other):
        if self.currency.lower() != other.currency.lower():
            raise RuntimeError("Mismatched currencies!")
        
        return Money(self.amount+other.amount,self.currency)
    
    def __sub__(self,other):
        if self.currency.lower() != other.currency.lower():
            raise RuntimeError("Mismatched currencies!")
        
        return Money(self.amount-other.amount,self.currency)

    def __mul__(self,factor):
        return Money(factor * self.amount,self.currency) 