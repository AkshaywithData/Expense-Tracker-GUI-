# Expense Tracker

## Project Overview

This project is a desktop-based Expense Tracker created using Python and Tkinter. 
It helps users record and manage daily income and expense transactions.

## Features

- Record income and expense transactions
- User-friendly desktop interface using Tkinter
- Automatic monthly worksheet creation
- Daily closing balance recording
- Saves all transactions in Excel   
- Standalone executable created using PyInstaller   


## Technologies Used

- Python
- Tkinter
- OpenPyXL
- Datetime
- OS
- PyInstaller

## How to Run

```text
dist/Expense_Tracker.exe
```

## Create Standalone Executable

    PyInstaller is used to package the Python application into a standalone Windows executable.

    Install PyInstaller:

    ```bash
    pip install pyinstaller
    ```
    Build the executable:

    ```bash
    pyinstaller --onefile --windowed expense_Tracker.py
    ```
    The executable will be created inside:

    dist/
      └── expense_Tracker.exe

## Project Structure

```
Expense-Tracker/
│
├── .gitignore
├── expense_Tracker.py
├── README.md
├── LICENSE
├── requirements.txt
│
├── Screenshots/
│   ├── application.png
│   └── excel_output.png
│
├── dist/
│   └── Expense_Tracker.exe
│
└── Expenses-2026.xlsx
```

## Output

- The application stores transaction data in a new or existing workbook
- The workbook contains monthly worksheets for organizing income and expense transactions 
- Daily balances are maintained within the workbook.

## Future Improvements

- Add expense categories and filtering
- Add monthly expense summaries
- Add charts and visual reports
- Add database integration
- Add email/report automation

## License

This project is licensed under the MIT License.

## Author

**Akshay Gawand**


