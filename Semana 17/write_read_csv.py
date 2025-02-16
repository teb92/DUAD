import csv
import os

FINANCE_FILE = 'finance.csv'
CATEGORIES_FILE = 'categories.csv'


def load_categories():
    categories = set()
    if os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    categories.add(row[0].lower()) 
    return categories


def save_categories(categories):
    with open(CATEGORIES_FILE, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Category"]) 
        for category in categories:
            writer.writerow([category])

allowed_categories = load_categories()

if not allowed_categories:
    allowed_categories.update({"food", "transport", "entertainment", "health", "education", "freelance"})
    save_categories(allowed_categories)

info_headers = ('transaction_type', 'category', 'amount')


def category_validation(category):
    return category.lower() in allowed_categories


def add_new_category(category):
    if category.lower() in allowed_categories:
        print(f"Category '{category}' already exists.")
    else:
        allowed_categories.add(category.lower())
        save_categories(allowed_categories)
        print(f"Category '{category}' has been added successfully.")


def add_transaction(transaction_type, category, amount):
    try:
        amount = float(amount)
        if amount < 0:
            return "Amount cannot be negative."
    except ValueError:
        return "Invalid amount entered."

    if not category_validation(category):
        return f"Category '{category}' does not exist. Please add it first."
    
    transaction = {'transaction_type': transaction_type, 'category': category, 'amount': amount}
    write_csv_file(FINANCE_FILE, [transaction], info_headers)
    
    return "Transaction added successfully."


def write_csv_file(file_path, data, headers):
    file_exists = os.path.exists(file_path)
    with open(file_path, 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)


def read_csv_file():
    expenses = []
    incomes = []
    if os.path.exists(FINANCE_FILE):
        with open(FINANCE_FILE, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['transaction_type'] == "expense":
                    expenses.append([row['category'], float(row['amount'])])
                elif row['transaction_type'] == "income":
                    incomes.append([row['category'], float(row['amount'])])
    return expenses, incomes