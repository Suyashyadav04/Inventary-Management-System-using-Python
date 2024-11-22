import tkinter as tk
from tkinter import ttk, messagebox
import json

# User credentials (simple authentication)
USER_CREDENTIALS = {"admin": "password123"}

# Inventory data storage (in memory for simplicity)
inventory_data = {}

# Authentication window
def login_window():
    login_screen = tk.Tk()
    login_screen.title("Inventory System Login")
    login_screen.geometry("300x150")

    tk.Label(login_screen, text="Username").pack(pady=5)
    username_entry = tk.Entry(login_screen)
    username_entry.pack(pady=5)

    tk.Label(login_screen, text="Password").pack(pady=5)
    password_entry = tk.Entry(login_screen, show="*")
    password_entry.pack(pady=5)

    def authenticate():
        username = username_entry.get()
        password = password_entry.get()
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            login_screen.destroy()
            main_inventory_window()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(login_screen, text="Login", command=authenticate).pack(pady=10)
    login_screen.mainloop()

# Main Inventory System Window
def main_inventory_window():
    def load_data():
        try:
            with open("inventory_data.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data():
        with open("inventory_data.json", "w") as file:
            json.dump(inventory_data, file, indent=4)

    def add_product():
        product_id = entry_product_id.get()
        name = entry_product_name.get()
        quantity = entry_product_quantity.get()
        price = entry_product_price.get()

        if not product_id or not name or not quantity or not price:
            messagebox.showwarning("Validation Error", "All fields are required!")
            return

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            messagebox.showwarning("Validation Error", "Quantity must be an integer and Price must be a number.")
            return

        if product_id in inventory_data:
            messagebox.showerror("Error", "Product ID already exists!")
            return

        inventory_data[product_id] = {"name": name, "quantity": quantity, "price": price}
        save_data()
        refresh_inventory_list()
        clear_entries()
        messagebox.showinfo("Success", "Product added successfully!")

    def edit_product():
        selected = inventory_list.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "No product selected!")
            return

        product_id = selected[0]
        name = entry_product_name.get()
        quantity = entry_product_quantity.get()
        price = entry_product_price.get()

        if not name or not quantity or not price:
            messagebox.showwarning("Validation Error", "All fields are required!")
            return

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            messagebox.showwarning("Validation Error", "Quantity must be an integer and Price must be a number.")
            return

        inventory_data[product_id] = {"name": name, "quantity": quantity, "price": price}
        save_data()
        refresh_inventory_list()
        clear_entries()
        messagebox.showinfo("Success", "Product updated successfully!")

    def delete_product():
        selected = inventory_list.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "No product selected!")
            return

        product_id = selected[0]
        del inventory_data[product_id]
        save_data()
        refresh_inventory_list()
        clear_entries()
        messagebox.showinfo("Success", "Product deleted successfully!")

    def low_stock_alert():
        alert_message = "Low Stock Products:\n\n"
        low_stock = False
        for product_id, product in inventory_data.items():
            if product["quantity"] < 5:
                low_stock = True
                alert_message += f"ID: {product_id}, Name: {product['name']}, Quantity: {product['quantity']}\n"
        if low_stock:
            messagebox.showinfo("Low Stock Alert", alert_message)
        else:
            messagebox.showinfo("Low Stock Alert", "No products with low stock levels.")

    def clear_entries():
        entry_product_id.delete(0, tk.END)
        entry_product_name.delete(0, tk.END)
        entry_product_quantity.delete(0, tk.END)
        entry_product_price.delete(0, tk.END)

    def refresh_inventory_list():
        inventory_list.delete(*inventory_list.get_children())
        for product_id, product in inventory_data.items():
            inventory_list.insert("", tk.END, iid=product_id, values=(product_id, product["name"], product["quantity"], product["price"]))

    def select_product(event):
        selected = inventory_list.selection()
        if selected:
            product_id = selected[0]
            product = inventory_data[product_id]
            entry_product_id.delete(0, tk.END)
            entry_product_id.insert(0, product_id)
            entry_product_name.delete(0, tk.END)
            entry_product_name.insert(0, product["name"])
            entry_product_quantity.delete(0, tk.END)
            entry_product_quantity.insert(0, product["quantity"])
            entry_product_price.delete(0, tk.END)
            entry_product_price.insert(0, product["price"])

    inventory_data.update(load_data())

    # Main Window
    window = tk.Tk()
    window.title("Inventory Management System")
    window.geometry("800x500")

    # Product Form
    frame_form = tk.Frame(window)
    frame_form.pack(pady=10)

    tk.Label(frame_form, text="Product ID").grid(row=0, column=0, padx=5, pady=5)
    entry_product_id = tk.Entry(frame_form)
    entry_product_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Name").grid(row=1, column=0, padx=5, pady=5)
    entry_product_name = tk.Entry(frame_form)
    entry_product_name.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Quantity").grid(row=2, column=0, padx=5, pady=5)
    entry_product_quantity = tk.Entry(frame_form)
    entry_product_quantity.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Price").grid(row=3, column=0, padx=5, pady=5)
    entry_product_price = tk.Entry(frame_form)
    entry_product_price.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(frame_form, text="Add Product", command=add_product).grid(row=4, column=0, padx=5, pady=5)
    tk.Button(frame_form, text="Edit Product", command=edit_product).grid(row=4, column=1, padx=5, pady=5)
    tk.Button(frame_form, text="Delete Product", command=delete_product).grid(row=4, column=2, padx=5, pady=5)
    tk.Button(frame_form, text="Low Stock Alert", command=low_stock_alert).grid(row=4, column=3, padx=5, pady=5)

    # Inventory List
    inventory_list = ttk.Treeview(window, columns=("ID", "Name", "Quantity", "Price"), show="headings")
    inventory_list.heading("ID", text="Product ID")
    inventory_list.heading("Name", text="Name")
    inventory_list.heading("Quantity", text="Quantity")
    inventory_list.heading("Price", text="Price")
    inventory_list.bind("<<TreeviewSelect>>", select_product)
    inventory_list.pack(fill="both", expand=True, padx=10, pady=10)

    refresh_inventory_list()
    window.mainloop()

# Start the program
if __name__ == "__main__":
    login_window()
