import tkinter as tk
from tkinter import messagebox

class Product:
    def __init__(self, name, code, price, is_weight=False):
        self.name = name
        self.code = code
        self.price = price
        self.is_weight = is_weight

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class CartGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart in Python  --  MS Devs")

        self.cart = Cart()
        self.products = {
            "Shampoo": Product("Shampoo", "m77", 5),
            "Rice": Product("Rice", "w88", 310),
            "Sugar": Product("Sugar", "w19", 155),
            "Bread": Product("Bread", "m20", 30),
            "Butter": Product("Butter", "m22", 100),
            "Flour": Product("Flour", "w55", 120),
            "Milk": Product("Milk", "w90", 100)
        }

        self.selected_product = tk.StringVar()
        self.selected_product.set("Shampoo")
        self.quantity_var = tk.IntVar()

        self.product_label = tk.Label(root, text="Select Product:")
        self.product_label.pack()

        self.product_dropdown = tk.OptionMenu(root, self.selected_product, *self.products.keys())
        self.product_dropdown.pack()

        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(root, textvariable=self.quantity_var)
        self.quantity_entry.pack()

        self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove from Cart", command=self.remove_from_cart)
        self.remove_button.pack()

        self.update_button = tk.Button(root, text="Update Cart", command=self.update_cart_display)
        self.update_button.pack()
        
        self.cart_text = tk.Text(root, height=10, width=40)
        self.cart_text.pack()

    def add_to_cart(self):
        product_name = self.selected_product.get()
        quantity = self.quantity_var.get()
        
        if product_name in self.products:
            product = self.products[product_name]
            if product.is_weight:
                weight = float(self.quantity_var.get())
                self.cart.add_item(product, weight=weight)
            else:
                self.cart.add_item(product, quantity=quantity)
            messagebox.showinfo("Added to Cart", f"{quantity} {product_name}(s) added to the cart.")
        else:
            messagebox.showerror("Error", "Invalid product selection.")
        self.update_cart_display()
        
    def remove_from_cart(self):
        product_name = self.selected_product.get()
        
        if product_name in self.products:
            product = self.products[product_name]
            self.cart.remove_item(product)
            messagebox.showinfo("Removed from Cart", f"{product_name} removed from the cart.")
        else:
            messagebox.showerror("Error", "Invalid product selection.")
        self.update_cart_display()
        
    def update_cart_display(self):
        self.cart_text.delete(1.0, tk.END)  # Clear the existing content
        cart_summary = self.cart.get_cart_summary()
        self.cart_text.insert(tk.END, cart_summary)

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=None, weight=None):
        for item in self.items:
            if item.product.code == product.code:
                if product.is_weight:
                    item.quantity += weight
                else:
                    item.quantity += quantity
                return
        if product.is_weight:
            self.items.append(CartItem(product, weight))
        else:
            self.items.append(CartItem(product, quantity))

    # (existing Cart methods)
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        for item in self.items:
            if item.product.code == product.code:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product):
        self.items = [item for item in self.items if item.product.code != product.code]

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        return total

    def display_cart(self):
        print("Your Cart Data:")
        for item in self.items:
            print(f"Product: {item.product.name}")
            print(f"Code: {item.product.code}")
            print(f"Price: Rs.{item.product.price:.2f}")
            print(f"Quantity: {item.quantity}")
            print(f"Subtotal: Rs.{item.product.price * item.quantity:.2f}\n")
        print("Total Payable Amount is Rs.")
        print(f"Total: Rs.{self.calculate_total():.2f}")


    def get_cart_summary(self):
        cart_summary = "Your Cart:\n\n"
        for item in self.items:
            cart_summary += f"Product: {item.product.name}\n"
            cart_summary += f"Code: {item.product.code}\n"
            cart_summary += f"Price: Rs.{item.product.price:.2f}\n"
            if item.product.is_weight:
                cart_summary += f"Weight: {item.quantity:.2f} kg\n"
            else:
                cart_summary += f"Quantity: {item.quantity}\n"
            cart_summary += f"Subtotal: Rs.{item.product.price * item.quantity:.2f}\n\n"
        cart_summary += f"Total Payable Amount: Rs.{self.calculate_total():.2f}\n"
        return cart_summary
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CartGUI(root)
    root.mainloop()
