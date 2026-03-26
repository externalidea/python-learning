from model import ExpenseModel
from view import ExpenseView
class ExpenseController:
    def __init__(self):
        self.model = ExpenseModel()
        self.view = ExpenseView()
    
    def add_expense(self, name ,amount):
        self.model.add_expense(self,name,amount)
        self.view.show_message("Expense added")
    
    def del_expense(self,id):
        self.model.del_expense(id)
        self.view.show_message("Expense was deleted")
    
    def show_all_expenses(self):
        expenses = self.model.get_expenses()
        self.view.show_expenses(expenses)
    
    def show_total(self):
        total = self.model.get_total_amount()
        self.view.show_total(total)
