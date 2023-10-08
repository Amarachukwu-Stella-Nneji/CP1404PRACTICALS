"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for monthly_income over a given number of number_of_months."""
    monthly_income = []
    number_of_months = int(input("How many number_of_months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        monthly_income.append(income)
    print_report(number_of_months, monthly_income)


def print_report(number_of_months, monthly_income):
    """Print report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = monthly_income[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
