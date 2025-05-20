#Version 1.0.3 17/05/2025

import random

class Frutto:
    """
    Class representing a fruit with name, price per kg, and weight in grams.
    """
    def __init__(self, q=["", "", ""]):
        if q == ["", "", ""]:
            x = random.randint(0, 1)
            if x == 0:
                self.name = "ciliegia"  # Cherry
                self.price_kg = round(random.uniform(5, 9), 2)
                self.weight_gr = random.randint(2, 25)
            else:
                self.name = "pesca"  # Peach
                self.price_kg = round(random.uniform(2, 7), 2)
                self.weight_gr = random.randint(15, 60)
        else:
            self.name = q[0].lower()
            self.price_kg = float(q[1])
            self.weight_gr = float(q[2])
    
    def __str__(self) -> str:
        return (f"{self.name} (weight {self.getWeight()}gr, "
                f"price {self.getPrice()}€/kg, price {self.fruitPrice()}€)")
    
    # ----- Getter methods -----
    
    def getName(self) -> str:
        return self.name
    
    def getPrice(self) -> float:
        return self.price_kg
    
    def getWeight(self) -> float:
        return self.weight_gr
    
    # ----- Setter methods -----
    
    def setName(self, x) -> str:
        self.name = x
    
    def setPrice(self, x) -> float:
        self.price_kg = x
    
    def setWeight(self, x) -> float:
        self.weight_gr = x
    
    # ----- Calculation methods -----
    
    def fruitPrice(self) -> str:
        price = (self.weight_gr / 1000) * self.price_kg
        return str(round(price, 2))