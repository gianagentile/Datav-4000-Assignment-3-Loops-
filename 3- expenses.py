# calculate totals for each category 

def calculate_category_totals(expenses):
    category_totals = {}
#loop through each category 
    for category in expenses:
        total = 0 
        for amount in expenses[category]:
            total += amount
        category_totals[category]= total
    return category_totals

#print out expense report 
def print_report(totals):
    grand_total = 0
    print("Expense Summary Report\n")

    for category in totals:
        print(category + " Total:", totals[category])
        grand_total += totals[category]
    print("\nGrand Total:", grand_total)

def main():
    expenses = {
        "Travel": [500,200],
        "Meals": [40,60,30],
        "Supplies":[100]
    }
    totals = calculate_category_totals(expenses)
    print_report(totals)

main()