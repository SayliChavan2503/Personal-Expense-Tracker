import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"
BUDGET_FILE = "budget.txt"



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")



def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    expenses.append({
                        "amount": float(row["amount"]),
                        "category": row["category"],
                        "date": row["date"],
                        "description": row["description"]
                    })

        except (ValueError, KeyError):
            print("Error reading expense file.")

    return expenses


def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["amount", "category", "date", "description"]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for expense in expenses:
                writer.writerow(expense)

        print("\nExpenses saved successfully!")

    except Exception as e:
        print("\nError saving expenses:", e)


def add_expense(expenses):

    clear_screen()

    print("==========================================")
    print("             ADD EXPENSE")
    print("==========================================")

    while True:
        try:
            amount = float(input("\nEnter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

   
    categories = [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Education",
        "Medical",
        "Bills",
        "Other"
    ]

    print("\nSelect Category:")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:
        try:
            category_choice = int(
                input("\nEnter category number: ")
            )

            if 1 <= category_choice <= len(categories):
                category = categories[category_choice - 1]
                break
            else:
                print("Please select a valid category.")

        except ValueError:
            print("Please enter a number.")

    while True:

        date = input(
            "\nEnter date (YYYY-MM-DD)"
            "\nor press Enter for today's date: "
        ).strip()

        if date == "":
            date = datetime.now().strftime("%Y-%m-%d")
            break

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date format.")
            print("Please use YYYY-MM-DD.")

    description = input(
        "\nEnter description (optional): "
    ).strip()

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    expenses.append(expense)

    print("\n------------------------------------------")
    print("Expense added successfully!")
    print("------------------------------------------")


def view_expenses(expenses):

    clear_screen()

    print("==========================================")
    print("            ALL EXPENSES")
    print("==========================================")

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print()

    print(
        f"{'No.':<5}"
        f"{'Date':<15}"
        f"{'Category':<18}"
        f"{'Amount':<15}"
        f"{'Description'}"
    )

    print("-" * 80)

    for i, expense in enumerate(expenses, 1):

        print(
            f"{i:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<18}"
            f"₹{expense['amount']:<14.2f}"
            f"{expense['description']}"
        )


def category_report(expenses):

    print("\n==========================================")
    print("          CATEGORY-WISE REPORT")
    print("==========================================")

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    total = sum(category_totals.values())

    print()

    print(
        f"{'Category':<20}"
        f"{'Amount':<15}"
        f"{'Percentage'}"
    )

    print("-" * 50)

    for category, amount in category_totals.items():

        percentage = (amount / total) * 100

        print(
            f"{category:<20}"
            f"₹{amount:<14.2f}"
            f"{percentage:.2f}%"
        )

    print("-" * 50)

    print(f"Total Spending: ₹{total:.2f}")


def generate_report(expenses):

    clear_screen()

    print("==========================================")
    print("             EXPENSE REPORT")
    print("==========================================")

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    average = total / len(expenses)

    highest = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    lowest = min(
        expenses,
        key=lambda expense: expense["amount"]
    )

    print()

    print(f"Number of Expenses : {len(expenses)}")
    print(f"Total Spending     : ₹{total:.2f}")
    print(f"Average Expense    : ₹{average:.2f}")

    print(
        f"Highest Expense    : ₹{highest['amount']:.2f}"
    )

    print(
        f"Category           : {highest['category']}"
    )

    print(
        f"Lowest Expense     : ₹{lowest['amount']:.2f}"
    )

    print(
        f"Category           : {lowest['category']}"
    )

    category_report(expenses)

def monthly_report(expenses):

    clear_screen()

    print("==========================================")
    print("             MONTHLY REPORT")
    print("==========================================")

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    monthly_totals = {}

    for expense in expenses:

        month = expense["date"][:7]

        if month in monthly_totals:
            monthly_totals[month] += expense["amount"]
        else:
            monthly_totals[month] = expense["amount"]

    print()

    for month, amount in sorted(
        monthly_totals.items()
    ):
        print(f"{month} : ₹{amount:.2f}")


def search_by_category(expenses):

    clear_screen()

    print("==========================================")
    print("         SEARCH BY CATEGORY")
    print("==========================================")

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    category = input(
        "\nEnter category to search: "
    ).strip().lower()

    found = False

    print()

    for expense in expenses:

        if expense["category"].lower() == category:

            print(
                f"Date        : {expense['date']}"
            )

            print(
                f"Category    : {expense['category']}"
            )

            print(
                f"Amount      : ₹{expense['amount']:.2f}"
            )

            print(
                f"Description : {expense['description']}"
            )

            print("-" * 40)

            found = True

    if not found:
        print(
            "No expenses found for this category."
        )

def delete_expense(expenses):

    clear_screen()

    print("==========================================")
    print("           DELETE EXPENSE")
    print("==========================================")

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    view_expenses(expenses)

    while True:

        try:

            choice = int(
                input(
                    "\nEnter expense number to delete "
                    "(0 to cancel): "
                )
            )

            if choice == 0:

                print("\nDelete cancelled.")
                return

            if 1 <= choice <= len(expenses):

                removed = expenses.pop(choice - 1)

                print(
                    "\nExpense deleted successfully!"
                )

                print(
                    f"Deleted Amount: "
                    f"₹{removed['amount']:.2f}"
                )

                return

            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")



def edit_expense(expenses):

    clear_screen()

    print("==========================================")
    print("            EDIT EXPENSE")
    print("==========================================")

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    view_expenses(expenses)

    while True:

        try:

            choice = int(
                input(
                    "\nEnter expense number to edit "
                    "(0 to cancel): "
                )
            )

            if choice == 0:
                print("\nEdit cancelled.")
                return

            if 1 <= choice <= len(expenses):
                break

            print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    expense = expenses[choice - 1]

    print("\nCurrent Expense Details:")
    print(f"Amount      : ₹{expense['amount']:.2f}")
    print(f"Category    : {expense['category']}")
    print(f"Date        : {expense['date']}")
    print(f"Description : {expense['description']}")


    while True:

        new_amount = input(
            "\nEnter new amount "
            "(press Enter to keep current): "
        ).strip()

        if new_amount == "":
            break

        try:

            new_amount = float(new_amount)

            if new_amount <= 0:
                print(
                    "Amount must be greater than 0."
                )
            else:
                expense["amount"] = new_amount
                break

        except ValueError:
            print("Please enter a valid number.")

  
    categories = [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Education",
        "Medical",
        "Bills",
        "Other"
    ]

    print("\nCategories:")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:

        new_category = input(
            "\nEnter new category number "
            "(press Enter to keep current): "
        ).strip()

        if new_category == "":
            break

        try:

            new_category = int(new_category)

            if 1 <= new_category <= len(categories):

                expense["category"] = categories[
                    new_category - 1
                ]

                break

            print("Invalid category number.")

        except ValueError:
            print("Please enter a number.")

  
    while True:

        new_date = input(
            "\nEnter new date (YYYY-MM-DD)"
            "\nPress Enter to keep current: "
        ).strip()

        if new_date == "":
            break

        try:

            datetime.strptime(
                new_date,
                "%Y-%m-%d"
            )

            expense["date"] = new_date
            break

        except ValueError:
            print("Invalid date format.")

  
    new_description = input(
        "\nEnter new description "
        "(press Enter to keep current): "
    ).strip()

    if new_description != "":
        expense["description"] = new_description

    print("\n------------------------------------------")
    print("Expense updated successfully!")
    print("------------------------------------------")


def show_bar_chart(expenses):

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(10, 6))

    plt.bar(
        categories,
        amounts
    )

    plt.xlabel("Category")
    plt.ylabel("Amount Spent (₹)")
    plt.title("Category-wise Expense")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()


def show_pie_chart(expenses):

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 8))

    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution")

    plt.show()


