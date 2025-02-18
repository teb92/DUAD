import PySimpleGUI as sg
from GUI_interface import main_window, expense_window, income_window, read_csv_file, add_new_category, category_validation, load_categories
from write_read_csv import read_csv_file

window = main_window()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "add_expense":
        expense_window()
        expenses, incomes = read_csv_file()
        window["expenses_table"].update(values=expenses)
        window.refresh() 
    elif event == "add_income":
        income_window()
        expenses, incomes = read_csv_file()
        window["income_table"].update(values=incomes)
        window.refresh() 
    elif event == "Add New Category":
        new_category = sg.popup_get_text("Enter new category:")
        if new_category:
            add_new_category(new_category)
            categories = sorted(load_categories())

window.close()