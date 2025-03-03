import datetime

class Transaction:
    def __init__(self, category, amount, transaction_type, date=None):
        self.category = category
        self.amount = amount
        self.transaction_type = transaction_type  # 'income' or 'expense'
        self.date = date if date else datetime.datetime.now()

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.category}: ${self.amount} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

class Budget:
    def __init__(self, category, budget_amount):
        self.category = category
        self.budget_amount = budget_amount
        self.spent_amount = 0

    def add_expense(self, amount):
        if self.spent_amount + amount > self.budget_amount:
            print(f"Warning: You are exceeding your budget in {self.category}!")
        self.spent_amount += amount

    def remaining_budget(self):
        return self.budget_amount - self.spent_amount

    def __str__(self):
        return f"{self.category}: Budget ${self.budget_amount}, Spent ${self.spent_amount}, Remaining ${self.remaining_budget()}"

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.budgets = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

        if transaction.transaction_type == 'expense':
            self.update_budget(transaction.category, transaction.amount)

    def add_budget(self, budget):
        self.budgets.append(budget)

    def update_budget(self, category, amount):
        for budget in self.budgets:
            if budget.category == category:
                budget.add_expense(amount)
                break

    def show_summary(self):
        print("\n--- Finance Summary ---")
        total_income = sum(t.amount for t in self.transactions if t.transaction_type == 'income')
        total_expense = sum(t.amount for t in self.transactions if t.transaction_type == 'expense')
        print(f"Total Income: ${total_income}")
        print(f"Total Expense: ${total_expense}")
        print(f"Net Balance: ${total_income - total_expense}\n")

    def show_transaction_history(self):
        print("\n--- Transaction History ---")
        for t in self.transactions:
            print(t)

    def show_budget_status(self):
        print("\n--- Budget Status ---")
        for budget in self.budgets:
            print(budget)

# Usage Example
finance_tracker = FinanceTracker()

# Adding some budgets
finance_tracker.add_budget(Budget('Food', 300))
finance_tracker.add_budget(Budget('Entertainment', 150))
finance_tracker.add_budget(Budget('Transport', 100))

# Adding some transactions
finance_tracker.add_transaction(Transaction('Food', 50, 'expense'))
finance_tracker.add_transaction(Transaction('Food', 30, 'expense'))
finance_tracker.add_transaction(Transaction('Entertainment', 100, 'expense'))
finance_tracker.add_transaction(Transaction('Salary', 2000, 'income'))

# Displaying the summaries
finance_tracker.show_summary()
finance_tracker.show_transaction_history()
finance_tracker.show_budget_status()
