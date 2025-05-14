# Version 1.11.5 12/05/2025

from fruitManager import AddFruit, RemoveFruit
from tkinter import Toplevel, Tk
from tkinter import Text, END
from widgets import (DropDown, VALUES, baskets, grid, button)

class BasketInfos:
    def __init__(self, master):
        # Initialize main window and variables
        self.master = master
        # self.relative = relative
        self.master.title("Basket manager")
        self.selected_basket = ""

        # Text area for basket details
        self.basket_content = Text(self.master, bg="#f0f0f0")

        # Buttons for various actions
        self.backBtn = button(self.master, text="exit", command=self.exit)
        self.addkBtn = button(self.master, text="Open fruit adder", command=self.addFruit)
        self.rmvBtn = button(self.master, text="open fruit remover", command=self.rmvFruit)
        self.clearBtn = button(self.master, text="Empty selected basket", command=self.clear)
        self.weightBtn = button(self.master, text="Display basket weight infos", command=self.displayBasketWeight)
        self.basketBtn = button(self.master, text="Display basket", command=self.displayBasket)
        self.pricetBtn = button(self.master, text="Display basket's price", command=self.displayPrice)
        
        # Dropdown for basket selection
        self.dropdown = DropDown(master, VALUES, self.dropdownHandler, overlay=None)
        grid(widget=self.dropdown.combobox, row=0, column=7, sticky="ew")

        # Arrange components in a grid layout
        self.master.grid_columnconfigure(0, weight=1)  # Back button column 
        self.master.grid_columnconfigure(1, weight=1)  # Weight infos column
        self.master.grid_columnconfigure(2, weight=1)  # Basket display column
        self.master.grid_columnconfigure(3, weight=1)  # Price column
        self.master.grid_columnconfigure(4, weight=1)  # Clear column
        self.master.grid_columnconfigure(5, weight=1)  # Clear column
        self.master.grid_columnconfigure(6, weight=1)  # Dropdown column

        # Place components in the grid
        grid(widget=self.basket_content, row=1, column=0, columnspan=7, sticky="nsew")
        grid(widget=self.backBtn, row=0, column=0, sticky="ew")
        grid(widget=self.addkBtn, row=0, column=1, sticky="ew")
        grid(widget=self.rmvBtn, row=0, column=2, sticky="ew")
        grid(widget=self.weightBtn, row=0, column=3, sticky="ew")
        grid(widget=self.basketBtn, row=0, column=4, sticky="ew")
        grid(widget=self.pricetBtn, row=0, column=5, sticky="ew")
        grid(widget=self.clearBtn, row=0, column=6, sticky="ew")

    def exit(self):
        exit()

    def clear(self):
        if self.getBasketName() is None:
            self.update_text_display("Basket's already empty")
        elif self.getBasketName():
            baskets.clear(self.selected_basket)

    def update_text_display(self, content):
        # Update text area with provided content
        self.basket_content.config(state="normal")
        self.basket_content.delete("1.0", "end")
        self.basket_content.insert(END, content)
        self.basket_content.config(state="disabled")
    
    def getBasketName(self) -> str:
        # Retrieve the selected basket
        return baskets.getBasket(self.selected_basket)
    
    def displayBasketWeight(self):
        # Display weight details of the selected basket
        if self.getBasketName():
            capacity = baskets.getCapacity(self.selected_basket)
            gross = self.getBasketName().getGrossWeight()
            tare = self.getBasketName().getTare()
            net = self.getBasketName().getNet()
            weight = f"Basket's total capacity is: {capacity}gr \
                \nBasket's tare is: {tare}gr \
                \nBasket's net is: {net}gr \
                \nBasket's gross is: {gross}gr"
            self.update_text_display(weight)
    
    def displayPrice(self):
        # Display price of the selected basket
        if self.getBasketName(): 
            self.price = self.getBasketName().getPrice()
            self.update_text_display(f"Basket's total price is: {self.price}€")
        
    def displayBasket(self):
        # Display content of the selected basket
        if self.getBasketName(): 
            self.update_text_display(str(self.getBasketName()))
    
    def dropdownHandler(self, event=None):
        # Handle dropdown selection changes
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem
    
    def addFruit(self):  # Open add fruit window
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        AddFruit(self.newWindow, self.master)

    def rmvFruit(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        RemoveFruit(self.newWindow, self.master)

if __name__ == '__main__':
    # Create the main application window (root window).
    root = Tk()
    # Instantiate the GUIManagement class, passing the root window as an argument.
    BasketInfos(root)
    # Start the Tkinter event loop to keep the application running and responsive.
    root.mainloop()