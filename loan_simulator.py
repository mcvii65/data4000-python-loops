"""Bank Loan Repayment Simulator"""

loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (percent): "))
monthly_payment = float(input("Enter the monthly payment: "))

monthly_rate = annual_interest_rate / 100 / 12
balance = loan_amount
months = 0

print("\nLoan Repayment Schedule")
while balance > 0:
    interest = balance * monthly_rate
    if monthly_payment <= interest:
        print("The monthly payment is too low to reduce the balance.")
        break

    balance = balance + interest - monthly_payment
    months += 1

    if balance < 0:
        balance = 0

    print(f"Month {months}: Balance remaining = ${balance:.2f}")

print(f"\nThe loan is paid off in {months} months.")
