import json

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from a file, if it exists."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        """Save the expenses to a file."""
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, description, category, amount):
        """Add a new expense."""
        expense = {
            "description": description,
            "category": category,
            "amount": amount
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Your Expenses:")
            for i, expense in enumerate(self.expenses, 1):
                print(f"{i}. {expense['description']} ({expense['category']}) - ${expense['amount']:,.2f}")

    def summarize_expenses(self):
        """Summarize total expenses by category."""
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            summary[category] = summary.get(category, 0) + expense['amount']
        
        if not summary:
            print("No expenses to summarize.")
        else:
            print("Expenses Summary by Category:")
            for category, total in summary.items():
                print(f"{category}: ${total:,.2f}")


# Example usage
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter description of expense: ")
            category = input("Enter category (e.g., Food, Entertainment, Bills): ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(description, category, amount)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.summarize_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
