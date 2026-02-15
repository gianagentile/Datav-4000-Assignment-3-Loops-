# caculate remaining loan balance 
def update_balance(balance, monthly_payment, intrest_rate):
    balance += balance * intrest_rate / 100 / 12
    balance -= monthly_payment
    return balance

# simulate the loan payment process
def simulate_loan_payment(balance, intrest_rate, monthly_payment):
    months = 0
#loop 
    while balance > 0:
        balance = update_balance(balance, monthly_payment, intrest_rate)
        months += 1
        if balance < 0:
            balance = 0
    return months

def main():
    loan_amount = float(input("Enter the loan amount: "))
    annual_intrest_rate = float(input("Enter the annual intrest rate (in %): "))
    monthly_payment = float(input("Enter the monthly payment amount: "))        
    months_needed = simulate_loan_payment(loan_amount, annual_intrest_rate, monthly_payment)
    print("\nIt will take", months_needed, "months to pay off the loan.")

main()