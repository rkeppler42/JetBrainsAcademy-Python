print("Enter the loan principal:")
loan_principal = float(input("> "))
print("Enter the monthly payment:")
monthly_payment = float(input("> "))
print()
months_to_pay = loan_principal / monthly_payment
print(f"It will take {months_to_pay} months to repay the loan")