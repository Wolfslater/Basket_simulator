# Version 3.9.7 12/05/2025

from tkinter import Text, END
from Frutto import Frutto
from widgets import (Warning, DropDown, VALUES,
                    baskets, button, grid, entry, name)

class AddFruit:
    def __init__(self, master, relative):
        # Initialize GUI components and attributes
        self.master = master
        self.master.title("Fruit manager")
        self.relative = relative
        self.fruit = Frutto
        self.selected_basket = ""
        self.capacity = 0.0
        self.fruitSum = 0.0

        # Dropdown for basket selection
        self.dropdown = DropDown(self.master, VALUES, self.dropdownHandler)
        self.dropdown.combobox.grid(row=0, column=0, padx=15)

        self.name_label = name(self.master, text="Fruit name here:")
        self.price_label = name(self.master, text="Fruit price (€/Kg) here:")
        self.weight_label = name(self.master, text="Fruit weight (gr) here:")
        self.last_fruit_label = name(self.master)

        # Labels layout
        grid(widget=self.name_label, row=1, column=0)
        grid(widget=self.price_label, row=2, column=0)
        grid(widget=self.weight_label, row=3, column=0)
        grid(widget=self.last_fruit_label, row=6, column=0, sticky="w")

        # Entry widgets for user inputs
        self.name_entry = entry(self.master, width=35)
        self.price_entry = entry(self.master, width=35)
        self.weight_entry = entry(self.master, width=35)

        # Entry layout
        grid(widget=self.name_entry, row=1, column=1)
        grid(widget=self.price_entry, row=2, column=1)
        grid(widget=self.weight_entry, row=3, column=1)

        # Buttons for actions
        self.add_btn = button(self.master, text="Add the fruit to the basket", command=self.insertFruit)
        self.back_btn = button(self.master, text="Back", command=self.back)
        self.clear_btn = button(self.master, text="Clear fruit entry infos", command=self.clearInfos)

        # Buttons layout
        grid(widget=self.add_btn, row=4, column=1, padx=5, pady=5)
        grid(widget=self.back_btn, row=5, column=0, padx=40, pady=5)
        grid(widget=self.clear_btn, row=5, column=1, padx=5, pady=5)
    
    def back(self):
        # Return to previous window
        self.relative.deiconify()
        self.master.destroy()
        
    def getBasketCapacity(self) -> float:
        # Get capacity of selected basket
        self.capacity = float(baskets.getCapacity(self.selected_basket))
        return self.capacity
        
    def getFruitsSum(self) -> float:
        # Get total weight of fruits in basket
        self.fruitSum = baskets.getNet(self.selected_basket)
        return self.fruitSum
        
    def insertFruit(self):
        # Add fruit to basket or show warning if full
        self.fruit = self.getFruit()
        try:
            if self.fruit:
                self.fruit = Frutto(self.fruit)
            elif self.fruit is None:
                self.fruit = Frutto()
            if self.getBasketName() and self.isFull():
                Warning("3").showWarning()
            else:
                self.last_fruit_label.config(text=f"Last added fruit: {self.fruit.getName()}")
                self.addToBasket()
        except ValueError:
            Warning("2").showWarning()

    def dropdownHandler(self, event=None):
        # Handle basket selection
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem

    def addToBasket(self):
        # Add fruit to basket
        baskets.addFruit(self.selected_basket, self.fruit)
    
    def clearInfos(self):
        # Clear input fields
        for entry in [self.name_entry, self.price_entry, self.weight_entry]:
            entry.delete(0, END)

    def getBasketName(self) -> str:
        # Get selected basket name
        return baskets.getBasket(self.selected_basket)
    
    def getSum(self) -> float:
        # Calculate total weight after adding fruit
        return self.getFruitsSum() + self.fruit.getWeight()

    def getFruit(self) -> list:
        # Retrieve fruit details from input fields
        name = self.name_entry.get()
        price = self.price_entry.get()
        weight = self.weight_entry.get()
        return [name, price, weight]
    
    def isFull(self) -> bool:
        # Check if basket can accommodate more fruits
        if float(baskets.getCapacity(self.selected_basket)) > 0.0:
            if self.getSum() <= self.getBasketCapacity():
                return False
        return True


class RemoveFruit:
    def __init__(self, master, relative):
        self.master = master
        self.master.title("Fruit manager")
        self.relative = relative
        self.selected_basket = ""

        # Text area for basket details
        self.text = Text(self.master, bg="#f0f0f0", width=40, height=10)

        self.removingName = name(self.master, text="Insert here the removing fruit's name:")
        self.removingEntry = entry(self.master)

        self.backBtn = button(self.master, text="Back", command=self.back)
        self.rmvBtn = button(self.master, text="Remove the chosen fruit", command=self.rmvOne)
        self.rmvAllBtn = button(self.master, text="Remove all chosen fruits", command=self.rmvAll)

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

        grid(widget=self.backBtn, row=0, column=0, sticky="ew")
        grid(widget=self.text, row=1, column=0, sticky="nsew")
        grid(widget=self.rmvBtn, row=2, column=0, sticky="ew")
        grid(widget=self.rmvAllBtn, row=2, column=1, sticky="ew")
        grid(widget=self.removingName, row=3, column=0, sticky="ew")
        grid(widget=self.removingEntry, row=3, column=1, sticky="ew")

        self.dropdown = DropDown(self.master, VALUES, self.dropdownHandler)
        self.dropdown.combobox.grid(row=0, column=1, padx=15)

    def back(self):
        self.relative.deiconify()
        self.master.destroy()

    def rmvOne(self):
        try:
            if self.getRemovingEntry() == "":
                raise TypeError
            if self.getBasketName():
                fruit_name = self.getRemovingEntry()
                if fruit_name:
                    baskets.rmvOne(self.selected_basket, fruit_name)
                    self.getFruitsName()  # Refresh the display
        except (TypeError, KeyError):
            Warning("4", self.getRemovingEntry()).showWarning()

    def rmvAll(self):
        try:
            if self.getRemovingEntry() == "":
                raise TypeError
            if self.getBasketName():
                fruit_name = self.getRemovingEntry()
                if fruit_name:
                    baskets.rmvAll(self.selected_basket, fruit_name)
                    self.getFruitsName()  # Refresh the display
        except (TypeError, KeyError):
            Warning("4", self.getRemovingEntry()).showWarning()

    def dropdownHandler(self, event=None):
        # Handle dropdown selection changes
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem
            self.getFruitsName()

    def getBasketName(self) -> str:
        # Get selected basket name
        return baskets.getBasket(self.selected_basket)
    
    def update_text_display(self, content):
        # Update text area with provided content
        self.text.config(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert(END, content)
        self.text.config(state="disabled")
    
    def getFruitsName(self):
        if self.getBasketName():
            self.update_text_display(str(baskets.getFruitsName(self.selected_basket)))

    def getRemovingEntry(self) -> str:
        return self.removingEntry.get()