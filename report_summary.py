import tkinter as tk
import sqlite3

# Connect to database
conn = sqlite3.connect("scm.db")
cursor = conn.cursor()

# Count records
cursor.execute("SELECT COUNT(*) FROM suppliers")
supplier_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM inventory")
inventory_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM orders")
order_count = cursor.fetchone()[0]

# Estimate value
cursor.execute("SELECT SUM(quantity * price) FROM inventory")
total_value = cursor.fetchone()[0] or 0

# GUI
root = tk.Tk()
root.title("Reports Summary")
root.geometry("400x250")

tk.Label(root, text="Supply Chain Report Summary", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text=f"Total Suppliers: {supplier_count}", font=("Arial", 12)).pack(pady=5)
tk.Label(root, text=f"Total Inventory Items: {inventory_count}", font=("Arial", 12)).pack(pady=5)
tk.Label(root, text=f"Total Orders: {order_count}", font=("Arial", 12)).pack(pady=5)
tk.Label(root, text=f"Estimated Total Inventory Value (₹): {total_value}", font=("Arial", 12)).pack(pady=5)

root.mainloop()
