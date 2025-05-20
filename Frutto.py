#Version 1.0.3 17/05/2025

import random

class Frutto:
    """
    Class representing a fruit with name, price per kg, and weight in grams.
    """
    def __init__(self, q=["", "", ""]):
        """
        Initialize a fruit with optional parameters or random values.
        """
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
        """
        String representation of the fruit.
        """
        return (f"{self.name} (weight {self.getWeight()}gr, "
                f"price {self.getPrice()}€/kg, price {self.fruitPrice()}€)")
    
    # ----- Getter methods -----
    
    def getName(self) -> str:
        """Get the name of the fruit."""
        return self.name
    
    def getPrice(self) -> float:
        """Get the price per kg of the fruit."""
        return self.price_kg
    
    def getWeight(self) -> float:
        """Get the weight in grams of the fruit."""
        return self.weight_gr
    
    # ----- Setter methods -----
    
    def setName(self, x):
        """Set the name of the fruit."""
        self.name = x
    
    def setPrice(self, x):
        """Set the price per kg of the fruit."""
        self.price_kg = x
    
    def setWeight(self, x):
        """Set the weight in grams of the fruit."""
        self.weight_gr = x
    
    # ----- Calculation methods -----
    
    def fruitPrice(self) -> set:
        """
        Calculate the price of the fruit based on weight and price per kg.
        """
        price = (self.weight_gr / 1000) * self.price_kg
        return str(round(price, 2))
