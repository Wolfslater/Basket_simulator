# Version 3.10.7 12/05/2025

from tkinter import Text, END
from Frutto import Frutto
from widgets import (Warning, DropDown, VALUES,
                    baskets, button, grid, entry, name)

class AddFruit:
    """
    Class for adding fruits to baskets through a GUI interface.
    """
    def __init__(self, master, relative):
        """
        Initialize the fruit addition window.
        """
        self.master = master
        self.master.title("Fruit manager")
        self.relative = relative
        self.fruit = Frutto
        self.placeholderMessage = "Leave empty fot a random fruit."  # Placeholder text for entries
        self.defaultFg = "black"  # Default text color
        self.color = "grey"  # Placeholder text color
        self.selected_basket = ""
        self.capacity = 0.0
        self.fruitSum = 0.0

        # Create dropdown for basket selection
        self.dropdown = DropDown(self.master, VALUES, self.dropdownHandler)
        self.dropdown.combobox.grid(row=0, column=0, padx=15)

        # Create labels for entry fields
        self.name_label = name(self.master, text="Fruit name here:")
        self.price_label = name(self.master, text="Fruit price (€/Kg) here:")
        self.weight_label = name(self.master, text="Fruit weight (gr) here:")
        self.last_fruit_label = name(self.master)

        # Position labels in grid
        grid(widget=self.name_label, row=1, column=0)
        grid(widget=self.price_label, row=2, column=0)
        grid(widget=self.weight_label, row=3, column=0)
        grid(widget=self.last_fruit_label, row=6, column=0, sticky="w")

        # Create entry fields
        self.name_entry = entry(self.master, width=35)
        self.price_entry = entry(self.master, width=35)
        self.weight_entry = entry(self.master, width=35)

        # Set initial placeholder text
        self.name_entry.insert(0, self.placeholderMessage)
        self.price_entry.insert(0, self.placeholderMessage)
        self.weight_entry.insert(0, self.placeholderMessage)

        # Set placeholder text color
        self.name_entry.configure(fg=self.color)
        self.price_entry.configure(fg=self.color)
        self.weight_entry.configure(fg=self.color)

        # Bind focus events to manage placeholder behavior
        self.name_entry.bind("<FocusIn>", self.onFocusIn)
        self.price_entry.bind("<FocusIn>", self.onFocusIn)
        self.weight_entry.bind("<FocusIn>", self.onFocusIn)

        self.name_entry.bind("<FocusOut>", self.onFocusOut)
        self.price_entry.bind("<FocusOut>", self.onFocusOut)
        self.weight_entry.bind("<FocusOut>", self.onFocusOut)

        # Position entry fields in grid
        grid(widget=self.name_entry, row=1, column=1)
        grid(widget=self.price_entry, row=2, column=1)
        grid(widget=self.weight_entry, row=3, column=1)

        # Create action buttons
        self.add_btn = button(self.master, text="Add the fruit to the basket", command=self.insertFruit)
        self.back_btn = button(self.master, text="Back", command=self.back)
        self.clear_btn = button(self.master, text="Clear fruit entry infos", command=self.clearInfos)

        # Position buttons in grid
        grid(widget=self.add_btn, row=4, column=1, padx=5, pady=5)
        grid(widget=self.back_btn, row=5, column=0, padx=40, pady=5)
        grid(widget=self.clear_btn, row=5, column=1, padx=5, pady=5)
    
    def onFocusIn(self, event):
        """Clear placeholder text when entry gains focus"""
        for i in [self.name_entry, self.price_entry, self.weight_entry]:
            if i.get() == self.placeholderMessage:
                i.delete(0, END)
                i.configure(fg=self.color)

    def onFocusOut(self, event):
        """Restore placeholder text when entry loses focus and is empty"""
        for i in [self.name_entry, self.price_entry, self.weight_entry]:
            if not i.get():
                i.insert(0, self.placeholderMessage)
                i.configure(fg=self.color)

    def back(self):
        """Return to the previous window."""
        self.relative.deiconify()
        self.master.destroy()
        
    def getBasketCapacity(self) -> float:
        """Get the capacity of the selected basket."""
        self.capacity = float(baskets.getCapacity(self.selected_basket))
        return self.capacity
        
    def getFruitsSum(self) -> float:
        """Get the total weight of fruits in the selected basket."""
        self.fruitSum = baskets.getNet(self.selected_basket)
        return self.fruitSum
        
    def insertFruit(self):
        """Add a fruit to the selected basket if possible."""
        try:
            fruit_data = self.getFruit()
            if fruit_data and any(fruit_data):
                self.fruit = Frutto(fruit_data)
            else:
                self.fruit = Frutto()  # Create random fruit if fields are empty
                
            if self.getBasketName() and self.isFull():
                Warning("3").showWarning()  # Basket is full
            else:
                self.last_fruit_label.config(text=f"Last added fruit: {self.fruit.getName()}")
                self.addToBasket()
        except ValueError:
            Warning("2").showWarning()  # Invalid input values

    def dropdownHandler(self, event=None):
        """Handle basket selection from dropdown."""
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem

    def addToBasket(self):
        """Add the current fruit to the selected basket."""
        baskets.addFruit(self.selected_basket, self.fruit)
    
    def clearInfos(self):
        """Clear all input fields."""
        for field in [self.name_entry, self.price_entry, self.weight_entry]:
            field.delete(0, END)

    def getBasketName(self) -> str:
        """Get the name of the selected basket."""
        return baskets.getBasket(self.selected_basket)
    
    def getSum(self) -> float:
        """Calculate total weight after adding the new fruit."""
        return self.getFruitsSum() + self.fruit.getWeight()

    def getFruit(self) -> list:
        """Get fruit details from input fields, filtering out placeholder text."""
        name = self.name_entry.get().lower()
        price = self.price_entry.get()
        weight = self.weight_entry.get()
        fruit = [name, price, weight]
        if self.placeholderMessage in fruit:
            return ["", "", ""]  # Return empty values if placeholder is present
        return fruit
    
    def isFull(self) -> bool:
        """Check if the basket can accommodate more fruits."""
        if float(baskets.getCapacity(self.selected_basket)) > 0.0:
            if self.getSum() <= self.getBasketCapacity():
                return False
        return True


