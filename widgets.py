# Version 0.3.3 12/05/2025

from tkinter import Label, Button, Entry, messagebox
from tkinter.ttk import Combobox
from Cestino import Cestino

class DropDown:
    """
    A dropdown widget for selecting baskets.
    """
    def __init__(self, master, VALUES, callback, overlay=None):
        """
        Initialize the dropdown with values and callback.
        """
        self.combobox = Combobox(master, width=40)
        self.combobox["values"] = VALUES
        self.combobox["state"] = "readonly"
        self.callback = callback
        self.overlay = overlay

        if self.callback:
            self.combobox.bind("<<ComboboxSelected>>", self.callback)

    def getBasket(self) -> str:
        """
        Get the selected basket name.
        """
        return self.combobox.get()


class Factory:
    """
    Factory class for creating and configuring GUI widgets.
    """
    @staticmethod
    def newLabel(master, text=None, width=0) -> Label:
        """Create a new label widget."""
        return Label(master, text=text, width=width)
    
    @staticmethod
    def newEntry(master, width=0) -> Entry:
        """Create a new entry widget."""
        return Entry(master, width=width)
    
    @staticmethod
    def newButton(master, text=None, command=None, width=0) -> Button:
        """Create a new button widget."""
        return Button(master, text=text, command=command, width=width)
    
    @staticmethod
    def gridConfig(widget, row, column, padx=0, pady=0, sticky="", columnspan=1, width=0, height=0) -> object:
        """Configure grid placement for a widget."""
        widget.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky, columnspan=columnspan)
        return widget


class Warning:
    """
    Class for displaying warning messages.
    """
    def __init__(self, message, fruit=None):
        """
        Initialize with a message code and optional fruit name.
        """
        self.message = message
        self.fruit = fruit

    def matchMessage(self) -> str:
        """
        Match the message code to a warning message.
        """
        match self.message:
            case "1":
                return "Please select a basket first"
            case "2":
                return "ERROR: MISSING DATA OR WRONG DATA TYPE.\nPrice and weight must be numeric values."
            case "3":
                return "Full basket.\nPlease select another basket!"
            case "4":
                return f"No fruits named: {self.fruit}"
            case _:
                return "Unknown warning"

    def showWarning(self):
        """Display the warning message in a dialog."""
        messagebox.showwarning("WARNING", self.matchMessage())


class Baskets:
    """
    Class for managing multiple baskets.
    """
    def __init__(self):
        """Initialize with five empty baskets."""
        self.baskets = {
            "Basket 1": Cestino(),
            "Basket 2": Cestino(),
            "Basket 3": Cestino(),
            "Basket 4": Cestino(),
            "Basket 5": Cestino()
        }
        
    def rmvAll(self, basketName, fruitName=None):
        """
        Remove all instances of a fruit from a basket.
        """
        if basketName in self.baskets:
            self.baskets[basketName].rmvAll(fruitName)
    
    def rmvOne(self, basketName, fruitName=None):
        """
        Remove one instance of a fruit from a basket.
        """
        if basketName in self.baskets:
            self.baskets[basketName].rmvOne(fruitName)

    def getCapacity(self, basketName) -> float:
        """
        Get the capacity of a basket.
        """
        if basketName in self.baskets:
            return self.baskets[basketName].getCapacity()
        return 0.0
        
    def getNet(self, basketName) -> float:
        """
        Get the net weight of a basket.
        """
        if basketName in self.baskets:
            return self.baskets[basketName].getNet()
        return 0.0

    def getBasket(self, basketName):
        """
        Get a basket by name.
        """
        if basketName in self.baskets:
            return self.baskets[basketName]
        return Warning("1").showWarning()

    def getBasketsName(self) -> list:
        """
        Get a list of all basket names.
        """
        return list(self.baskets.keys())
    
    def getFruitsName(self, basketName) -> str:
        """
        Get names of all fruits in a basket.
        """
        if basketName in self.baskets:
            return self.baskets[basketName].getNames()
        return ""

    def addFruit(self, basketName, fruit):
        """
        Add a fruit to a basket.
        """
        if basketName in self.baskets:
            self.baskets[basketName].add(fruit)
    
    def clear(self, basketName):
        """
        Clear all fruits from a basket.
        """
        if basketName in self.baskets:
            self.baskets[basketName].clear()

baskets = Baskets()
VALUES = baskets.getBasketsName()

name = Factory.newLabel
entry = Factory.newEntry
button = Factory.newButton
grid = Factory.gridConfig
