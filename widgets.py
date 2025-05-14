# Version 0.5.3 14/05/2025

from tkinter import Label, Button, Entry, messagebox
from tkinter.ttk import Combobox
from Cestino import Cestino  # Import the Cestino class, presumably for basket management

# DropDown class for creating a read-only dropdown menu
class DropDown:
    def __init__(self, master, VALUES, callback, overlay=None):
        self.combobox = Combobox(master, width=40)
        self.combobox["values"] = VALUES  # Set dropdown options
        self.combobox["state"] = "readonly"  # Make dropdown read-only
        self.callback = callback
        self.overlay = overlay

        if self.callback:
            self.combobox.bind("<<ComboboxSelected>>", self.callback)  # Bind selection event to callback

    def getBasket(self) -> object:
        return self.combobox.get()  # Get selected basket

# Factory class for creating and configuring GUI widgets
class Factory:

    @staticmethod
    def newLabel(master, text=None, width=0) -> object:
        return Label(master, text=text, width=width)  # Create a label
    
    @staticmethod
    def newEntry(master, width=0) -> object:
        return Entry(master, width=width)  # Create an entry field
    
    @staticmethod
    def newButton(master, text=None, command=None, width=0) -> object:
        return Button(master, text=text, command=command)  # Create a button
    
    @staticmethod
    def gridConfig(widget, row, column, padx=0, pady=0, sticky="", columnspan=1, width=0, height=0) -> object:
        widget.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky, columnspan=columnspan)
        return widget  # Configure widget's grid placement

# Warning class for displaying warning messages
class Warning:
    def __init__(self, message):
        self.message = message

    def matchMessage(self) -> str:
        match self.message:
            case "1":
                return "Please select a basket first"
            case "2":
                return "ERROR: MISSING DATA OR WRONG DATA TYPE.\nPrice and weight must be numeric values."
            case "3":
                return "Full basket.\nPlease select another basket!"
            case "4":
                return "No fruits named this way"

    def showWarning(self):
        messagebox.showwarning("WARNING", self.matchMessage())  # Show warning with matched message

# Baskets class for managing multiple baskets
class Baskets:
    def __init__(self):
        self.baskets = {
            "Basket 1": Cestino(),
            "Basket 2": Cestino(),
            "Basket 3": Cestino(),
            "Basket 4": Cestino(),
            "Basket 5": Cestino()
        }

    def rmvAll(self, basketName, fruitName=None):
        if basketName in self.baskets:
            baskets.rmvAll(fruitName)
    
    def rmvOne(self, basketName, fruitName=None):
        if basketName in self.baskets:
            baskets.rmvOne(fruitName)

    def getCapacity(self, basketName) -> float:
        # Get the capacity of a specific basket
        if basketName in self.baskets:
            return self.baskets[basketName].getCapacity()
        else:
            return 0.0

    def getFruitSum(self, basketName) -> float:
        # Get the total weight/quantity of fruits in a basket
        if basketName in self.baskets:
            return self.baskets[basketName].sumFruit()
        else:
            return 0.0

    def getBasket(self, basketName) -> str:
        # Retrieve a basket object by name
        if basketName in self.baskets:
            return self.baskets[basketName]
        else:
            return Warning("1").showWarning()

    def getBasketsName(self) -> list:
        return list(self.baskets.keys())  # Return list of basket names
    
    def getFruistName(self, basketName) -> str:
        if basketName in self.baskets:
            return self.baskets[basketName].getNames()

    def addFruit(self, basketName, fruit):
        # Add a fruit to a specific basket
        if basketName in self.baskets:
            self.baskets[basketName].add(fruit)
    
    def clear(self, basketName):
        if basketName in self.baskets:
            self.baskets[basketName].clear()

# Initialize baskets and dropdown values
baskets = Baskets()
VALUES = baskets.getBasketsName()

# Shortcuts for creating widgets using Factory
name = Factory.newLabel
entry = Factory.newEntry
button = Factory.newButton
grid = Factory.gridConfig
