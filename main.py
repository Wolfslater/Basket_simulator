# Version 2.11.6 17/05/2025

from fruitManager import AddFruit, RemoveFruit
from tkinter import Toplevel, Tk
from tkinter import Text, END
from widgets import (DropDown, VALUES, baskets, grid, button)

class BasketInfos:
    """
    Main class for basket management interface.
    """
    def __init__(self, master):
        """
        Initialize the main basket management window.
        """
        self.master = master
        self.master.title("Basket manager")
        self.selected_basket = ""

        self.basket_content = Text(self.master, bg="#f0f0f0")
        self.basket_content.config(state="disabled")  # Make read-only initially

        self.backBtn = button(self.master, text="exit", command=self.exit)
        self.addkBtn = button(self.master, text="Open fruit adder", command=self.addFruit)
        self.rmvBtn = button(self.master, text="open fruit remover", command=self.rmvFruit)
        self.clearBtn = button(self.master, text="Empty selected basket", command=self.clear)
        self.weightBtn = button(self.master, text="Display basket weight infos", command=self.displayBasketWeight)
        self.basketBtn = button(self.master, text="Display basket", command=self.displayBasket)
        self.pricetBtn = button(self.master, text="Display basket's price", command=self.displayPrice)
        
        self.dropdown = DropDown(master, VALUES, self.dropdownHandler, overlay=None)
        grid(widget=self.dropdown.combobox, row=0, column=7, sticky="ew")

        for i in range(7):
            self.master.grid_columnconfigure(i, weight=1)

        grid(widget=self.basket_content, row=1, column=0, columnspan=7, sticky="nsew")
        grid(widget=self.backBtn, row=0, column=0, sticky="ew")
        grid(widget=self.addkBtn, row=0, column=1, sticky="ew")
        grid(widget=self.rmvBtn, row=0, column=2, sticky="ew")
        grid(widget=self.weightBtn, row=0, column=3, sticky="ew")
        grid(widget=self.basketBtn, row=0, column=4, sticky="ew")
        grid(widget=self.pricetBtn, row=0, column=5, sticky="ew")
        grid(widget=self.clearBtn, row=0, column=6, sticky="ew")

    def exit(self):
        """Exit the application."""
        exit()

    def clear(self):
        """Clear the selected basket."""
        basket = self.getBasketName()
        if basket is None:
            self.update_text_display("Basket's already empty")
        elif basket:
            baskets.clear(self.selected_basket)
            self.update_text_display("Basket cleared successfully")

    def update_text_display(self, content):
        """
        Update the text area with new content.
        """
        self.basket_content.config(state="normal")
        self.basket_content.delete("1.0", "end")
        self.basket_content.insert(END, content)
        self.basket_content.config(state="disabled")
    
    def getBasketName(self):
        """
        Get the selected basket object.
        """
        return baskets.getBasket(self.selected_basket)
    
    def displayBasketWeight(self):
        """Display weight details of the selected basket."""
        basket = self.getBasketName()
        if basket:
            capacity = baskets.getCapacity(self.selected_basket)
            gross = basket.getGrossWeight()
            tare = basket.getTare()
            net = basket.getNet()
            weight_info = (
                f"Basket's total capacity is: {capacity}gr\n"
                f"Basket's tare is: {tare}gr\n"
                f"Basket's net is: {net}gr\n"
                f"Basket's gross is: {gross}gr"
            )
            self.update_text_display(weight_info)
    
    def displayPrice(self):
        """Display the total price of items in the selected basket."""
        basket = self.getBasketName()
        if basket: 
            self.price = basket.getPrices()
            self.update_text_display(f"Basket's total price is: {self.price}€")
        
    def displayBasket(self):
        """Display all items in the selected basket."""
        basket = self.getBasketName()
        if basket: 
            self.update_text_display(str(basket))
    
    def dropdownHandler(self, event=None):
        """
        Handle basket selection from dropdown.
        """
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem
    
    def addFruit(self):
        """Open the add fruit window."""
        self.master.withdraw()  # Hide main window
        self.newWindow = Toplevel(self.master)
        AddFruit(self.newWindow, self.master)

    def rmvFruit(self):
        """Open the remove fruit window."""
        self.master.withdraw()  # Hide main window
        self.newWindow = Toplevel(self.master)
        RemoveFruit(self.newWindow, self.master)


if __name__ == '__main__':
    root = Tk()
    BasketInfos(root)
    root.mainloop()