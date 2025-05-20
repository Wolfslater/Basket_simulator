#Version 1.2.7 27/04/2025

from random import uniform

class Cestino:
    """
    Class representing a basket that can hold fruits.
    The basket has capacity, tare weight, and can contain multiple fruits.
    """
    def __init__(self, q=None):
        self.cestino = set()
        self.capacity = round(uniform(150, 400), 2)  # Random capacity between 150-400
        self.tare = round(uniform(15, 50), 2)  # Random tare weight between 15-50
        
        if q is not None:
            for x in q:
                self.add(x)
    
    def __str__(self):
        s = ""
        for x in self.cestino:
            s += ("Name:" + x.getName() + ", price: {}kg/€, fruit's price: {}€"
                 .format(x.getPrice(), x.fruitPrice()).replace(".", ","))
            s += "\n"
        return s
    
    # ----- Fruit management methods -----
    
    def add(self, f):
        self.cestino.add(f)
    
    def rmvOne(self, fruit):
        """Remove one fruit with the specified name"""
        for item in self.cestino:
            if item.getName() == fruit:
                self.cestino.remove(item)
                break
    
    def rmvAll(self, fruit):
        """Remove all fruits with the specified name"""
        to_remove = [item for item in self.cestino if fruit == item.getName()]
        for item in to_remove:
            self.cestino.remove(item)
    
    def clear(self):
        """Clears the basket."""
        self.cestino.clear()
    
    # ----- Basket property getters -----
    
    def getCapacity(self) -> str:
        return self.capacity
    
    def getTare(self):
        return self.tare
    
    # ----- Content information methods -----
    
    def len(self) -> int:
        return len(self.cestino)
    
    def getNames(self) -> str:
        """
        Get the names of all fruits in the basket.
        """
        names = ""
        for x in self.cestino:
            names += f"{x.getName()}\n"
        return names
    
    # ----- Weight calculation methods -----
    
    def getNet(self) -> int:
        return sum(x.getWeight() for x in self.cestino)
    
    def getGrossWeight(self) -> float:
        if self.getNet() == 0.0:
            return self.getTare()
        return round(self.getTare() + self.getNet(), 2)
    
    # ----- Price calculation methods -----
    
    def getPrices(self) -> float:
        total = sum(float(x.fruitPrice()) for x in self.cestino)
        return "{:0,.2f}".format(total).replace(".", ",")