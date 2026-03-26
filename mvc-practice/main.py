from controller import ExpenseController

controller = ExpenseController()

controller.add_expense("Food", 100)
controller.add_expense("Taxi", 50)

controller.show_all_expenses()
controller.show_total()

controller.del_expense(1)

controller.show_all_expenses()
controller.show_total()