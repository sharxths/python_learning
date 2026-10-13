
import datetime

date = datetime.date.today()

account = {
    "name": "Sharath",
    "balance": 100000
}

expenses = []
categories = set()

expense_categories = (
    "Food", "Travel", "Grocery",
    "Education", "Shopping", "Others"
)

while True:
    print("\n========== PERSONAL FINANCE TRACKER ==========")
    print("1. Check Balance")
    print("2. Add Income")
    print("3. Add Expense")
    print("4. View Transaction History")
    print("5. View Financial Summary")
    print("6. Exit")

    service = input("Choose an option: ")

    if service == "1":
        print("Account holder:", account["name"])
        print("Current balance: ₹", account["balance"])

    elif service == "2":
        source = input("Enter new source of income: ")
        amount = float(input("Enter income amount: ₹"))

        if amount > 0:
            account["balance"] += amount

            transaction = {
                "type": "Income",
                "description": source,
                "amount": amount
            }

            expenses.append(transaction)

            print("Income added successfully!")
            print("Income source:", source)
            print("Amount: ₹", amount)
            print("Current balance: ₹", account["balance"])

        else:
            print("Amount must be greater than zero!")

    elif service == "3":
        description = input("Enter the expense description: ")

        print("Available categories:", expense_categories)
        category = input("Enter the expense category: ")

        if category in expense_categories:
            amount = float(input("Enter the expense amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero!")

            elif amount > account["balance"]:
                print("Insufficient balance!")

            else:
                account["balance"] -= amount

                transaction = {
                    "type": "Expense",
                    "description": description,
                    "category": category,
                    "amount": amount
                }

                expenses.append(transaction)
                categories.add(category)

                print("Expense recorded successfully!")
                print("Description:", description)
                print("Category:", category)
                print("Amount: ₹", amount)
                print("Remaining balance: ₹", account["balance"])

        else:
            print("Invalid category!")

    elif service == "4":
        if len(expenses) == 0:
            print("No transactions listed yet.")

        else:
            print("\n========== TRANSACTION HISTORY ==========")

            for transaction in expenses:
                print("Type:", transaction["type"])
                print("Description:", transaction["description"])
                print("Amount: ₹", transaction["amount"])

                if transaction["type"] == "Expense":
                    print("Category:", transaction["category"])

                print("-------------------------------------")

    elif service == "5":
        total_income = 0
        total_expenses = 0
        expense_amounts = []

        for transaction in expenses:
            if transaction["type"] == "Income":
                total_income += transaction["amount"]

            elif transaction["type"] == "Expense":
                total_expenses += transaction["amount"]
                expense_amounts.append(transaction["amount"])

        print("\n========== FINANCIAL SUMMARY ==========")
        print("Account Holder:", account["name"])
        print("Total Income: ₹", total_income)
        print("Total Expenses: ₹", total_expenses)
        print("Current Balance: ₹", account["balance"])
        print("Total Transactions:", len(expenses))
        print("Expense Categories:", categories)

        if len(expense_amounts) > 0:
            print("Highest Expense: ₹", max(expense_amounts))
            print("Lowest Expense: ₹", min(expense_amounts))
        else:
            print("No expenses recorded yet.")

    elif service == "6":
        print("\n========== SESSION SUMMARY ==========")
        print("Account Holder:", account["name"])
        print("Date:", date)
        print("Final Balance: ₹", account["balance"])
        print("Thank you for using Personal Finance Manager!")
        break

    else:
        print("Invalid choice! Please select an option from 1 to 6.")
