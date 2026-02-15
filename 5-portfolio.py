# calculate total value of portfolio
def calculate_portfolio_value(portfolio):
    total_value = 0 
#loop 
    for stock in portfolio:
       shares = portfolio[stock]['shares']
       price = portfolio[stock]['price']  
       total_value += shares * price
    return total_value

#print summary 
def print_portfolio_value(portfolio):
    total_value = calculate_portfolio_value(portfolio)
    print("Portfolio Summary:")
    for stock in portfolio:
        shares = portfolio[stock]['shares']
        price = portfolio[stock]['price']  
        value = shares * price
        print(stock, "-", shares, "shares @", price, "=", value)
    print("Total Portfolio Value:", total_value)

def main():
    portfolio = {
        'AAPL': {'shares': 10, 'price': 170},
        'TSLA': {'shares': 4, 'price': 250},
        'AMZN': {'shares': 2, 'price': 130}
    }
    print_portfolio_value(portfolio)
main()

#bonus 
import random

def simulate_week(portfolio, days=5):
    print("\nSimulating daily price changes...\n")
    for day in range(1, days + 1):
        for stock in portfolio:
            change_percent = random.uniform(-0.05, 0.05)  # ±5%
            portfolio[stock]["price"] *= (1 + change_percent)
            portfolio[stock]["price"] = round(portfolio[stock]["price"], 2)
        print("Day", day)
        print_portfolio_value(portfolio)
        print()
