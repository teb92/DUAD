import PySimpleGUI as sg
from GUI_interface import main_window, expense_window, income_window
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
        window.refresh()  # Refresh the entire window
    elif event == "add_income":
        income_window()
        expenses, incomes = read_csv_file()
        window["income_table"].update(values=incomes)
        window.refresh()  # Refresh the entire window

window.close()