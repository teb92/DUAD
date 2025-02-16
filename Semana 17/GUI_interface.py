import PySimpleGUI as sg
from write_read_csv import add_transaction, read_csv_file, add_new_category, category_validation 

def expense_window():
    layout = [
        [sg.Text("Add Expense")],
        [sg.Text("Category"), sg.InputText(key="category")],
        [sg.Text("Amount"), sg.InputText(key="amount")],
        [sg.Button("Add"), sg.Button("Cancel")]
    ]

    window = sg.Window("Add Expense", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        elif event == "Add":
            category = values["category"]
            amount = values["amount"]
            
            if not category_validation(category): 
                add_category_popup_layout = [
                    [sg.Text(f"Category '{category}' does not exist. Add it? ")],
                    [sg.Button("Yes"), sg.Button("No")]
                ]
                add_category_popup = sg.Window("Add Category?", add_category_popup_layout, modal=True) 
                popup_event, popup_values = add_category_popup.read()
                add_category_popup.close()

                if popup_event == "Yes":
                    add_new_category(category) 
                    msg = add_transaction("expense", category, amount) 
                    sg.popup(msg)
                    if msg == "Transaction added successfully.":
                        window.close()
                        return
                else:  
                    continue 
            else: 
                msg = add_transaction("expense", category, amount) # Add the transaction
                sg.popup(msg)
                if msg == "Transaction added successfully.":
                    window.close()
                    return

    window.close()


def income_window():
    layout = [
        [sg.Text("Add Income")],
        [sg.Text("Category"), sg.InputText(key="category")],
        [sg.Text("Amount"), sg.InputText(key="amount")],
        [sg.Button("Add"), sg.Button("Cancel")]
    ]

    window = sg.Window("Add Income", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        elif event == "Add":
            category = values["category"]
            amount = values["amount"]

            if not category_validation(category):  
                add_category_popup_layout = [
                    [sg.Text(f"Category '{category}' does not exist. Add it? ")],
                    [sg.Button("Yes"), sg.Button("No")]
                ]
                add_category_popup = sg.Window("Add Category?", add_category_popup_layout, modal=True) 
                popup_event, popup_values = add_category_popup.read()
                add_category_popup.close()

                if popup_event == "Yes":
                    add_new_category(category) 
                    msg = add_transaction("income", category, amount)  
                    sg.popup(msg)
                    if msg == "Transaction added successfully.":
                        window.close()
                        return
                else: 
                    continue  
            else:  
                msg = add_transaction("income", category, amount)  
                sg.popup(msg)
                if msg == "Transaction added successfully.":
                    window.close()
                    return

    window.close()


def main_window():
    expenses, incomes = read_csv_file()

    layout = [
        [sg.Text("Personal Finance Management System", font=("Calibri", 20), justification="center", expand_x=True)],

        [
            sg.Column([
                [sg.Text("Expenses", font=("Calibri", 14), justification="center", expand_x=True)],
                [sg.Table(values=expenses, headings=['Category', 'Amount'],
                            num_rows=10, auto_size_columns=False, col_widths=[15, 10], justification='center',
                            expand_x=True, key="expenses_table")],
                [sg.Button("Add Expense", key="add_expense", expand_x=True)]
            ], element_justification='center', expand_x=True),

            sg.Column([
                [sg.Text("Income", font=("Calibri", 14), justification="center", expand_x=True)],
                [sg.Table(values=incomes, headings=['Category', 'Amount'],
                            num_rows=10, auto_size_columns=False, col_widths=[15, 10], justification='center',
                            expand_x=True, key="income_table")],
                [sg.Button("Add Income", key="add_income", expand_x=True)]
            ], element_justification='center', expand_x=True)
        ]
    ]

    return sg.Window("Personal Finance Management System", layout, size=(800, 500))