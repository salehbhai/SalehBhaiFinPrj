"""
Author:  Saleh Bhai
Date written: 07/27/2024
Assignment:   Final Project GUI app
Description:GUI application to generate two windows for school supply cost calculator.  One to enter the item counts and the other to display the cost per items along
            with the total cost of all items. This application has taken following features into considerations when designed.
            Implementing a modular approach in your application.
            Consistent clear navigation throughout the GUI application.  Allows user to enter values in one window then go the second and continue operation.  Clear path to terminate
            the appliation with a end button.
            Use two images, one to indicate the supply quantity window and the other to indicate a cost window with a dollar image.
            Has around 10 labels.
            Include three buttons. 
            Includes three call backs one associated with each button. 
            Implement secure coding best practices, by validating the input supply quantity values to be integer values of zero or positive numbers.
"""

import tkinter as tk
from tkinter import messagebox

class SupplyEntryWindow:
    """
    A class to create a GUI window for entering quantities of school supplies.

    This window allows users to input the quantities of pencils, pens, erasers, and notebooks.
    It also displays an image of school supplies.    
    - root (tk.Tk): The main window for the application.
    Input/Output - > entry field, buttons, image etc
    - Entry box for the number of pencils.
    - Entry box for the number of pens.
    - Entry box for the number of erasers.
    - Entry box for the number of notebooks.
    - Label to display the Count.png image.
    """

    def __init__(self, master):
        """
        Initializes the SupplyEntryWindow.
        """
        self.root = master
        self.root.title("Supply Entry")

        # Creating labels and entry fields for each supply item
        tk.Label(self.root, text="Pencils:").grid(row=0, column=0)
        self.entry_pencils = tk.Entry(self.root)
        self.entry_pencils.grid(row=0, column=1)

        tk.Label(self.root, text="Pens:").grid(row=1, column=0)
        self.entry_pens = tk.Entry(self.root)
        self.entry_pens.grid(row=1, column=1)

        tk.Label(self.root, text="Erasers:").grid(row=2, column=0)
        self.entry_erasers = tk.Entry(self.root)
        self.entry_erasers.grid(row=2, column=1)

        tk.Label(self.root, text="Notebooks:").grid(row=3, column=0)
        self.entry_notebooks = tk.Entry(self.root)
        self.entry_notebooks.grid(row=3, column=1)

        # Displaying the Count.png image at the bottom
        self.image_label = tk.Label(self.root)
        self.image_label.grid(row=4, columnspan=2)
        self.load_image("Count.png")

        # button to end the program
        self.end_button = tk.Button(self.root, text="End", command=self.end_program)
        self.end_button.grid(row=7, columnspan=2)        

    def load_image(self, image_path):
        """
        Loads and displays an image to indicate counting symbol

        Input:
        The path to the image file to be displayed.
        """
        try:
            # Load the image and display it in the label
            self.image = tk.PhotoImage(file=image_path)
            self.image_label.config(image=self.image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

            
    def end_program(self):
        """
        Ends the program by closing the root window.
        This method is called when the user clicks the 'End' button.
        """        
        supply_entry_window.root.destroy()            

class CostWindow:
    """
    A class to create a GUI window for calculating the cost of school supplies.

    This window allows users to view the costs of each supply item and the total cost.
    It includes a button to apply a discount and a button to calculate costs.
    
    Input/Output - > entry field, buttons, image etc
    - Entry widget for the cost of pencils.
    - Entry widget for the cost of pens.
    - Entry widget for the cost of erasers.
    - Entry widget for the cost of notebooks.
    - Entry widget for the total cost.
    - Label to display the Dollar.png image.
    """

    def __init__(self, master):
        """
        Initializes the CostWindow.
        - The parent window to which this window belongs.
        """
        self.root = master 
        self.root.title("Cost Calculation")

        # Creating entry fields for the cost of each supply item
        # cost for pencil
        tk.Label(self.root, text="Cost of Pencils:").grid(row=0, column=0)
        self.entry_cost_pencils = tk.Entry(self.root)
        self.entry_cost_pencils.grid(row=0, column=1)

        # cost for pens
        tk.Label(self.root, text="Cost of Pens:").grid(row=1, column=0)
        self.entry_cost_pens = tk.Entry(self.root)
        self.entry_cost_pens.grid(row=1, column=1)

        # cost for erasers
        tk.Label(self.root, text="Cost of Erasers:").grid(row=2, column=0)
        self.entry_cost_erasers = tk.Entry(self.root)
        self.entry_cost_erasers.grid(row=2, column=1)

        # cost for notebooks
        tk.Label(self.root, text="Cost of Notebooks:").grid(row=3, column=0)
        self.entry_cost_notebooks = tk.Entry(self.root)
        self.entry_cost_notebooks.grid(row=3, column=1)

        tk.Label(self.root, text="Total Cost:").grid(row=4, column=0)
        self.entry_total_cost = tk.Entry(self.root)
        self.entry_total_cost.grid(row=4, column=1)

        # Displaying the Dollar.png image
        self.image_label = tk.Label(self.root)
        self.image_label.grid(row=5, columnspan=2)
        self.load_image("Dollar.png")

        # Creating buttons for calculating cost and applying discount
        self.calculate_button = tk.Button(self.root, text="Calculate Cost", command=self.calculate_cost)
        self.calculate_button.grid(row=6, column=0)

        self.discount_button = tk.Button(self.root, text="Apply 10% Discount", command=self.apply_discount)
        self.discount_button.grid(row=6, column=1)


    def load_image(self, image_path):
        """
        Loads and displays an image in the window.

        Parameters:
        - image_path (str): The path to the image file to be displayed.
        """
        try:
            # Load the image and display it in the label
            self.image = tk.PhotoImage(file=image_path)
            self.image_label.config(image=self.image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def calculate_cost(self):
        """
        Calculates the cost of each supply item based on user input.

        This method retrieves the quantities from the SupplyEntryWindow, calculates
        the costs based on predefined prices, and displays the results in the entry fields.

        
        Secure coding as taught in class.  Checking for valid input.
        - ValueError: If the input values are not valid integers that is are floating values or negative quantities of supplies.
        """
        try:
            # Retrieve quantities from the SupplyEntryWindow
            pencils_qty = int(supply_entry_window.entry_pencils.get())
            pens_qty = int(supply_entry_window.entry_pens.get())
            erasers_qty = int(supply_entry_window.entry_erasers.get())
            notebooks_qty = int(supply_entry_window.entry_notebooks.get())

            if pencils_qty < 0 or pens_qty < 0 or erasers_qty < 0 or notebooks_qty < 0:
                raise ValueError("Please enter a 0 or positive quantity")                 

            # Define the prices for each supply item
            price_pencil = 1
            price_pen = 3
            price_eraser = 1
            price_notebook = 5

            # Calculate costs for each item
            cost_pencils = pencils_qty * price_pencil
            cost_pens = pens_qty * price_pen
            cost_erasers = erasers_qty * price_eraser
            cost_notebooks = notebooks_qty * price_notebook

            # Calculate total cost
            total_cost = cost_pencils + cost_pens + cost_erasers + cost_notebooks

            # Display costs in the respective entry fields
            self.entry_cost_pencils.delete(0, tk.END)
            self.entry_cost_pencils.insert(0, f"${cost_pencils:.2f}")

            self.entry_cost_pens.delete(0, tk.END)
            self.entry_cost_pens.insert(0, f"${cost_pens:.2f}")

            self.entry_cost_erasers.delete(0, tk.END)
            self.entry_cost_erasers.insert(0, f"${cost_erasers:.2f}")

            self.entry_cost_notebooks.delete(0, tk.END)
            self.entry_cost_notebooks.insert(0, f"${cost_notebooks:.2f}")

            self.entry_total_cost.delete(0, tk.END)
            self.entry_total_cost.insert(0, f"${total_cost:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integer quantities.")

    def apply_discount(self):
        """
        Applies a 10% discount to the total cost of each supply item.

        This method retrieves the current costs from the entry fields, then applying the discount,
        and updates the displayed costs likewise.

        
        Error if the current costs are not valid float values.
        """
        try:
            # Retrieve current costs from the entry fields
            cost_pencils = float(self.entry_cost_pencils.get().replace('$', ''))
            cost_pens = float(self.entry_cost_pens.get().replace('$', ''))
            cost_erasers = float(self.entry_cost_erasers.get().replace('$', ''))
            cost_notebooks = float(self.entry_cost_notebooks.get().replace('$', ''))

            # Calculate discounted costs
            discounted_pencils = cost_pencils * 0.9
            discounted_pens = cost_pens * 0.9
            discounted_erasers = cost_erasers * 0.9
            discounted_notebooks = cost_notebooks * 0.9

            # Update the entry fields with the discounted costs
            self.entry_cost_pencils.delete(0, tk.END)
            self.entry_cost_pencils.insert(0, f"${discounted_pencils:.2f}")

            self.entry_cost_pens.delete(0, tk.END)
            self.entry_cost_pens.insert(0, f"${discounted_pens:.2f}")

            self.entry_cost_erasers.delete(0, tk.END)
            self.entry_cost_erasers.insert(0, f"${discounted_erasers:.2f}")

            self.entry_cost_notebooks.delete(0, tk.END)
            self.entry_cost_notebooks.insert(0, f"${discounted_notebooks:.2f}")

            # Recalculate total cost after discount
            total_cost = discounted_pencils + discounted_pens + discounted_erasers + discounted_notebooks
            self.entry_total_cost.delete(0, tk.END)
            self.entry_total_cost.insert(0, f"${total_cost:.2f}")

        except ValueError:            
            messagebox.showerror("Input Error", "Please ensure all costs are valid numbers.")


# Main application logic
if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()

    # Create the Supply Entry window
    supply_entry_window = SupplyEntryWindow(root) 

    # Create the Cost Calculation window
    # This creates a new top-level window (a separate window that is associated with the main window).
    cost_window = tk.Toplevel(root) 
    cost_calculation_window = CostWindow(cost_window) 

    # Start the Tkinter event loop
    root.mainloop()
