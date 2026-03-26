class ExpenseView:
    def show_expenses(self,expenses):
        if not expenses:
            print("List is empty")
            return
        print("List of expenses:")
        for e in expenses:
            print(f"ID: {e.id} | {e.name} | {e.amount}")
    
    def show_total(self,total):
        print(f"Total amount: {total}")
    
    def show_message(self, message):
        print(message)