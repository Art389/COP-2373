# A program that allows users to store their monthly expenses and then the program totals the expenses. It also shows the highest and lowest monthly expense.


from functools import reduce

# Asks the user to enter the monthly expenses.
def get_expenses():
    expenses = []
    while True:
        expense_name = input("Enter expense type or type '+' to end): ")
        if expense_name.lower() == '+':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_name}: "))
            expenses.append((expense_name, amount))
        except ValueError:
            print("Error. Please enter a number.")
    return expenses

# the function analyzes the inputted expenses.
def analyze_expenses(expenses):
    if not expenses:
        return {"total": 0, "highest": None, "lowest": None}
    
    # Uses reduce to calculate the total, highest, and lowest expense.
    total_expense = reduce(lambda acc, exp: acc + exp[1], expenses, 0)
    highest_expense = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)
    lowest_expense = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)
    
    # returns a dictionary containing these values.
    return {
        "total": total_expense,
        "highest": highest_expense,
        "lowest": lowest_expense
    }

# main funtion for running the program
def main():
    expenses = get_expenses()
    results = analyze_expenses(expenses)
    
    # displays the results
    print(f"\nTotal Expenses: ${results['total']:.2f}")
    if results['highest']:
        print(f"Highest Expense: {results['highest'][0]} - ${results['highest'][1]:.2f}")
    if results['lowest']:
        print(f"Lowest Expense: {results['lowest'][0]} - ${results['lowest'][1]:.2f}")

if __name__ == "__main__":
    main()
