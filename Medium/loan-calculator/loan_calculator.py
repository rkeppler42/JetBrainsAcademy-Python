import math
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--interest")
parser.add_argument("--periods")

args = parser.parse_args()

interest = float(args.interest) / 100 / 12


def calculate_principal(a, i, n):
    principal = a / (i * (1 + i) ** n / ((1 + i) ** n - 1))
    print(f"Your loan principal = {round(principal)}!")


def calculate_monthly_payment(p, i, n):
    monthly_payment = p * (i * (1 + i) ** n / ((1 + i) ** n - 1))
    print(f"Your monthly payment = {math.ceil(monthly_payment)}!")


def calculate_periods(a, i, p):
    periods = math.ceil(math.log(a / (a - i * p), 1 + i))
    years = periods // 12
    months = periods % 12

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

    print(f"Your periods = {math.ceil(periods)}")


if args.principal is None:
    calculate_principal(float(args.payment), interest, int(args.periods))
elif args.payment is None:
    calculate_monthly_payment(float(args.principal), interest, int(args.periods))
elif args.periods is None:
    calculate_periods(float(args.payment), interest, float(args.principal))
