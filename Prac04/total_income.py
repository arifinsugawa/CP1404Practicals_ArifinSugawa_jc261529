def main():
    incomes = []
    number_of_months = int(input("Please Input The Number of Months? "))

    for month in range(1, number_of_months + 1):
        income = float(
            input("Please Enter the Income for the Month {}: ".format(month)))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))


main()