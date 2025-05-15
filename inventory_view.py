import tkinter as tk
from tkinter import ttk
import sqlite3

# Connect to database
conn = sqlite3.connect("scm.db")
cursor = conn.cursor()

# Create inventory table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        product_id TEXT PRIMARY KEY,
        name TEXT,
        quantity INTEGER,
        price REAL
    )
""")
conn.commit()

# Insert some sample products (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM inventory")
if cursor.fetchone()[0] == 0:
    sample_data = [
        ("P001", "Laptop", 15, 55000),
        ("P002", "Mouse", 50, 500),
        ("P003", "Keyboard", 30, 1500)
    ]
    cursor.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?)", sample_data)
    conn.commit()

# Tkinter GUI
root = tk.Tk()
root.title("Inventory Table View")
root.geometry("600x300")

# Create Treeview for inventory
tree = ttk.Treeview(root, columns=("Product ID", "Name", "Quantity", "Price"), show="headings")
tree.heading("Product ID", text="Product ID")
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")

# Fetch and insert data
cursor.execute("SELECT * FROM inventory")
for row in cursor.fetchall():
    tree.insert("", tk.END, values=row)

tree.pack(expand=True, fill="both")
root.mainloop()
