import csv
import argparse
import datetime
import matplotlib.pyplot as plt

def read_data():
    """Reads the data from the expenses.csv file and returns a list of dictionaries."""
    expenses = []
    with open('expenses.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(row)
    return expenses

def add_expense(description, amount, category):
    """Adds a new expense to the expenses.csv file."""
    with open('expenses.csv', 'a', newline='') as f:
        fieldnames = ['date', 'description', 'amount', 'category']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({
            'date': datetime.datetime.now().strftime('%Y-%m-%d'),
            'description': description,
            'amount': amount,
            'category': category
        })

def view_expenses(sort_by='date'):
    """Displays a list of all expenses sorted by the specified field."""
    expenses = read_data()
    if sort_by == 'date':
        expenses = sorted(expenses, key=lambda x: x['date'])
    elif sort_by == 'amount':
        expenses = sorted(expenses, key=lambda x: float(x['amount']))
    elif sort_by == 'category':
        expenses = sorted(expenses, key=lambda x: x['category'])
    for expense in expenses:
        print(f"{expense['date']}: {expense['description']} ({expense['amount']}: {expense['category']})")

def analyze_expenses():
    """Generates a summary of expenses by category and a pie chart showing the percentage of expenses in each category."""
    expenses = read_data()
    categories = {}
    total_amount = 0
    for expense in expenses:
        amount = float(expense['amount'])
        category = expense['category']
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
        total_amount += amount
    print("Expense Summary:")
    for category, amount in categories.items():
        print(f"{category}: {amount} ({amount / total_amount:.2f}%)")
    plt.pie([amount for amount in categories.values()], labels=[category for category in categories.keys()], autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['add', 'view', 'analyze'])
    parser.add_argument('--description', required=False)
    parser.add_argument('--amount', required=False, type=float)
    parser.add_argument('--category', required=False)
    parser.add_argument('--sort_by', required=False, choices=['date', 'amount', 'category'], default='date')
    args = parser.parse_args()
    if args.action == 'add':
        add_expense(args.description, args.amount, args.category)
    elif args.action == 'view':
        view_expenses(sort_by=args.sort_by)
    elif args.action == 'analyze':
        analyze_expenses()