class RemoveFruit:
    """Class for removing fruits from baskets through a GUI interface."""
    def __init__(self, master, relative):
        """Initialize the fruit removal window."""
        self.master = master
        self.master.title("Fruit manager")
        self.relative = relative
        self.selected_basket = ""

        # Create read-only text area for displaying basket contents
        self.text = Text(self.master, bg="#f0f0f0", width=40, height=10)
        self.text.config(state="disabled")  # Make read-only initially

        # Create label and entry for fruit removal
        self.removingName = name(self.master, text="Insert here the removing fruit's name:")
        self.removingEntry = entry(self.master)

        # Create action buttons
        self.backBtn = button(self.master, text="Back", command=self.back)
        self.rmvBtn = button(self.master, text="Remove the chosen fruit", command=self.rmvOne)
        self.rmvAllBtn = button(self.master, text="Remove all chosen fruits", command=self.rmvAll)

        # Configure grid columns to expand properly
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

        # Position widgets in grid
        grid(widget=self.backBtn, row=0, column=0, sticky="ew")
        grid(widget=self.text, row=1, column=0, sticky="nsew")
        grid(widget=self.rmvBtn, row=2, column=0, sticky="ew")
        grid(widget=self.rmvAllBtn, row=2, column=1, sticky="ew")
        grid(widget=self.removingName, row=3, column=0, sticky="ew")
        grid(widget=self.removingEntry, row=3, column=1, sticky="ew")

        # Create dropdown for basket selection
        self.dropdown = DropDown(self.master, VALUES, self.dropdownHandler)
        self.dropdown.combobox.grid(row=0, column=1, padx=15)

    def back(self):
        """Return to the previous window."""
        self.relative.deiconify()
        self.master.destroy()

    def rmvOne(self):
        """Remove one instance of the specified fruit from the basket."""
        try:
            fruit_name = self.getRemovingEntry()
            if fruit_name not in baskets.getFruitsName(self.selected_basket):
                raise TypeError("Fruit not found")
                
            if self.getBasketName():
                if fruit_name:
                    baskets.rmvOne(self.selected_basket, fruit_name)
                    self.getFruitsName()  # Refresh the display
        except (TypeError, KeyError):
            Warning("4", self.getRemovingEntry()).showWarning()  # Fruit not found warning

    def rmvAll(self):
        """Remove all instances of the specified fruit from the basket."""
        try:
            fruit_name = self.getRemovingEntry()
            if fruit_name not in baskets.getFruitsName(self.selected_basket):
                raise TypeError("Fruit not found")
                
            if self.getBasketName():
                if fruit_name:
                    baskets.rmvAll(self.selected_basket, fruit_name)
                    self.getFruitsName()  # Refresh the display
        except (TypeError, KeyError):
            Warning("4", self.getRemovingEntry()).showWarning()  # Fruit not found warning

    def dropdownHandler(self, event=None):
        """Handle basket selection from dropdown."""
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem
            self.getFruitsName()  # Update display with fruits in selected basket

    def getBasketName(self) -> str:
        """Get the name of the selected basket."""
        return baskets.getBasket(self.selected_basket)
    
    def update_text_display(self, content):
        """Update the text area with new content."""
        self.text.config(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert(END, content)
        self.text.config(state="disabled")
    
    def getFruitsName(self):
        """Display names of fruits in the selected basket."""
        if self.getBasketName():
            fruits_names = baskets.getFruitsName(self.selected_basket)
            self.update_text_display(str(fruits_names))

    def getRemovingEntry(self) -> str:
        """Get the name of the fruit to remove from the entry field."""
        return self.removingEntry.get().lower()