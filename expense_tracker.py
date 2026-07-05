import tkinter as tk
from tkinter import ttk, messagebox
from openpyxl import Workbook, load_workbook
from datetime import datetime
import os

# ---------------- Excel Setup ---------------- #

year = datetime.now().strftime("%Y")
filename = f"Expenses-{year}.xlsx"

# Current month (Jan, Feb, Mar...)
month = datetime.now().strftime(f"%b-expenses")

if not os.path.exists(filename):
    wb = Workbook()

    # Rename the default sheet to the current month
    ws = wb.active
    ws.title = month

    ws.append([
        "Date",
        "Category",
        "Credit",
        "Debit",
        "Balance",
        "Daily Closing"
    ])

    wb.save(filename)

# ---------------- Save Function ---------------- #

def save_expense():

    category = category_var.get()

    try:
        amount = float(amount_entry.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount.")
        return

    today = datetime.now().strftime("%d-%b-%Y")

    wb = load_workbook(filename)

    month = datetime.now().strftime(f"%b-expenses")

    if month in wb.sheetnames:
        ws = wb[month]
    else:
        ws = wb.create_sheet(title=month)

        ws.append([
        "Date",
        "Category",
        "Credit",
        "Debit",
        "Balance",
        "Daily Closing"
        ])

    # Credit / Debit
    income_categories = ["Pest Control", "Balloon Decoration"]

    if category in income_categories:
        credit = amount
        debit = 0
    else:
        credit = 0
        debit = amount

    # -------- Balance Calculation -------- #

    if ws.max_row == 1:
        previous_balance = 0

    else:
        last_row = ws.max_row

        while last_row > 1 and ws.cell(last_row, 1).value is None:
            last_row -= 1

        if last_row == 1:
            previous_balance = 0
        else:
            last_date = ws.cell(last_row, 1).value

            if last_date == today:
                previous_balance = ws.cell(last_row, 5).value or 0
            else:
                ws.cell(last_row, 6).value = ws.cell(last_row, 5).value
                ws.append([None, None, None, None, None, None])
                previous_balance = 0

# Calculate today's balance
    balance = previous_balance + credit - debit

# Save today's transaction
    ws.append([
    today,
    category,
    credit,
    debit,
    balance,
    ""      # Final Balance column
])

    wb.save(filename)

    amount_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Transaction Saved Successfully")

# ---------------- Tkinter Window ---------------- #

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("350x300")
root.resizable(False, False)

# Category

tk.Label(root, text="Category").pack(pady=(15,5))

category_var = tk.StringVar()

category_box = ttk.Combobox(
    root,
    textvariable=category_var,
    values=[
        "Pest Control",
        "Balloon Decoration",
        "Food",
        "Travel",
        "Shopping",
        "Utilities",
        "Medical",
        "Entertainment",
        "Commission",
        "Fuel",
        "Gifts",
        "Others"
    ],
    state="readonly"
)

category_box.pack()
category_box.current(0)

# Amount

tk.Label(root, text="Amount").pack(pady=(15,5))

amount_entry = tk.Entry(root)
amount_entry.pack()

# Save Button

tk.Button(
    root,
    text="Save Transaction",
    command=save_expense,
    width=20
).pack(pady=20)

root.mainloop()