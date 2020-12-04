"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def display_report(num_month,incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month,income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month+1, income, total))

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_month = int(input("How many months? "))

    for month in range(1, num_month + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    display_report(num_month,incomes)

main()
