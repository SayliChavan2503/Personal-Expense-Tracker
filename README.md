# Personal Expense Tracker

## Ediglobe Internship Project

### Project Description
Personal Expense Tracker is a Python command-line application for recording, managing, analyzing, and visualizing personal expenses.

The application stores the amount, category, date, and description of each expense. It also provides reports, charts, search, edit/delete functionality, and monthly budget management.

### Features
- Add an expense
- View all expenses
- Generate expense reports
- Calculate total and average spending
- Identify highest and lowest expenses
- Category-wise spending report
- Monthly spending report
- Search by category
- Edit an expense
- Delete an expense
- Bar chart visualization
- Pie chart visualization
- Set and view monthly budget
- Save expense data to CSV
- Error handling for invalid input

### Technologies Used
- Python
- CSV file handling
- Matplotlib
- datetime
- Lists and dictionaries
- Functions
- Loops and conditional statements
- try-except error handling

### Files
- `expense_tracker.py` - Main application
- `expenses.csv` - Expense data file (created/updated by the application)
- `budget.txt` - Monthly budget file (created/updated by the application)
- `requirements.txt` - Required external Python package
- `README.md` - Project information

### How to Run

1. Install Python 3.
2. Open this folder in VS Code or Command Prompt.
3. Install the required package:

   `python -m pip install -r requirements.txt`

4. Run the application:

   `python expense_tracker.py`

5. Follow the menu displayed in the terminal.

### Main Menu
1. Add an Expense
2. View All Expenses
3. Generate Report
4. Monthly Report
5. Search by Category
6. Delete an Expense
7. View Charts
8. Save
9. Save and Exit
10. Edit an Expense
11. Budget Management

### Data Storage
Expense records are stored in `expenses.csv`. The monthly budget is stored in `budget.txt`.

The application can create these files when required, so they do not need to contain sample data for a fresh submission.

### Submission Note
This project is prepared as an Ediglobe internship project submission. It is a command-line Python application with expense recording, file storage, reporting, visualization, search/edit/delete functionality, budget management, and input error handling.
