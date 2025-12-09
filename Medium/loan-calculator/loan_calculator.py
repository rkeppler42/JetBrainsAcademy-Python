import math


def enter_loan_principal():
    print("Enter the loan principal:")
    return int(input())


def what_to_calculate():
    print("What do you want to calculate?")
    print('type "m" - for number of monthly payments,')
    print('type "p" - for monthly payment:')
    user_input = input()
    while user_input != 'm' and user_input != 'p':
        print('Please enter either "m" or "p"')
        user_input = input()
    return user_input


def which_option(user_input, loan_principal):
    if user_input == 'm':
        calculate_number_monthly_payment(loan_principal)
    else:
        calculate_monthly_payment(loan_principal)


def calculate_number_monthly_payment(loan_principal):
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    print()
    print(f"It will take {math.ceil(loan_principal / monthly_payment)} months to repay the loan")


def calculate_monthly_payment(loan_principal):
    print("Enter the number of months:")
    number_of_months = int(input())
    monthly_payment = loan_principal / number_of_months
    print()
    if monthly_payment.is_integer():
        monthly_payment = int(monthly_payment)
        print("Your monthly payment =", monthly_payment)
    else:
        monthly_payment = math.ceil(monthly_payment)
        last_monthly_payment = loan_principal - (number_of_months - 1) * monthly_payment
        print("Your monthly payment =", monthly_payment, "and the last payment =", last_monthly_payment)


loan = enter_loan_principal()
user_input = what_to_calculate()
which_option(user_input, loan)