def visualization_menu(expenses):

    while True:

        clear_screen()

        print("==========================================")
        print("           EXPENSE CHARTS")
        print("==========================================")

        print("\n1. Bar Chart")
        print("2. Pie Chart")
        print("3. Back to Main Menu")

        print("------------------------------------------")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            clear_screen()

            print("Opening Bar Chart...")

            show_bar_chart(expenses)

            pause()

        elif choice == "2":

            clear_screen()

            print("Opening Pie Chart...")

            show_pie_chart(expenses)

            pause()

        elif choice == "3":

            break

        else:

            print("\nInvalid choice.")

            pause()


def load_budget():

    if os.path.exists(BUDGET_FILE):

        try:

            with open(
                BUDGET_FILE,
                "r"
            ) as file:

                return float(
                    file.read().strip()
                )

        except ValueError:
            return 0

    return 0


def save_budget(budget):

    try:

        with open(
            BUDGET_FILE,
            "w"
        ) as file:

            file.write(str(budget))

        print("\nBudget saved successfully!")

    except Exception as e:

        print(
            "\nError saving budget:",
            e
        )


def budget_management(expenses):

    clear_screen()

    print("==========================================")
    print("          MONTHLY BUDGET")
    print("==========================================")

    budget = load_budget()

    if budget > 0:
        print(
            f"\nCurrent Monthly Budget: ₹{budget:.2f}"
        )
    else:
        print("\nNo monthly budget set.")

    print("\n1. Set Monthly Budget")
    print("2. View Budget Status")
    print("3. Back to Main Menu")

    choice = input(
        "\nEnter your choice: "
    ).strip()


    if choice == "1":

        while True:

            try:

                new_budget = float(
                    input(
                        "\nEnter monthly budget: ₹"
                    )
                )

                if new_budget <= 0:
                    print(
                        "Budget must be greater than 0."
                    )
                else:
                    save_budget(new_budget)
                    break

            except ValueError:

                print(
                    "Please enter a valid amount."
                )


    elif choice == "2":

        if budget <= 0:

            print(
                "\nPlease set a budget first."
            )

        else:

            current_month = datetime.now().strftime(
                "%Y-%m"
            )

            monthly_spending = 0

            for expense in expenses:

                if expense["date"][:7] == current_month:

                    monthly_spending += expense[
                        "amount"
                    ]

            remaining = budget - monthly_spending

            print("\n==========================================")
            print("          BUDGET STATUS")
            print("==========================================")

            print(
                f"\nMonthly Budget   : ₹{budget:.2f}"
            )

            print(
                f"Spent This Month : "
                f"₹{monthly_spending:.2f}"
            )

            if remaining >= 0:

                print(
                    f"Remaining        : "
                    f"₹{remaining:.2f}"
                )

            else:

                print(
                    f"Over Budget By   : "
                    f"₹{abs(remaining):.2f}"
                )

  
    elif choice == "3":

        return

    else:

        print("\nInvalid choice.")

    pause()


