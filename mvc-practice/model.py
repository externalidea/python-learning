class Expense:
    def __init__(self, expense_id, name, amount):
        self.id = expense_id
        self.name = name
        self.amount = amount


class ExpenseModel:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self, name, amount):
        expense = Expense(self.next_id, name, amount)
        self.expenses.append(expense)
        self.next_id += 1

    def delete_expense(self, expense_id):
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_expenses(self):
        return self.expenses

    def get_total_amount(self):
        total = 0
        for e in self.expenses:
            total += e.amount
        return total