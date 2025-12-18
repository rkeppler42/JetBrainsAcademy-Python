import math
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--interest")
parser.add_argument("--periods")

args = parser.parse_args()


def validate_arguments():
    number_of_arguments = 0
    number_of_negative_arguments = 0
    for arg in vars(args):
        if vars(args)[arg] is not None:
            number_of_arguments += 1
            if arg != "type" and float(vars(args)[arg]) < 0:
                number_of_negative_arguments += 1

    if args.type != "annuity" and args.type != "diff":
        return False
    elif args.type == "diff" and args.payment is not None:
        return False
    elif args.interest is None:
        return False
    elif number_of_arguments < 4:
        return False
    elif number_of_negative_arguments > 0:
        return False
    else:
        return True


def calculate_differentiated_payments(p, i, n):
    total = 0
    for month in range(1, n + 1):
        differentiated_payments = math.ceil(p / n + i * (p - ((p * (month - 1)) / n)))
        total += differentiated_payments
        print(f"Month {month}: payment is {differentiated_payments}")
    print()
    calculate_overpayment(total, p)


def calculate_principal(a, i, n):
    principal = a / (i * (1 + i) ** n / ((1 + i) ** n - 1))
    total = a * n
    print(f"Your loan principal = {math.floor(principal)}!")
    calculate_overpayment(total, principal)


def calculate_annuity_payment(p, i, n):
    annuity_payment = math.ceil(p * (i * (1 + i) ** n / ((1 + i) ** n - 1)))
    total = annuity_payment * n
    print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
    calculate_overpayment(total, p)


def calculate_periods(a, i, p):
    periods = math.ceil(math.log(a / (a - i * p), 1 + i))
    years = periods // 12
    months = periods % 12
    total = a * periods
    if years > 0 and months > 0:
        year_word = "year" if years == 1 else "years"
        month_word = "month" if months == 1 else "months"
        print(f"It will take {years} {year_word} and {months} {month_word} to repay this loan!")
    elif years > 0:
        year_word = "year" if years == 1 else "years"
        print(f"It will take {years} {year_word} to repay this loan!")
    else:
        month_word = "month" if months == 1 else "months"
        print(f"It will take {months} {month_word} to repay this loan!")
    calculate_overpayment(total, p)


def calculate_overpayment(total_amount_paid, principal):
    print(f"Overpayment = {math.ceil(total_amount_paid - principal)}")


if validate_arguments():
    interest = float(args.interest) / 100 / 12
    if args.type == "annuity":
        if args.principal is None:
            calculate_principal(float(args.payment), interest, int(args.periods))
        elif args.payment is None:
            calculate_annuity_payment(float(args.principal), interest, int(args.periods))
        elif args.periods is None:
            calculate_periods(float(args.payment), interest, float(args.principal))
    else:
        calculate_differentiated_payments(float(args.principal), interest, int(args.periods))

else:
    print("Incorrect parameters")