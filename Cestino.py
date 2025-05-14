#Version 1.6.7 14/04/2025

from random import uniform

class Cestino:
    def __init__(self,q=None):
        # q èuna lista di frutti da mettere nel cestino, eventualmente vuoti
        self.cestino = set()
        self.capacity = round(uniform(150, 400), 2)
        self.tare = round(uniform(1, 50), 2)
        if not q is None:
            for x in q:
                self.add(x)

    def rmvAll(self, fruit):
        if fruit in self.cestino:
            for i in self.cestino:
                self.cestino.remove(i)

    def rmvOne(self, fruit):
        if fruit in self.cestino:
            self.cestino.remove(fruit)
        
    def clear(self):
        self.cestino.clear()
        
    def add(self, f):
        self.cestino.add(f)
    
    def getCapacity(self):
        return str(self.capacity)
    
    def getNames(self) -> str:
        names = ""
        for x in self.cestino:
            names += f"{x.getName()}\n"
        return names
    
    def getPrice(self):
        c = 0.0
        for x in self.cestino:
            c+=x.price()
        return round(c,2)
    
    def getNet(self):
        c = 0.0
        for x in self.cestino:
            c+=x.getWeight()
        return c
    
    def getGrossWeight(self):
        grossWeight = self.getTare()
        if self.getNet() != 0.0:
            grossWeight = round(float(self.getTare()) + float(self.getNet()), 2)
        return grossWeight
        
    def getTare(self):
        return str(self.tare)
    
    def sumFruit(self):
        fruitSum = 0
        for x in self.cestino:
            fruitSum += x.getWeight()
        return fruitSum
    
    def len(self):
        return len(self.cestino)
    
    def __str__(self):
        s = ""
        for x in self.cestino:
          s += str(x)
          s += "\n"
        return s
