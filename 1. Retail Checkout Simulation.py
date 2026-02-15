# collect price from user 
from itertools import count


def get_prices():
    prices = []
# ask for first price and loop until user enters 0
    price = float(input("Enter item price (0 to finish): "))
    while price != 0:
        if price > 0:
            prices.append(price)
        else:
            print("Price must be positive.")
        price = float(input("Enter item price (0 to finish): "))
    return prices

# cacluate total cost 
def calculate_total(prices):
    return sum(prices)

# caculate avergae price 
def calculate_average(prices):
    if len(prices) == 0:
        return 0
    return sum(prices) / len(prices)

# display final results 
def display_results(prices):
    total = calculate_total(prices)
    average = calculate_average(prices)
    count = len(prices)

    print("\nItems bought:", count)
    print("Total cost:", total)
    print("Average price:", average)


def main():
    prices = get_prices()
    display_results(prices)

main()