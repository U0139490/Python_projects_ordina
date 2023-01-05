import csv
import datetime
# Create the CSV file and write the field names
with open('expenses.csv', 'w', newline='') as f:
    fieldnames = ['date', 'description', 'amount', 'category']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()



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

# Add some example expenses
add_expense('Groceries', 50.0, 'Food')
add_expense('Rent', 800.0, 'Housing')
add_expense('Gas', 30.0, 'Transportation')
add_expense('Gym Membership', 50.0, 'Fitness')
add_expense('Coffee', 3.0, 'Food')