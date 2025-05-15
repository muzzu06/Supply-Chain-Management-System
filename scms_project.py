import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("scm.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS suppliers (id INTEGER PRIMARY KEY, name TEXT, contact TEXT)")
conn.commit()

# Add Supplier Functionality
def add_supplier():
    cursor.execute("INSERT INTO suppliers (name, contact) VALUES (?, ?)", (supplier_name.get(), supplier_contact.get()))
    conn.commit()
    messagebox.showinfo("Supplier Management", "Supplier Added Successfully")

# Main window setup
root = tk.Tk()
root.title("Supply Chain Management System")
root.geometry("500x300")

ttk.Label(root, text="Supplier Name:").pack(pady=5)
supplier_name = ttk.Entry(root)
supplier_name.pack(pady=5)

ttk.Label(root, text="Supplier Contact:").pack(pady=5)
supplier_contact = ttk.Entry(root)
supplier_contact.pack(pady=5)

ttk.Button(root, text="Add Supplier", command=add_supplier).pack(pady=20)

root.mainloop()
