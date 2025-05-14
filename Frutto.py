#Version 1.0.1 21/04/2025

import random

class Frutto:
    def __init__(self, q=["", "", ""]):
        # q è una lista [nom,pre,pes] oppure è None (in tal caso, frutto Random)
        if q == ["", "", ""]:
            x = random.randint(0,1)
            if x==0:
                self.name = "Ciliegia"
                self.price_kg = round(random.uniform(5,9),2)
                self.weight_gr = random.randint(2,25)
            else:
                self.name = "Pesca"
                self.price_kg = round(random.uniform(2,7),2)
                self.weight_gr = random.randint(15,60)
        else:
            self.name = q[0]
            self.price_kg = float(q[1])
            self.weight_gr = int(q[2])

    def __str__(self):
        s = ""
        s += self.name + " ("
        s += "weight " + str(self.weight_gr) + "gr, "
        s += "price " + str(self.price_kg) + "€/kg"
        s += ", price " + str(self.price()) + "€)"
        return s

# I getter non prendono parametri formali #
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price_kg
    def getWeight(self):
        return self.weight_gr
    
    def setName(self, x):
        self.name = x
    def setPrice(self, x):
        self.price_kg = x
    def setWeight(self, x):
        self.weight_gr = x
    
    def price(self):
        c  = (self.weight_gr / 1000) * self.price_kg
        return round(c,2)