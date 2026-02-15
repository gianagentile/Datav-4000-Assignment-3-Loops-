# calculate total stock of each product
def calculate_total_stock(warehouses):
    total_stock = {}
    # loop 
    for warehouse in warehouses:
        inventory = warehouse["inventory"]
        for product in inventory:
            if product in total_stock:
                total_stock[product] += inventory[product]
            else:
                total_stock[product] = inventory[product]
    return total_stock

# print summary of supply chain 
def print_summary(total_stock):
    print("Supply Chain Inventory Summary:")
    for product in total_stock:
        print(product + ":", total_stock[product])
        
def main():
    warehouses = [
        {"name": "Warehouse A", "inventory": {"Apples": 100, "Bananas": 150}},
        {"name": "Warehouse B", "inventory": {"Apples": 200, "Bananas": 100}},
    ]
    total_stock = calculate_total_stock(warehouses)
    print_summary(total_stock)

main()