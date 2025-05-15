import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Connect to database
conn = sqlite3.connect("scm.db")
cursor = conn.cursor()

# Create orders table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        order_date TEXT
    )
""")
conn.commit()

# Submit order
def submit_order():
    cursor.execute("INSERT INTO orders VALUES (?, ?, ?, ?)",
                   (order_id.get(), product.get(), quantity.get(), order_date.get()))
    conn.commit()
    messagebox.showinfo("Order Submitted", "Order recorded successfully.")

# Tkinter window
root = tk.Tk()
root.title("Order Form")
root.geometry("400x300")

tk.Label(root, text="Order ID").pack(pady=5)
order_id = tk.Entry(root)
order_id.pack(pady=5)

tk.Label(root, text="Product").pack(pady=5)
product = tk.Entry(root)
product.pack(pady=5)

tk.Label(root, text="Quantity").pack(pady=5)
quantity = tk.Entry(root)
quantity.pack(pady=5)

tk.Label(root, text="Order Date (YYYY-MM-DD)").pack(pady=5)
order_date = tk.Entry(root)
order_date.pack(pady=5)

tk.Button(root, text="Submit Order", command=submit_order).pack(pady=20)

root.mainloop()