def main():

    expenses = load_expenses()

    while True:

        clear_screen()

        print("==========================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("==========================================")

        print(
            f"\nLoaded {len(expenses)} expense(s)."
        )

        print("\n--------------- MENU ----------------")

        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Generate Report")
        print("4. Monthly Report")
        print("5. Search by Category")
        print("6. Delete an Expense")
        print("7. View Charts")
        print("8. Save")
        print("9. Save and Exit")
        print("10. Edit an Expense")
        print("11. Budget Management")

        print("-------------------------------------")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_expense(expenses)
            pause()

        elif choice == "2":

            view_expenses(expenses)
            pause()

        elif choice == "3":

            generate_report(expenses)
            pause()

        elif choice == "4":

            monthly_report(expenses)
            pause()

        elif choice == "5":

            search_by_category(expenses)
            pause()

        elif choice == "6":

            delete_expense(expenses)
            pause()

        elif choice == "7":

            visualization_menu(expenses)

        elif choice == "8":

            save_expenses(expenses)
            pause()

        elif choice == "9":

            save_expenses(expenses)

            print(
                "\nThank you for using "
                "Personal Expense Tracker!"
            )

            break

        elif choice == "10":

            edit_expense(expenses)
            pause()

        elif choice == "11":

            budget_management(expenses)

        else:

            print("\nInvalid choice.")

            print(
                "Please enter a number from 1 to 11."
            )

            pause()

if __name__ == "__main__":
    main()